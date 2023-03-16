import pyfiglet

class MouseJigglerMenu():

    def __init__(self):
        self.banner = self.mouse_ascii()

    def menu_header(self):
        ascii_banner = pyfiglet.figlet_format("Mouse Jiggler")
        return ascii_banner

    def mouse_ascii(self):

        return """
         __  __                            _ _             _                     ,.
        |  \/  | ___  _   _ ___  ___      | (_) __ _  __ _| | ___ _ __       __.'_
        | |\/| |/ _ \| | | / __|/ _ \  _  | | |/ _` |/ _` | |/ _ \ '__|     |__|__|
        | |  | | (_) | |_| \__ \  __/ | |_| | | (_| | (_| | |  __/ |        |     |   
        |_|  |_|\___/ \__,_|___/\___|  \___/|_|\__, |\__, |_|\___|_|        |-___-|
                                               |___/ |___/                  '.___.' 
                                                                By Devite"""

    def select_mode_menu(self):
        return f'{self.banner}\n\n Select Mode: \n [1] Press & Hold 1 For Random Mode \n [2] Press & Hold 2 For Natural Mode \n [3] Press & Hold 3 For Pattern Mode \n\n'


menu = MouseJigglerMenu()
menu.select_mode_menu()