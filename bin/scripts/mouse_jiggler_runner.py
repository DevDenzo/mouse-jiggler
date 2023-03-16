import keyboard
from scripts.modes.random_mode import RandomMode
from scripts.enums.jiggler_mode import JigglerMode
from scripts.enums.jiggler_status import JigglerStatus

class MouseJigglerRunner():
    def __init__(self, settings):
        self.settings = settings
        self.status = JigglerStatus.SELECTING_MODE
        self.start_application = self.run()

    def run(self):

        while self.status == JigglerStatus.SELECTING_MODE:

            #Start Random Mode
            if keyboard.read_key() == JigglerMode.RANDOM.value:
                print("Random")
                random_mode = RandomMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), False, JigglerMode.RANDOM)
                random_mode.run()
                self.status = JigglerStatus.RUNNING

            #Start Natural Mode
            elif keyboard.read_key() == JigglerMode.NATURAL.value:
                print("Natural")
                self.status = JigglerStatus.RUNNING

            #Start Pattern Mode
            elif keyboard.read_key() == JigglerMode.PATTERN.value:
                print("Pattern")
                self.status = JigglerStatus.RUNNING

        while self.status == JigglerStatus.RUNNING:
            print("Entered Running Phase")
            if keyboard.read_key() == "q" or keyboard.read_key() == "Q":
                self.status = JigglerStatus.STOPPED
        
        print("Quit Application")
