import enum

class TruckCommand(enum.Enum):
    DO_NOTHING = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    PICK_UP = 5
    TAKE_OFF = 6