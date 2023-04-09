from scripts.mouse_jiggler_menu import MouseJigglerMenu
from scripts.mouse_jiggler_runner import MouseJigglerRunner
from scripts.settings.settings import MouseJigglerSettings

__author__ = "Deniz Yukselir - @DevDenzo - dyukselir@hotmail.co.uk"
__version__ = "1.0.1"
__license__ = "Please request permission from Deniz Yukselir - @DevDenzo on Twitter"

def main():
    mouseSettings = MouseJigglerSettings()
    mouseMenu = MouseJigglerMenu()
    mousejiggler = MouseJigglerRunner(mouseMenu, mouseSettings)

if __name__ == "__main__":
    main()