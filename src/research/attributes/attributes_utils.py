def is_public_property(attr_name, source_instance):
    """
    Checks if an attribute is a public property of a class instance.

    Args:
        - attr_name (str): The attribute name to check.
        - source_instance: The instance to check the attribute in.

    """
    cls = source_instance.__class__
    attr = getattr(cls, attr_name, None)
    return isinstance(attr, property) and not attr_name.startswith("_")


def copy_public_properties(source_instance, target_instance):
    """
    Copies the public properties from one instance into another class instance.
    Retrieves all public properties from source_instance and sets them as
    attributes in the target_instance.

    Args:
        - source_instance: The instance from which properties are copied.
        - target_instance: The class instance to insert attributes into.
    """

    for attr_name in dir(source_instance):
        if is_public_property(attr_name, source_instance):
            source_value = getattr(source_instance, attr_name)
            try:
                setattr(target_instance, attr_name, source_value)
            # If the property is read-only, try to access the private attribute
            except AttributeError:
                attr_name = "_" + attr_name
                if hasattr(source_instance, attr_name):
                    setattr(
                        target_instance,
                        attr_name,
                        source_value,
                    )
                else:
                    msg = f"Could neither set property {attr_name} nor access"
                    msg += "its private attribute"
                    raise AttributeError(msg)
