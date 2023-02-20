from scripts.mouse_jiggler import MouseJiggler

__author__ = "Deniz Yukselir"
__version__ = "0.0.1"
__license__ = "Devite"


# #Code to control keyboard
# from pynput.keyboard import Key, Controller as KeyboardController
# from pynput.mouse import Button, Controller as MouseController
# keyboard = KeyboardController()
# mouse = MouseController()

def main():
    mousejiggler = MouseJiggler
    mousejiggler.run()

if __name__ == "__main__":
    main()