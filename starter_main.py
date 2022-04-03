from pysnake import main_menu, win
import os
import sys
from platform import system

if __name__ == "__main__":
    current_os = system()
    choosen_os = ['Linux', 'Mac', 'Ubuntu', 'Windows', 'Java']

    for i in choosen_os:
        if i in choosen_os:
            main_menu(win)
        else:
            pass