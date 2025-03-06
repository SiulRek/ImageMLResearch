import random
import re


def is_sequential(lst):
    """
    Check if the list elements start from 0 and increment by 1.

    Parameters
    ----------
    lst : list
        The list of elements to check.

    Returns
    -------
    bool
        True if the list is sequential starting from 0, otherwise False.
    """
    return all(i == val for i, val in enumerate(lst))


def matches_pattern(key, pattern):
    """
    Check if a key matches a given regular expression pattern.

    Parameters
    ----------
    key : str
        The key to check.
    pattern : Pattern
        The regular expression pattern to match the key against.

    Returns
    -------
    bool
        True if the key matches the pattern, otherwise False.
    """
    return pattern.match(key) is not None


def extract_indices(input_dict, pattern):
    """
    Extract indices from keys in the input dictionary based on a pattern.

    Parameters
    ----------
    input_dict : dict
        The dictionary whose keys are to be checked.
    pattern : Pattern
        The regular expression pattern to match the keys against.

    Returns
    -------
    list
        A list of indices extracted from the keys that match the pattern.
    """
    return [
        int(pattern.match(key).group(2))
        for key in input_dict
        if matches_pattern(key, pattern)
    ]


def filter_keys_by_pattern(input_dict, pattern):
    """
    Filter keys in the input dictionary that match a given pattern.

    Parameters
    ----------
    input_dict : dict
        The dictionary whose keys are to be filtered.
    pattern : Pattern
        The regular expression pattern to match the keys against.

    Returns
    -------
    list
        A list of keys from the dictionary that match the pattern.
    """
    return [key for key in input_dict if matches_pattern(key, pattern)]


def remove_second_group(s, pattern):
    """
    Remove the content of the second group from the matched pattern in
    the given string. If the pattern does not match, return the input string.

    Parameters
    ----------
    s : str
        The input string to process.
    pattern : Pattern
        The compiled regular expression pattern with at least two groups.

    Returns
    -------
    str
        Modified string with the second group content removed, or the original
        string if no match is found.
    """
    match = pattern.search(s)
    if not match:
        return s

    def replace_with_first_and_third_group(match):
        return match.group(1) + match.group(3)

    return pattern.sub(replace_with_first_and_third_group, s)


def randomly_select_sequential_keys(input_dict, separator="__"):
    """
    Randomly selects keys from a dictionary that follow a specific sequential
    pattern. The pattern is defined by a separator followed by 'I' and a number,
    optionally followed by 'F' and another number.

    Parameters
    ----------
    input_dict : dict
        The input dictionary containing keys to be selected.
    separator : str, optional
        The separator used in the key pattern, defaulting to '__'.

    Returns
    -------
    dict
        A new dictionary containing randomly selected keys and their
        corresponding values.
    """
    end_pattern = rf"($|{re.escape(separator)}\S+)"
    ind_key_pattern = re.compile(rf"(.*?){re.escape(separator)}I(\d+)(.*?)")
    ind_key_pattern_all = re.compile(
        rf"(.*?)({re.escape(separator)}I\d+)(.*?)"
    )
    ind_key_pattern_end = re.compile(
        rf"(.*?){re.escape(separator)}I(\d+){end_pattern}"
    )
    freq_key_pattern = re.compile(
        rf"(.*?){re.escape(separator)}I\d+F(\d+){end_pattern}"
    )
    freq_key_pattern_all = re.compile(
        rf"(.*?)({re.escape(separator)}I\d+F\d+){end_pattern}"
    )

    match_flags = [
        matches_pattern(key, ind_key_pattern_end)
        or matches_pattern(key, freq_key_pattern)
        for key in input_dict
    ]

    if not any(match_flags):
        return input_dict

    if not all(match_flags):
        raise KeyError("Some keys do not follow a sequential pattern.")

    indices = extract_indices(input_dict, ind_key_pattern)
    unique_sorted_indices = sorted(set(indices))

    if not is_sequential(unique_sorted_indices):
        raise KeyError("Indices of the keys are not sequential.")

    output_dict = {}
    for index in unique_sorted_indices:
        compiled_pattern = re.compile(
            rf".*{re.escape(separator)}I{index}(F\d+|{end_pattern})"
        )
        temp_keys = filter_keys_by_pattern(input_dict, compiled_pattern)
        keys = []
        for key in temp_keys:
            if match := freq_key_pattern.match(key):
                freq = int(match.group(2))
                keys.extend([key] * freq)
            else:
                keys.append(key)

        selected_key = random.choice(keys)
        new_key = remove_second_group(selected_key, freq_key_pattern_all)
        new_key = remove_second_group(new_key, ind_key_pattern_all)

        if new_key in output_dict:
            raise KeyError("The selected key already exists in the output.")

        output_dict[new_key] = input_dict[selected_key]

    return output_dict
