import json


def copy_json_exclude_entries(source_file, dest_file, exclude_keys):
    """
    Copies data from a source JSON file to a destination JSON file, excluding
    certain entries.

    Parameters
    ----------
    source_file : str
        Path to the source JSON file.
    dest_file : str
        Path to the destination JSON file.
    exclude_keys : list
        A list of keys to exclude from copying.

    Notes
    -----
    The function will open the source JSON file, remove the specified keys from
    the data, and then save the updated data into the destination JSON file.
    """
    with open(source_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    for key in exclude_keys:
        data.pop(key, None)

    with open(dest_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
