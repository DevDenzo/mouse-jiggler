from threading import Thread
from pynput.mouse import Button, Controller
import time
from scripts.enums.jiggler_status import JigglerStatus
from scripts.helpers.coordinate_generator import CoordinateGenerator

class RandomMode(Thread):

    def __init__(self, screen_size_list, os, random_type, move_delay, status):
        Thread.__init__(self)
        self.screen_size_list = screen_size_list
        self.os = os
        self.move_delay = move_delay
        self.status = status
        self.mouse = Controller()
        self.random_type = random_type

    def run(self):
        if self.random_type == "LINE":
            random_generator = CoordinateGenerator()
            random_points = random_generator.generate_random_coordinates_by_screensize(self.screen_size_list, 50)
            random_coordinates = []

            number_of_lines = 50

            for n in range(1, number_of_lines):
                if n == number_of_lines:
                    random_coordinates = random_coordinates + random_generator.generate_coordinates_on_line(random_points[n], random_points[0], 500000)
                
                random_coordinates = random_coordinates + random_generator.generate_coordinates_on_line(random_points[n-1], random_points[n], 500000)
        elif self.random_type == "POINTS":
            random_coordinates = random_generator.generate_random_coordinates_by_screensize(self.screen_size_list, 300)

        while self.status == JigglerStatus.RUNNING:
            for cordinate in random_coordinates:
                self.mouse.position = cordinate

                # Insert Delay Here
                if type(self.move_delay) == float:
                    # If delay provided, check 4 times per second if status is still RUNNING or not
                    for n in range(0, self.move_delay*4):
                        if self.status == JigglerStatus.RUNNING:
                            time.sleep(0.01)
                        else:
                            break

                if self.status != JigglerStatus.RUNNING:
                    break