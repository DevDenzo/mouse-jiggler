from screeninfo import get_monitors
import platform

class MouseJigglerSettings():

    def __init__(self):
        self.os = self.getOperatingSystem()
        self.screen_size_list = self.getScreenSize()

    def getOperatingSystem(self):
        self.os = platform.system()
        return self.os

    def getScreenSize(self):
        self.screen_size_list = []
        for monitor in get_monitors():
            monitor_height = monitor.height
            monitor_width = monitor.width
            self.screen_size_list.append([monitor_height, monitor_width])

        return self.screen_size_list