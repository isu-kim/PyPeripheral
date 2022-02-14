"""
@project : PyPeripheralDemos
@author : Gooday2die
@date : 2022-02-13
@file : GUI.py
"""
import pickle
import tkinter
from tkinter.font import BOLD

from PyPeripheral import All

import RainbowAll
import ScreenReactive
import StaticColor

import asyncio


class ui:
    def __init__(self):
        self.master = tkinter.Tk()
        self.master.title("PyPeripheral Demo GUI")
        self.master.geometry("450x250")

        self.cur_mode_text = tkinter.StringVar()
        self.cur_mode = None

        self.button1 = None
        self.button2 = None
        self.button3 = None

        self.r_val = None
        self.g_val = None
        self.b_val = None

        self.demo_thread = None

        self.sdk_object = All.SDK()
        self.sdk_object.connect()

    def start(self):
        self.set_buttons()
        self.set_labels()
        self.set_rgb_inputs()
        self.master.mainloop()

    def set_buttons(self):
        self.button1 = tkinter.Button(self.master, text="Screen Reactive", command=self.screen_reactive)
        self.button1.place(x=10, y=30, width=200, height=50)

        self.button2 = tkinter.Button(self.master, text="Rainbow All", command=self.rainbow_all)
        self.button2.place(x=10, y=90, width=200, height=50)

        self.button3 = tkinter.Button(self.master, text="Static Color", command=self.static)
        self.button3.place(x=10, y=150, width=200, height=50)

    def set_labels(self):
        tkinter.Label(self.master, text="R").place(x=10, y=210)
        tkinter.Label(self.master, text="G").place(x=55, y=210)
        tkinter.Label(self.master, text="B").place(x=105, y=210)

        tkinter.Label(self.master, text="Current Mode : ", font=('arial', 9, BOLD)).place(x=10, y=5)
        self.cur_mode = tkinter.Label(self.master, textvariable=self.cur_mode_text)
        self.cur_mode.place(x=100, y=5)

    def set_rgb_inputs(self):
        self.r_val = tkinter.Entry(self.master)
        self.g_val = tkinter.Entry(self.master)
        self.b_val = tkinter.Entry(self.master)

        self.r_val.place(x=25, y=210, width=30)
        self.g_val.place(x=75, y=210, width=30)
        self.b_val.place(x=125, y=210, width=30)

    def screen_reactive(self):
        try:
            self.demo_thread.terminate()
        except AttributeError:
            pass
        self.cur_mode_text.set("Screen Reactive")
        self.demo_thread = asyncio.run(ScreenReactive.screen_reactive(self.sdk_object))

    def rainbow_all(self):
        self.cur_mode_text.set("Rainbow All")
        try:
            self.demo_thread.terminate()
        except AttributeError:
            pass
        self.demo_thread = asyncio.run(RainbowAll.rainbow_all(10, self.sdk_object))

    def static(self):
        self.cur_mode_text.set("Static Color")


if __name__ == "__main__":
    u = ui()
    u.start()
