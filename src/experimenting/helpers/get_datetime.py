from datetime import datetime


def get_datetime():
    """
    Returns the current date and time formatted as a beautiful string.

    Returns:
        - str: The current date and time formatted as 'YYYY-MM-DD HH:MM:SS'.
    """
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime
