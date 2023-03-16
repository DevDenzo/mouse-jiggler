from threading import Thread
from pynput.mouse import Button, Controller
import time
from scripts.enums.jiggler_status import JigglerStatus
from scripts.helpers.coordinate_generator import CoordinateGenerator

class RandomMode(Thread):

    def __init__(self, screen_size_list, os, move_delay, status):
        Thread.__init__(self)
        self.screen_size_list = screen_size_list
        self.os = os
        self.move_delay = move_delay
        self.status = status
        self.mouse = Controller()

    def run(self):
        random_coordinates = CoordinateGenerator().generate_random_coordinates_by_screensize(self.screen_size_list, 10000)

        while self.status == JigglerStatus.RUNNING:
            for cordinate in random_coordinates:
                self.mouse.position = cordinate

                # Insert Delay Here
                if type(self.move_delay) == float:
                    # If delay provided, check 4 times per second if status is still RUNNING or not
                    for n in range(0, self.move_delay*4):
                        if self.status == JigglerStatus.RUNNING:
                            time.sleep(0.25)
                        else:
                            break