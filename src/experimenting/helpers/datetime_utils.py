from datetime import datetime


def get_datetime():
    """
    Returns the current date and time formatted as a beautiful string.

    Returns:
        - str: The current date and time formatted as 'YYYY-MM-DD HH:MM:SS:MS'.
    """
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S.%f")
    formatted_datetime = formatted_datetime[:-3]
    return formatted_datetime

def get_duration(start_time):
    """
    Returns the duration between the start time and the current time.

    Args:
        - start_time (str): The start time of the experiment.

    Returns:
        - str: The duration between the start time and the current time.
    """
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
    end_time = datetime.now()
    duration = end_time - start_time
    duration = str(duration)[:-3]
    if duration.startswith("0:00:"): # Zero hours and minutes
        duration = duration.split(":")[-1]  # Keep seconds
        duration += " s"
    elif not duration.startswith("0:"): # Non-zero hours
        duration = duration.split(".")[0] # Remove milliseconds
    return duration
