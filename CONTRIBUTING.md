# Contributing to ImageMLResearch

Thanks for your interest in contributing! Here's how to get started.

## Reporting Issues

Open an issue on [GitHub](https://github.com/SiulRek/ImageMLResearch/issues) with:
- A clear description of the bug or feature request
- Steps to reproduce (for bugs)
- Python version and OS

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment with Python 3.10–3.12:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install in editable mode:
   ```bash
   pip install -e .
   ```

## Running Tests

```python
from imlresearch.api.tests import run_all_tests
run_all_tests()
```

All tests must pass before submitting a pull request.

## Pull Requests

1. Create a feature branch from `main`
2. Keep changes focused — one feature or fix per PR
3. Follow the existing code style (enforced by ruff and pylint)
4. Add tests for new functionality
5. Update documentation if needed
6. Open a PR with a clear title and description

## Code Style

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and [black](https://black.readthedocs.io/) for formatting (line length 79).

## Questions

Open an issue or reach out to the maintainer listed in `pyproject.toml`.
