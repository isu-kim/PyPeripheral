"""
@project : PyPeripheralDemos
@author : Gooday2die
@date : 2022-02-13
@file : GUI.py
"""
import tkinter
from tkinter import DISABLED
from tkinter.font import BOLD

from PyPeripheral import All

import RainbowAll
import ScreenReactive
import StaticColor

import multiprocessing


class ui:
    """
    A class for main ui of this program
    """
    def __init__(self):
        """
        An initializer method for class UI
        """
        self.master = tkinter.Tk()
        self.master.title("PyPeripheral Demo GUI")
        self.master.geometry("450x250")
        self.master.resizable(width=False, height=False)

        self.cur_mode_text = tkinter.StringVar()
        self.cur_mode = None

        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None

        self.r_val = None
        self.g_val = None
        self.b_val = None

        self.connected_devices = None

        self.demo_process = None

        self.sdk_object = All.SDK()
        self.sdk_object.connect()

    def start(self):
        """
        A method for setting all attributes into places and starting the object
        :return: returns None
        """
        self.set_buttons()
        self.set_labels()
        self.set_rgb_inputs()
        self.show_connected_devices()
        self.master.mainloop()

    def set_buttons(self):
        """
        A method that sets all buttons in place
        :return: returns None
        """
        self.button1 = tkinter.Button(self.master, text="Screen Reactive", command=self.screen_reactive)
        self.button1.place(x=10, y=30, width=200, height=50)

        self.button2 = tkinter.Button(self.master, text="Rainbow All", command=self.rainbow_all)
        self.button2.place(x=10, y=90, width=200, height=50)

        self.button3 = tkinter.Button(self.master, text="Static Color", command=self.static)
        self.button3.place(x=10, y=150, width=200, height=50)

        self.button4 = tkinter.Button(self.master, text="EXIT", command=self.exit_program)
        self.button4.place(x=240, y=200, width=200, height=30)

    def exit_program(self):
        """
        A method that exits the program
        :return: returns None, Exits with 0
        """
        self.master.destroy()
        self.demo_process.terminate()
        sdk_object = All.SDK()
        sdk_object.connect()
        sdk_object.disable()
        exit(0)

    def set_labels(self):
        """
        A method that sets labels in the ui section
        :return: returns None
        """
        tkinter.Label(self.master, text="R").place(x=10, y=210)
        tkinter.Label(self.master, text="G").place(x=65, y=210)
        tkinter.Label(self.master, text="B").place(x=120, y=210)

        tkinter.Label(self.master, text="Current Mode : ", font=('arial', 9, BOLD)).place(x=10, y=5)
        tkinter.Label(self.master, text="Connected Devices", font=('arial', 9, BOLD)).place(x=275, y=5)

        self.cur_mode = tkinter.Label(self.master, textvariable=self.cur_mode_text)
        self.cur_mode.place(x=100, y=5)

    def set_rgb_inputs(self):
        """
        A method that sets input fields for rgb values in the ui field
        :return: returns None
        """
        self.r_val = tkinter.Entry(self.master)
        self.g_val = tkinter.Entry(self.master)
        self.b_val = tkinter.Entry(self.master)

        self.r_val.place(x=30, y=210, width=30)
        self.g_val.place(x=85, y=210, width=30)
        self.b_val.place(x=140, y=210, width=30)

    def show_connected_devices(self):
        """
        A method that shows the connected devices in right text area
        :return: returns None
        """
        self.connected_devices = tkinter.Text(self.master)
        self.connected_devices.place(x=240, y=30, width=200, height=150)

        sdk_object = All.SDK()
        sdk_object.connect()
        dev_list = sdk_object.get_all_device_information()
        print(dev_list)
        sdk_object.disable()
        del sdk_object

        connected_device_string = ""
        for sdk in dev_list:
            connected_device_string = connected_device_string + "- " + str(sdk) + "\n"
            for devices in dev_list[sdk]:
                connected_device_string = connected_device_string + str(devices) + " : " + \
                                          str(dev_list[sdk][devices][0]) + "\n"

        self.connected_devices.insert(tkinter.INSERT,connected_device_string)
        self.connected_devices.config(state=DISABLED)

    def screen_reactive(self):
        """
        A method that runs screen reactive using multi thread
        :return: returns None
        """
        try:  # If there were any process that was running RGB control, terminate it
            self.demo_process.terminate()
        except AttributeError:  # If this was the first control, pass
            pass
        self.cur_mode_text.set("Screen Reactive")
        self.demo_process = multiprocessing.Process(target=ScreenReactive.screen_reactive)
        self.demo_process.start()

    def rainbow_all(self):
        """
        A method that runs Rainbow all using multi thread
        :return: returns None
        """
        self.cur_mode_text.set("Rainbow All")
        try:
            self.demo_process.terminate()
        except AttributeError:
            pass
        self.demo_process = multiprocessing.Process(target=RainbowAll.rainbow_all, kwargs={"step": 10})
        self.demo_process.start()

    def static(self):
        """
        A method that runs static rainbow effect with multi thread
        :return: returns None
        """
        self.cur_mode_text.set("Static Color")
        try:
            self.demo_process.terminate()
        except AttributeError:
            pass
        self.demo_process = multiprocessing.Process(target=StaticColor.static_color, kwargs={"r": 0, "g": 255, "b": 0})
        self.demo_process.start()


if __name__ == "__main__":
    u = ui()
    u.start()
