import cv2
import numpy as np
import sys
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# SETTINGS
BLUR_INTENSITY = 2

def image_read(image_address):
    image = cv2.imread(image_address)
    return image


def image_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


def image_blur(image):
    blurred_image = cv2.medianBlur(image, BLUR_INTENSITY)
    return blurred_image

def solve_captcha(address):
    original = image_read(address)
    gray = image_gray(original)
    text = pytesseract.image_to_string(gray)
    print(text)

if __name__ == "__main__":
    solve_captcha(sys.argv[1])