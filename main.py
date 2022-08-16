import pytesseract
import numpy as np
from PIL import ImageGrab
import pyautogui
import matplotlib.pyplot as plt
import cv2 as cv2
import matplotlib.image as mpimg

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def proccesImg(img):
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    txt = pytesseract.image_to_string(img).split("\n")
    del txt[-1]
    print(txt)
    cv2.imshow("Result", img)
    cv2.waitKey(1)
    return txt


x = 350
y = 290
offx = 240
offy = 105

image = ImageGrab.grab(bbox=(x, y, x + offx, y + offy))
i = 2
while (i>=0):
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