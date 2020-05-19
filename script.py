import cv2
import numpy as np
import sys


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


# SETTINGS
KERNEL_SIZE = (5, 5)
BLUR_INTENSITY = 0
MIN_THRESH = 100
MAX_THRESH = 200



address = 'TestCases/' + sys.argv[1] + '.jpg'
original = image_read(address)
blurred = cv2.medianBlur(original, 11)
edged = image_canny(blurred)
cv2.imshow('Edged Image', edged)
cv2.waitKey(0)