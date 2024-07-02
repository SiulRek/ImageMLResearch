def copy_public_properties(source_instance, target_instance):
    """
    Copies the public properties from one instance into another class instance.
    Retrieves all public properties from source_instance and sets them as
    attributes in the target_instance.

    Args:
        - source_instance: The instance from which properties are copied.
        - target_instance: The class instance to insert attributes into.
    """

    def is_public_property(attr_name, source_instance):
        cls = source_instance.__class__
        attr = getattr(cls, attr_name, None)
        return isinstance(attr, property) and not attr_name.startswith("_")

    for attr_name in dir(source_instance):
        if is_public_property(attr_name, source_instance):
            try:
                setattr(target_instance, attr_name, getattr(source_instance, attr_name))
            # If the property is read-only, try to access the private attribute
            except AttributeError:
                attr_name = "_" + attr_name
                if hasattr(source_instance, attr_name):
                    setattr(
                        target_instance,
                        attr_name,
                        getattr(source_instance, attr_name[1:]),
                    )
                else:
                    msg = f"Could neither set property {attr_name} nor access"
                    msg += "its private attribute"
                    raise AttributeError(msg)