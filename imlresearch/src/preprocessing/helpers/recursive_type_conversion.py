def recursive_type_conversion(source_value, target_datatype_template):
    """
    Converts the data type of a given value to match that of a template value,
    doing so recursively for complex data structures.

    This function aims to transform the data type of `source_value` so that it
    matches the data type of `target_datatype_template`. The conversion is
    performed recursively, meaning that if `source_value` is a collection
    (e.g., list, tuple, dictionary), each item within the collection will also
    be converted to match the corresponding item in the template.

    Parameters
    ----------
    source_value : object
        The value whose data type is to be converted. It can be of any type:
        primitive data types, list, tuple, or dict.
    target_datatype_template : object
        An instance of the desired data type that serves as a template for
        conversion. It should be of the same structure as `source_value` if it
        is a collection. If it is a dictionary, `target_datatype_template`
        shall have all keys of `source_value`, the other way around is not
        required.

    Returns
    -------
    object
        The `source_value` converted to the data type structure of
        `target_datatype_template`.
    """
    target_datatype = type(target_datatype_template)

    if target_datatype_template in [int, float, str, bool]:
        try:
            return target_datatype_template(source_value)
        except ValueError as ex:
            msg = (
                f"Value '{source_value}' cannot be converted to "
                f"{target_datatype_template}."
            )
            raise TypeError(msg) from ex

    elif target_datatype is list:
        if isinstance(source_value, tuple):
            source_value = list(source_value)
        elif not isinstance(source_value, list):
            msg = (
                f"Value '{source_value}' cannot be converted to "
                f"{target_datatype_template}."
            )
            raise TypeError(msg)
        if len(source_value) != len(target_datatype_template):
            msg = (
                f"Value '{source_value}' cannot be converted to "
                f"{target_datatype_template}."
            )
            raise TypeError(msg)

        return [
            recursive_type_conversion(src, tgt)
            for src, tgt in zip(source_value, target_datatype_template)
        ]

    elif target_datatype is tuple:
        if isinstance(source_value, list):
            source_value = tuple(source_value)
        elif not isinstance(source_value, tuple):
            msg = (
                f"Value '{source_value}' cannot be converted to "
                f"{target_datatype_template}."
            )
            raise TypeError(msg)
        if len(source_value) != len(target_datatype_template):
            msg = (
                f"Value '{source_value}' cannot be converted to "
                f"{target_datatype_template}."
            )
            raise TypeError(msg)

        return tuple(
            recursive_type_conversion(src, tgt)
            for src, tgt in zip(source_value, target_datatype_template)
        )

    elif target_datatype is dict:
        if isinstance(source_value, dict):
            return {
                key: recursive_type_conversion(src, tgt)
                for key, tgt in target_datatype_template.items()
                if (src := source_value.get(key)) is not None
            }
        return source_value

    return source_value
