from datetime import datetime


def get_datetime():
    """
    Returns the current date and time formatted as a beautiful string.

    Returns:
        - str: The current date and time formatted as 'YYYY-MM-DD HH:MM:SS:MS'.
    """
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S:%f")
    formatted_datetime = formatted_datetime[:-3]
    return formatted_datetime
