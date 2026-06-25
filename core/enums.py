from enum import Enum


class Side(str, Enum):
    LONG = "LONG"
    SHORT = "SHORT"


class Signal(str, Enum):
    NONE = "NONE"
    LONG = "LONG"
    SHORT = "SHORT"


class ExitReason(str, Enum):
    REVERSE = "REVERSE"
    STOP = "STOP"
    TAKE = "TAKE"
    MANUAL = "MANUAL"