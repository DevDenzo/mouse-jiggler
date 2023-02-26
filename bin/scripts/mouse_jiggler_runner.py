import keyboard
from scripts.enums.jiggler_mode import JigglerMode
from scripts.enums.jiggler_status import JigglerStatus
from scripts.modes import natural_mode, pattern_mode, random_mode

class MouseJigglerRunner():
    def __init__(self):
        self.status = JigglerStatus.SELECTING_MODE
        self.start_application = self.run()

    def run(self):

        while self.status == JigglerStatus.SELECTING_MODE:

            #Start Random Mode
            if keyboard.read_key() == JigglerMode.RANDOM.value:
                print("Random")
                self.status = JigglerStatus.RUNNING

            #Start Natural Mode
            elif keyboard.read_key() == JigglerMode.NATURAL.value:
                print("Natural")
                self.status = JigglerStatus.RUNNING

            #Start Pattern Mode
            elif keyboard.read_key() == JigglerMode.PATTERN.value:
                print("Pattern")
                self.status = JigglerStatus.RUNNING
