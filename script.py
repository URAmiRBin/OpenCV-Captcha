import cv2
import numpy as np
import sys
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# SETTINGS
KERNEL_SIZE = (5, 5)
BLUR_INTENSITY = 0
MIN_THRESH = 100
MAX_THRESH = 200

def image_read(image_address):
    image = cv2.imread(image_address)
    return image


def image_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def image_blur(image):
    blurred_image = cv2.GaussianBlur(image, KERNEL_SIZE, BLUR_INTENSITY)
    return blurred_image


def image_canny(image):
    edged_image = cv2.Canny(image, MIN_THRESH, MAX_THRESH)
    return edged_image




address = 'TestCases/' + sys.argv[1] + '.jpg'
original = image_read(address)
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
text = pytesseract.image_to_string(gray, config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
print(text)