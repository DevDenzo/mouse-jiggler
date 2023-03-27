import keyboard
from scripts.modes.pattern_mode import PatternMode
from scripts.modes.random_line_mode import RandomLineMode
from scripts.modes.random_point_mode import RandomPointMode
from scripts.enums.jiggler_mode import JigglerMode
from scripts.enums.jiggler_status import JigglerStatus

class MouseJigglerRunner():
    def __init__(self, menu, settings):
        self.menu = menu
        self.settings = settings
        self.status = JigglerStatus.SELECTING_MODE
        self.start_application = self.run()
        self.mode = ""
        self.mode_thread = ""

    def run(self):
        while self.status != JigglerStatus.STOPPED:
            self.application_start()

        print("Shutting Down...")

    def application_start(self):

        print(self.menu.select_mode_menu())

        while self.status == JigglerStatus.SELECTING_MODE:

            #Start Random Line Mode
            if keyboard.read_key() == JigglerMode.RANDOM_LINE.value:
                self.mode = "Random Line"
                self.mode_thread = RandomLineMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), 100, JigglerStatus.RUNNING)
                self.mode_thread.start()
                self.status = JigglerStatus.RUNNING

            #Start Random Point Mode
            if keyboard.read_key() == JigglerMode.RANDOM_POINT.value:
                self.mode = "Random Point"
                self.mode_thread = RandomPointMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), 100, JigglerStatus.RUNNING)
                self.mode_thread.start()
                self.status = JigglerStatus.RUNNING

            #Start Pattern Mode
            elif keyboard.read_key() == JigglerMode.PATTERN.value:
                self.mode = "Pattern"
                self.mode_thread = PatternMode(self.settings.getScreenSize(), self.settings.getOperatingSystem(), 10, JigglerStatus.RUNNING)
                self.mode_thread.start()
                self.status = JigglerStatus.RUNNING

            #Start Human Mode
            elif keyboard.read_key() == JigglerMode.HUMAN.value:
                print("Human")
                self.status = JigglerStatus.RUNNING

        while self.status == JigglerStatus.RUNNING:
            print("Began " + self.mode + " mode")
            print("\n")
            print("Hold S to stop and return to menu\n")
            print("Hold Q to stop and quit the application\n")

            if keyboard.read_key() == "s" or keyboard.read_key() == "S":
                self.mode_thread.status = JigglerStatus.SELECTING_MODE
                self.status = JigglerStatus.SELECTING_MODE
            
            if keyboard.read_key() == "q" or keyboard.read_key() == "Q":
                self.mode_thread.status = JigglerStatus.STOPPED
                self.status = JigglerStatus.STOPPED

