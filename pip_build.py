import contextlib
import os
import shutil
import subprocess
import sys

from imlresearch.src.testing.master.master_test_runner import run_tests

ROOT_DIR = os.getcwd()
HOME_DIR = os.path.expanduser("~")
BUILD_DIR = os.path.join(HOME_DIR, "tmp", "imlresearch_builds")
DIST_DIRS = ["dist", "imlresearch.egg-info"]


class BuildFailed(Exception):
    pass


def run_unit_tests():
    print("Running unit tests...")
    result = run_tests()
    if len(result.errors) + len(result.failures) > 0:
        raise BuildFailed("Some unit tests failed!")
    print("All unit tests passed!")


def run_code_style_checks():
    print("Running ruff checks...")
    try:
        output = subprocess.check_output("ruff check imlresearch/src", shell=True)
    except subprocess.CalledProcessError as e:
        msg = "Ruff checks failed with the following output:\n"
        msg += e.output.decode("utf-8")
        raise BuildFailed(msg)
    print("All ruff checks passed!")


def delete_old_build_artifacts():
    for dist_dir in DIST_DIRS:
        dist_dir = os.path.join(BUILD_DIR, dist_dir)
        if os.path.exists(dist_dir):
            shutil.rmtree(dist_dir)
    if os.path.exists(BUILD_DIR):
        shutil.rmtree(BUILD_DIR)


def refactor_build_dir():
    for item in os.listdir(f"{BUILD_DIR}/imlresearch/api"):
        shutil.move(
            os.path.join(f"{BUILD_DIR}/imlresearch/api", item),
            f"{BUILD_DIR}/imlresearch",
        )
    os.rmdir(f"{BUILD_DIR}/imlresearch/api")


def remove_tests_from_codebase():
    codebase_dir = f"{BUILD_DIR}/imlresearch"
    test_dirnames = ["tests", "testing"]
    test_dirs = []
    for root, dirs, _ in os.walk(codebase_dir):
        for test_dirname in test_dirnames:
            if test_dirname in dirs:
                test_dir = os.path.join(root, test_dirname)
                test_dirs.append(test_dir)
    for dir_ in test_dirs:
        shutil.rmtree(dir_)


def setup_build_dir(exclude_tests=True):
    delete_old_build_artifacts()

    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
    shutil.copytree("imlresearch", f"{BUILD_DIR}/imlresearch")
    required_files = ["pyproject.toml", "README.md", "LICENSE"]
    for file in required_files:
        shutil.copy(file, BUILD_DIR)

    refactor_build_dir()

    if exclude_tests:
        remove_tests_from_codebase()


@contextlib.contextmanager
def set_temporary_cwd(path):
    old_cwd = os.getcwd()
    os.chdir(path)
    site_packages_path = os.path.join(
        ROOT_DIR, "venv/lib64/python3.10/site-packages"
    )
    pth_file = os.path.join(site_packages_path, "ImageMLResearch.pth")
    with open(pth_file, "r", encoding="utf-8") as f:
        previous_content = f.read()
    try:
        with open(pth_file, "w", encoding="utf-8") as f:
            f.write(path)
        yield
    finally:
        os.chdir(old_cwd)
        with open(pth_file, "w", encoding="utf-8") as f:
            f.write(previous_content)


def exclude_tests_query():
    exclude_tests = input(
        "Do you want to exclude tests from the build? (y/n): "
    )
    return exclude_tests.lower() in ["y", "yes"]


def build_package():
    run_code_style_checks()
    run_unit_tests()
    setup_build_dir(exclude_tests=exclude_tests_query())
    with set_temporary_cwd(BUILD_DIR):
        os.system(f"{sys.executable} -m build")
    print("\n", "*" * 50)
    print(f"Build package is available at: {BUILD_DIR}")


if __name__ == "__main__":
    build_package()
