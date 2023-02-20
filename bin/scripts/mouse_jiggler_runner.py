import keyboard
from scripts.enums.jiggler_mode import JigglerMode

class MouseJigglerRunner:
    def __init__(self, mode, status):
        self.mode = mode
        self.status = status

    def run():
        MOUSE_JIGGLER_ACTIVATED = True

        while MOUSE_JIGGLER_ACTIVATED:

            if keyboard.read_key() == JigglerMode.RANDOM.value:
                print("Random")
                MOUSE_JIGGLER_ACTIVATED = False

            elif keyboard.read_key() == JigglerMode.NATURAL.value:
                print("Natural")
                MOUSE_JIGGLER_ACTIVATED = False

            elif keyboard.read_key() == JigglerMode.PATTERN.value:
                print("Pattern")
                MOUSE_JIGGLER_ACTIVATED = False
