#!/usr/bin/python

import tkinter as tk
import _thread
import time
import os


def make_window():
    WIDTH = 800
    HEIGHT = 600
    # initialize window
    window = tk.Tk()
    window.title("Posuvniko Vokno")
    window.geometry("800x600")
    window.maxsize(WIDTH, HEIGHT)
    window.minsize(WIDTH, HEIGHT)

    alphaSlider = alpha_components()

    BSlider = B_components()

    diffSlider = diff_components()

    # start logger
    try:
        _thread.start_new_thread(logger, (alphaSlider, BSlider, diffSlider))
    except:
        print("Error: unable to start thread")

    # run Tkinter event loop
    window.mainloop()


def alpha_components():
    frame = tk.Frame(bg="red")
    # frame.place(x=10, y=10, width=400, height=50)
    frame.grid(row=0, column=0, pady=2)
    alphaLabel = tk.Label(frame, text="ALPHA")
    alphaLabel.pack()
    alphaSlider = tk.Scale(frame, from_=0, to=100, length=600, orient=tk.HORIZONTAL)
    alphaSlider.pack()
    #frame.pack()
    return alphaSlider


def B_components():
    frame = tk.Frame(bg="green")
    # frame.place(x=10, y=70, width=400, height=50)
    frame.grid(row=1, column=0, pady=2)
    BLabel = tk.Label(frame, text="B")
    BLabel.pack()
    BSlider = tk.Scale(frame, from_=0, to=10, length=600, orient=tk.HORIZONTAL)
    BSlider.pack()
    #frame.pack()
    return BSlider


def diff_components():
    frame = tk.Frame(bg="blue")
    # frame.place(x=10, y=130, width=400, height=50)
    frame.grid(row=2, column=0, pady=2)
    diffLabel = tk.Label(frame, text="DIFF")
    diffLabel.pack()
    diffSlider = tk.Scale(frame, from_=0, to=10, length=600, orient=tk.HORIZONTAL)
    diffSlider.pack()
    #frame.pack()

    return diffSlider


def logger(alpha_slider, b_slider, diff_slider):
    while 1:
        time.sleep(0.5)
        print("------------------")
        print("alpha: " + str(alpha_slider.get()))
        print("B: " + str(b_slider.get()))
        print("DIFF: " + str(diff_slider.get()))


if __name__ == '__main__':
    make_window()
