import pyfiglet

from scripts.enums.jiggler_mode import JigglerMode

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
        return f'{self.banner}\n\n{self.generate_list_of_modes()}'

    def generate_list_of_modes(self):

        menu_options = "Select Mode: \n"
        for mode in JigglerMode:
            mode_name = mode._name_.replace('_', ' ').title()
            menu_options = menu_options + f"[{mode.value}] Press & Hold {mode.value} For {mode_name} Mode \n"
        menu_options = menu_options + "\n"

        return menu_options
            


menu = MouseJigglerMenu()
menu.generate_list_of_modes()