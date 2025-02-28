import os
import re

from imlresearch.src.utils import send_chatgpt_prompt

PAGE_BREAK = '<div style="page-break-after: always;">'

prompt = """
# Experiment Execution Code

```python
EXECUTION_CODE
```

# Experiment Results
```markdown
RESULTS
```

# Request for Analysis:

Please analyze the experiment and its results above. Provide an analysis in markdown with three chapters:
```markdown
# 1. Key insights
# 2. Trends in Results
# 3. Recommendations for improving the experiment design and performance.
```
"""


def _get_execution_code(experiment_dir):
    """
    Take the execution code of the experiment.

    Args:
        - experiment_dir (str): The directory of the experiment.

    Returns:
        - str: The execution code of the experiment.
    """
    execution_skript = os.path.join(experiment_dir, "execution.py")
    if not os.path.exists(execution_skript):
        msg += "Execution script named 'execution.py' not found in "
        msg = f"{experiment_dir} "
        raise FileNotFoundError(msg)
    with open(execution_skript, "r", encoding="utf-8") as file:
        execution_code = file.read()
    return execution_code.strip()


def _get_results(output_dir):
    report_dir = os.path.join(output_dir, "experiment_report.md")
    if not os.path.exists(report_dir):
        msg = f"Report file not found in {output_dir}."
        raise FileNotFoundError(msg)
    with open(report_dir, "r", encoding="utf-8") as file:
        results = file.read()
        summary = results.split("Summary")[1].split(PAGE_BREAK)[0]
        # Remove HTML tags from the summary
        summary = re.sub(r"<.*?>", "", summary).strip()
    return summary


def ask_for_experiment_analysis(experiment_dir):
    """
    Ask ChatGPT for an analysis of the given experiment.

    Args:
        - experiment_dir (str): The directory of the experiment to analyze.
    """
    output_dir = os.path.join(experiment_dir, "output")
    prompt_file = os.path.join(experiment_dir, "prompt.txt")
    response_file = os.path.join(output_dir, "analysis.md")

    execution_code = _get_execution_code(experiment_dir)
    results = _get_results(output_dir)

    updated_prompt = prompt.replace("EXECUTION_CODE", execution_code)
    updated_prompt = updated_prompt.replace("RESULTS", results)

    with open(prompt_file, "w", encoding="utf-8") as file:
        file.write(updated_prompt)
    print(f"Prompt written to {prompt_file}")

    response = send_chatgpt_prompt(updated_prompt)
    try:
        response = response.split("```markdown")[1].split("```")[0]
    except IndexError:
        response = response.replace("```", "")
    with open(response_file, "w", encoding="utf-8") as file:
        file.write(response)
    print(f"Analysis written to {response_file}")


if __name__ == "__main__":
    experiment_dir = "Path/to/experiment"
    ask_for_experiment_analysis(experiment_dir)
