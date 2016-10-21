#!/usr/bin/python3
import sys, time, pyautogui, gi, random
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
window = Gdk.get_default_root_window()

def Pixel(X, Y):
    # Source X coordinate within window
    # Source Y coordinate within window
    Pixbuf = Gdk.pixbuf_get_from_window(window, X, Y, 1, 1)
    return Pixbuf.get_pixels()

def LumberJack():
    scoreX = int(sys.argv[1])
    Score = 0
    time.sleep(2)
    pyautogui.press(' ')

    while Score < scoreX:
        Left  = Pixel(291, 317)
        Right = Pixel(411, 317)
        if Right[0] < Left[0]:
            # pyautogui.moveTo(290, 317)
            pyautogui.press('left', 2, random.choice([0.09, 0.10]))
        else:
            # pyautogui.moveTo(411, 317)
            pyautogui.press('right', 2, random.choice([0.09, 0.10]))
        Score += 2

#Run
LumberJack()
