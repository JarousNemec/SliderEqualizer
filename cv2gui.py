#!/usr/bin/python
import time

import cv2
import numpy as np

img = np.zeros(shape=[100, 800, 3], dtype=np.uint8)
windowName = 'Slider Equalizer'

def on_alpha_change(val):
    print("Alpha: " + str(val))


def on_b_change(val):
    print("B: " + str(val))


def on_diff_change(val):
    print("Diff: " + str(val))


def make_window():
    cv2.imshow(windowName, img)
    cv2.createTrackbar('Alpha', windowName, 0, 100, on_alpha_change)
    cv2.createTrackbar('B', windowName, 0, 10, on_b_change)
    cv2.createTrackbar('Diff', windowName, 0, 10, on_diff_change)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    make_window()
