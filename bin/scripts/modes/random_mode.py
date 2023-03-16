from pynput.mouse import Button, Controller
import time

class RandomMode():

    def __init__(self, screen_size_list, os, move_delay, status):
        self.screen_size_list = screen_size_list
        self.os = os
        self.move_delay = move_delay
        self.status = status

        self.mouse = Controller()
        # self.button = Button.left

    def run(self):
        random_coordinates = [(1000,1000)]

        for cord in random_coordinates:
            self.mouse.position = cord
            # self.mouse.click(self.button)

            # Insert Delay Here
            if type(self.move_delay) == float:
                time.sleep(self.move_delay)