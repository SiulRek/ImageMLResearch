from src.research.attributes.research_attributes import ResearchAttributes


def insert_research_attributes(instance, research_attributes):
    """
    Inserts the attributes from a ResearchAttributes instance into another class
    instance. Retrieves all public properties from research_attributes and sets
    them as attributes in the instance.

    Args:
        - instance: The class instance to insert attributes into.
        - research_attributes (ResearchAttributes): The ResearchAttributes
            instance.
    """

    def is_property(attr_name):
        cls = research_attributes.__class__
        attr = getattr(cls, attr_name)
        return isinstance(attr, property)

    if not isinstance(research_attributes, ResearchAttributes):
        msg = "research_attributes must be an instance of ResearchAttributes"
        msg += f"not {type(research_attributes)}."
        raise ValueError(msg)

    for attr_name in dir(research_attributes):
        attribute = getattr(research_attributes, attr_name)
        if (
            not attr_name.startswith("_")
            and not callable(attribute)
            and is_property(attr_name)
        ):
            setattr(instance, "_" + attr_name, getattr(research_attributes, attr_name))