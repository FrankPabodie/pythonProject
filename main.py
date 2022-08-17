import sys

import keyboard
import pynput
import pytesseract
import numpy as np
from PIL import ImageGrab
import pyautogui
import cv2 as cv2
from pynput import keyboard
from pynput.keyboard import Key,Controller

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

global stop
def on_press(key):
        if("k" == key.char):
            global stop
            stop = True
            print("stop")
            exit()
        print('alphanumeric key {0} pressed'.format(
            key.char))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False



def proccesImg(img):
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    txt = pytesseract.image_to_string(img).split("\n")
    del txt[-1]
    print(txt)
    cv2.imshow("Result", img)
    return txt


def startsearch():
    x = 350
    y = 290
    offx = 240
    offy = 105
    global stop
    stop = False
    image = ImageGrab.grab(bbox=(x, y, x + offx, y + offy))
    i = 2

    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

    while i >= 0:
        if stop:
            break

        if any("Blood Plague" in n for n in proccesImg(image)):
            print("swap")
            i = i - 1
            x = x + 613
            image = ImageGrab.grab(bbox=(x, y, x + offx, y + offy))
        elif any("Just Keeps Going" in n for n in proccesImg(image)):
            print("swap")
            i = i - 1
            x = x + 613
            image = ImageGrab.grab(bbox=(x, y, x + offx, y + offy))
        else:
            pyautogui.click(x, y + 500)
            image = ImageGrab.grab(bbox=(x, y, x + offx, y + offy))


startsearch()