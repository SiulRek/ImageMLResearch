from datetime import datetime


def get_datetime():
    """
    Returns the current date and time formatted as a beautiful string.

    Returns:
        - str: The current date and time formatted as 'YYYY-MM-DD
        - HH:MM:SS:MS'.
    """
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_datetime = formatted_datetime[:-3]
    return formatted_datetime


def _prettify_duration(duration):
    """
    Formats the duration string in a more readable format.

    Args:
        - duration (str): The duration string to be formatted.

    Returns:
        - str: The formatted duration string.
    """
    if duration.startswith("0:00:"):  # Zero hours and minutes
        duration = duration.removeprefix("0:00:")
        duration += " s"
    elif not duration.startswith("0:"):  # Non-zero hours
        duration = duration.split(".")[0]  # Remove milliseconds
    if "." in duration:
        after_decimal = duration.split(".")[1]
        if len(after_decimal) > 3:
            duration = duration.split(".")[0] + "." + after_decimal[:3]
    return duration


def get_duration(start_time):
    """
    Returns the duration between the start time and the current time.

    Args:
        - start_time (str): The start time in the format 'YYYY-MM-DD
        - HH:MM:SS:MS'.

    Returns:
        - str: The duration between the start time and the current time.
    """
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
    end_time = datetime.now()
    duration = end_time - start_time
    duration = str(duration)
    return _prettify_duration(duration)


def _normalize_duration(duration):
    """
    Normalize the duration format to be of format 'H:MM:SS'.

    Args:
        - duration (str): The duration string to be normalized.

    Returns:
        - list: The normalized duration as a list of strings.
    """
    length = duration.count(":") + 1
    assert length <= 3, "Invalid duration format"
    if length == 1:
        duration = "0:00:" + duration
    if length == 2:
        duration = "0:" + duration
    return duration


def add_durations(duration1, duration2):
    """
    Adds two durations together.

    Args:
        - duration1 (str): A duration in the format 'H:MM:SS'.
        - duration2 (str): A duration in the format 'H:MM:SS'.

    Returns:
        - str: The sum of the two durations in the format 'H:MM:SS'.
    """

    duration1 = _normalize_duration(duration1)
    duration2 = _normalize_duration(duration2)

    duration1 = [float(x) for x in duration1.split(":")]
    duration2 = [float(x) for x in duration2.split(":")]

    seconds = duration1[-1] + duration2[-1]
    minutes = int(duration1[-2] + duration2[-2])
    hours = int(duration1[-3] + duration2[-3])

    if seconds >= 60:
        seconds -= 60
        minutes += 1
    if minutes >= 60:
        minutes -= 60
        hours += 1
    total_duration = f"{hours}:{minutes}:{seconds}"
    return _prettify_duration(total_duration)
