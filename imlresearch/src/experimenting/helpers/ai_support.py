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

Please analyze the experiment and its results above. Provide an analysis in
markdown with three sections:
```markdown
# 1. Key Insights
# 2. Trends in Results
# 3. Recommendations for Improving Experiment Design and Performance
```
"""


def _get_execution_code(experiment_dir):
    """
    Retrieves the execution code of the experiment.

    Parameters
    ----------
    experiment_dir : str
        The directory containing the experiment.

    Returns
    -------
    str
        The content of the execution script.
    """
    execution_script = os.path.join(experiment_dir, "execution.py")
    if not os.path.exists(execution_script):
        msg = f"Execution script 'execution.py' not found in {experiment_dir}."
        raise FileNotFoundError(msg)
    with open(execution_script, "r", encoding="utf-8") as file:
        execution_code = file.read()
    return execution_code.strip()


def _get_results(output_dir):
    """
    Extracts the summary of the experiment report.

    Parameters
    ----------
    output_dir : str
        The directory containing the experiment results.

    Returns
    -------
    str
        The summary of the experiment report.
    """
    report_file = os.path.join(output_dir, "experiment_report.md")
    if not os.path.exists(report_file):
        msg = f"Report file not found in {output_dir}."
        raise FileNotFoundError(msg)
    with open(report_file, "r", encoding="utf-8") as file:
        results = file.read()
        summary = results.split("Summary")[1].split(PAGE_BREAK)[0]
        summary = re.sub(r"<.*?>", "", summary).strip()  # Remove HTML tags
    return summary


def ask_for_experiment_analysis(experiment_dir):
    """
    Requests an AI-based analysis of an experiment.

    Parameters
    ----------
    experiment_dir : str
        The directory of the experiment to analyze.
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
