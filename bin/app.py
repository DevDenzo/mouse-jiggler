from scripts.mouse_jiggler_menu import MouseJigglerMenu
from scripts.mouse_jiggler_runner import MouseJigglerRunner
from scripts.settings.settings import MouseJigglerSettings

__author__ = "Deniz Yukselir"
__version__ = "0.0.1"
__license__ = "Devite"

def main():
    mouseSettings = MouseJigglerSettings()
    mouseMenu = MouseJigglerMenu()
    mousejiggler = MouseJigglerRunner(mouseMenu, mouseSettings)

if __name__ == "__main__":
    main()