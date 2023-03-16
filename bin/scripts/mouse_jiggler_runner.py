import keyboard
from scripts.modes.pattern_mode import PatternMode
from scripts.modes.random_mode import RandomMode
from scripts.enums.jiggler_mode import JigglerMode
from scripts.enums.jiggler_status import JigglerStatus

class MouseJigglerRunner():
    def __init__(self, settings):
        self.settings = settings
        self.status = JigglerStatus.SELECTING_MODE
        self.start_application = self.run()
        self.mode = ""
        self.mode_thread = ""

    def run(self):

        while self.status == JigglerStatus.SELECTING_MODE:

            #Start Random Mode
            if keyboard.read_key() == JigglerMode.RANDOM.value:
                self.mode = "Random"
                self.mode_thread = RandomMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), 10, JigglerStatus.RUNNING)
                self.mode_thread.start()
                self.status = JigglerStatus.RUNNING

            #Start Natural Mode
            elif keyboard.read_key() == JigglerMode.NATURAL.value:
                print("Natural")
                self.status = JigglerStatus.RUNNING

            #Start Pattern Mode
            elif keyboard.read_key() == JigglerMode.PATTERN.value:
                self.mode = "Pattern"
                self.mode_thread = PatternMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), 10, JigglerStatus.RUNNING)
                self.mode_thread.start()
                self.status = JigglerStatus.RUNNING

        while self.status == JigglerStatus.RUNNING:
            print("Began " + self.mode + " mode")

            if keyboard.read_key() == "q" or keyboard.read_key() == "Q":
                self.mode_thread.status = JigglerStatus.STOPPED
                self.status = JigglerStatus.STOPPED
        
        print("Quit Application")
