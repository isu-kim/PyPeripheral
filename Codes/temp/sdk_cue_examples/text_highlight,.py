# Python port of text_highlight.cpp from the CUE SDK examples.
import time
import sys

import cue_sdk
from cue_sdk import *

try:
    input = raw_input
except NameError:
    pass


def range_float(start, stop, step):
    while start < stop:
        yield start
        start += step

'''
+ PyPheperial by Gooday2die
FUNC : range_float (start, stop ,step)
for x in range_float is just like original python function for i in range (start , stop, step)
in our program this is used to make the light in precise colour control.
'''

def highlight_key(led_id):
    for x in range_float(0, 2, 0.1):
        val = int((1 - abs(x - 1)) * 200)
        led_color = CorsairLedColor(led_id, val, val, val)
        cue.set_led_colors(led_color)
        time.sleep(0.03)

'''
+ PyPheperial by Gooday2die
FUNC : highlight_key(led_id)
the function CorsairLedColor(led_id , RVal , GVal , BVal)
the variable named val in this function would make the key glow and dim after keystroke.
since the whole function is in a for loop.
if you want to change the color of this function, you should check function pinkhighlight_key(key_id)
'''

def newkeyled(led_id):
    led_color = CorsairLedColor(led_id, 255, 0, 0)
    # CorsairLedColor(led_id , R , G , B )
    cue.set_led_colors(led_color)
    time.sleep(0.05)

'''
+ PyPheperial by Gooday2die
FUNC : def newkeyled(led_id)
it is similar to FUNC highlight_key(led_id).
However, in this case, it does not have that glowing effect since the function does not have a for loop to execute.
you can just see the quick red blink when you run this function.
'''

def pinkhighlight_key(led_id):
    for x in range_float(0, 2, 0.1):
        Rval = int((1 - abs(x - 1)) * 254)
        Gval = int((1 - abs(x - 1)) * 127)
        Bval = int((1 - abs(x - 1)) * 156)
        led_color = CorsairLedColor(led_id, Rval, Gval , Bval)
        cue.set_led_colors(led_color)
        time.sleep(0.01)
    #print(led_id) #this is for debugging which key was lit.

'''
+ PyPheperial by Gooday2die
FUNC : pinkhighlight_key(led_id)
it is similar to FUNC highlight_key(led_id).
this is just an example for you to change colors of the led.
A colour RGB of Pink is 254 , 127 , 156 . 
Rval is value for Red , Gval is value for Blue , and Bval is the value for Blue.
each values have connectedness since they all use x as their color brightness (not exactly but).
'''

def main():
    word = input("Please, input a word...\n")

    for letter in word:
        try:
            led_id = CLK(cue.get_led_by_name(letter))
        except cue_sdk.exceptions.InvalidArguments:
            continue
        if led_id != CLK.CLI_Invalid:
            #highlight_key(led_id)
            #newkeyled(led_id)
            #redhighlight_key(led_id)
            pinkhighlight_key(led_id)


if __name__ == "__main__":
    # To determine whether or not we are using a 64-bit version of Python,
    # we will check sys.maxsize. 64-bit Python will have a maxsize value of
    # 9223372036854775807, while 32-bit Python will have a mazsize value of
    # 2147483647.
    cue = CUESDK(r"C:\Users\FlagShipPC\Downloads\CUESDK.x64_2015.dll")
    cue.request_control(CAM.ExclusiveLightingControl)
    main()
