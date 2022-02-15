"""
@project : PyPeripheral
@author : Gooday2die
@date : 2022-02-13
@file : Razer.py
"""


import json
import multiprocessing
import time

import requests

from PyPeripheral import abstractSDK
from PyPeripheral import Errors

import subprocess


def put_heart_beat(uri):
    """
    A function that puts heart beat in every 1 second to keep connection alive.
    The official doucment from https://assets.razerzone.com/dev_portal/REST/html/index.html#keeping_the_connection_alive
    mentions that the heartbeat url is http://localhost:123456/chromasdk/heartbeat. But this is wrong. The URL for heartbeat
    is the uri + /heartbeat.
    :param uri: the url of current session
    :return: returns device type in string
    """

    url = uri + "/heartbeat"
    while True:
        requests.put(url)
        time.sleep(1)


class SDK(abstractSDK.SDK):
    """
    A class for implementing wrapper class for Razer SDK
    """

    def __init__(self):
        """
        An initializer method for Corsair ICUE SDK
        """

        self.uri = ""
        self.all_devices = None
        self.heart_beat_thread = None

    def connect(self):
        """
        A connect method for Razer SDK
        :return: returns None
        """
        try:
            url = "http://localhost:54235/razer/chromasdk/"
            jsondata = {
                "title": 'PyPheperial',
                "description": 'A Wrapper for PyPheperial',
                "author": {
                    "name": 'Gooday2die',
                    "contact": 'https://github.com/gooday2die/PyPheperial'
                },
                "device_supported": ['keyboard', 'mouse', 'mousepad', 'headset', 'keypad', 'chromalink'],
                "category": 'application'
            }
            response = requests.post(url=url, json=jsondata)
            try:
                self.uri = json.loads(response.text)['uri']
                self.heart_beat_thread = multiprocessing.Process(target=put_heart_beat, kwargs={"uri": self.uri})
                self.heart_beat_thread.start()  # start heartbeat thread
            except KeyError:
                raise Errors.RazerSDKInitFailError("Cannot retrieve URI from Razer SDK")
            except TypeError:
                raise Errors.RazerSDKInitFailError("Cannot retrieve URI from Razer SDK")

        except requests.exceptions.ConnectionError:  # When the library cannot connect Razer SDK.
            raise Errors.RazerSDKInitFailError("Cannot connect Razer SDK. "
                                               "Please check if you have installed Chroma Connect")

    def disable(self):
        """
        A disable method for Razer SDK.
        This method disables SDK and stops heart beating immediately.
        :return: returns None
        """
        self.heart_beat_thread.terminate()  # stop heart beating immediately
        result = requests.delete(self.uri)
        print(result.text)
        del self.heart_beat_thread

    def get_all_device_information(self):
        """
        A get_all_device_information method for Razer SDK.
        Razer SDK does not provide any way of getting connected devices.
        Thus this method is invalid in this SDK.
        :return: returns dictionary object of all device information
        """

        p = subprocess.Popen(["powershell.exe", "-Command",
                              "Get-PnpDevice -PresentOnly | Where-Object {$_.FriendlyName -match '^Razer'} | Select-Object -Property InstanceId, FriendlyName"],
                             stdout=subprocess.PIPE)
        result = p.stdout.read().decode('utf-8')

        self.all_devices = dict()
        return self.all_devices

    def get_device_information(self, index):
        """
        A get_device_information method for Razer SDK
        Razer SDK does not provide any way of getting connected devices.
        Thus this method is invalid in this SDK.
        :param index: the index of device to get information
        :return: returns Device Information object.
        """
        try:
            pass
        except ValueError:
            raise Errors.InvalidDeviceIndexError("Invalid device index : " + str(index))

    def set_rgb(self, rgb_info):
        """
        A set_rgb method for Razer SDK.

        Since I do not have any Razer devices besides my Deathadders, I could NOT check if other devices work or not.
        Please PR or report issues if you got any problems with your devices.

        :param rgb_info: the rgb_information to set
        :return: returns True if successful, False if failure.
        """
        effect_id_list = list()

        for device_type in rgb_info:
            url_list = list()
            values = rgb_info[device_type]

            if device_type == "MouseMat":
                url_list.append(self.uri + "/mousepad")

            elif device_type == "Mouse":
                url_list.append(self.uri + "/mouse")

            elif device_type == "Keyboard":
                url_list.append(self.uri + "/keyboard")

            elif device_type == "Headset":
                url_list.append(self.uri + "/headset")

            elif device_type == "HeadsetStand":
                raise Errors.InvalidDeviceTypeError("Razer Does not support this device Type: " + device_type)

            elif device_type == "Cooler":
                raise Errors.InvalidDeviceTypeError("Razer Does not support this device Type: " + device_type)

            elif device_type == "MemoryModule":
                raise Errors.InvalidDeviceTypeError("Razer Does not support this device Type: " + device_type)

            elif device_type == "Motherboard":
                raise Errors.InvalidDeviceTypeError("Razer Does not support this device Type: " + device_type)

            elif device_type == "GPU":
                raise Errors.InvalidDeviceTypeError("Razer Does not support this device Type: " + device_type)

            elif device_type == "ETC":
                url_list.append(self.uri + "/keypad")
                url_list.append(self.uri + "/chromalink")
                url_list.append(self.uri + "/devid=45B308F2-CD44-4594-8375-4D5945AD880E")
                url_list.append(self.uri + "/devid=3017280B-D7F9-4D7B-930E-7B47181B46B5")

            elif device_type == "ALL":
                url_list.append(self.uri + "/mousepad")
                url_list.append(self.uri + "/mouse")
                url_list.append(self.uri + "/keypad")
                url_list.append(self.uri + "/chromalink")
                url_list.append(self.uri + "/keyboard")
                url_list.append(self.uri + "/headset")
                url_list.append(self.uri + "/devid=45B308F2-CD44-4594-8375-4D5945AD880E")
                url_list.append(self.uri + "/devid=3017280B-D7F9-4D7B-930E-7B47181B46B5")

            else:
                raise Errors.InvalidDeviceTypeError("Invalid device type name : " + device_type)

            for cur_url in url_list:
                try:  # try generating effect id using effect type CHROMA_STATIC
                    data = {
                        "effect": "CHROMA_STATIC",
                        "param": {
                            "color": self.__convert_hex(values[0], values[1], values[2])
                        },
                    }
                    effect_id = requests.post(cur_url, data=json.dumps(data))
                    effect_id = json.loads(effect_id.text)['id']
                    effect_id_list.append(effect_id)
                except requests.exceptions.MissingSchema:
                    raise Errors.RazerRGBSetError("Cannot set effect. Perhaps you did not use connect method before")
                except ValueError:  # when the value had some wrong values. raise InvalidRgbValue Error.
                    raise Errors.InvalidRgbValueError("RGB Value : " + str(values) + " is invalid RGB Value")
                except KeyError:  # when the effect id was not generated
                    raise Errors.RazerRGBSetError("Cannot generate effect")

        url = self.uri + "/effect"
        data = {
            "ids": effect_id_list
        }

        requests.put(url, data=json.dumps(data))
        # please note that this method does NOT check if a certain request was invalid and failed to set RGB effect
        # if you would like to check why if effect was not working, please print out the request up above.
        # With https://assets.razerzone.com/dev_portal/REST/html/_rz_errors_8h.html, you can find out which error
        # occurred by looking at results.

    @staticmethod
    def __convert_hex(r, g, b):
        """
        A method that converts RGB value into BGR format in hex
        :param r: red value
        :param g: green value
        :param b: blue value
        :return: returns converted BGR value of RGB
        """
        # BGR Format
        hr = "0x{:02x}".format(r)
        hg = "0x{:02x}".format(g)
        hb = "0x{:02x}".format(b)
        bgr_val = int("0x" + str(hb).replace("0x", "") + str(hg).replace("0x", "") + str(hr).replace("0x", ""), 16)

        return bgr_val

    def __repr__(self):
        """
        A __repr__ method for this class
        """
        return "Razer SDK"
