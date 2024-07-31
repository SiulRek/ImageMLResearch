from enum import Enum


class Category(Enum):
    """ Enum class for PCB defect categories. """

    MISSING_HOLE = 0
    MOUSE_BITE = 1
    OPEN_CIRCUIT = 2
    SHORT = 3
    SPUR = 4
    SPURIOUS_COPPER = 5

CATEGORY_NAMES = [
    "missing_hole",
    "mouse_bite",
    "open_circuit",
    "short",
    "spur",
    "spurious_copper",
]
