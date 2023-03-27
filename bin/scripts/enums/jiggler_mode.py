from enum import Enum

class JigglerMode(Enum):
    __order__ = "RANDOM_LINE RANDOM_POINT PATTERN HUMAN"
    RANDOM_LINE = "1"
    RANDOM_POINT = "2"
    PATTERN = "3"
    HUMAN = "4"


