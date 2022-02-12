
import time
import sys

import cue_sdk
from cue_sdk import *

try:
    input = raw_input
except NameError:
    pass

'''
+ PyPheperial by Gooday2die
This program is for finding each key values of Corsair Keyboards.
I cannot find any so I am making this one for my K95.
If you are using a different Corsair keyboard, please let me know.


This program is simple.
I guess there is no keyboard of more than 200 LEDs.
So this program is going to light all the 200 keys up with red colour 5 times rapidly.
'''


def range_float(start, stop, step):
    while start < stop:
        yield start
        start += step


def redhighlight_key(led_id):
    for i in range(5):
        for x in range_float(0, 2, 0.1):
            Rval = int((1 - abs(x - 1)) * 255)
            Gval = int((1 - abs(x - 1)) * 0)
            Bval = int((1 - abs(x - 1)) * 0)
            led_color = CorsairLedColor(led_id, Rval, Gval , Bval)
            cue.set_led_colors(led_color)
            time.sleep(0.01)
    print(led_id) #this is for debugging which key was lit.

'''
+ PyPheperial by Gooday2die
FUNC : redhighlight_key(led_id)
this would light up the key in red for 5 times rapidly.
if you want to change the numbers of blinking, modify the "for i in range(5)" loop to other numbers.
'''

def findloop(start , stop):
    for i in range(start , stop+1,1):
        redhighlight_key(i)

def main():
    #glowloop()
    #pinkhighlight_key(CLK.TEMP1)
    #redhighlight_key(1)
    print(cue.get_led_positions())
    print(len(cue.get_led_positions()))
    #redhighlight_key(24)
    #findloop(1 , 13)  #first line for me
    #findloop(13 , 24)  #second line for me
    #findloop(25 , 36) # third line for me
    #findloop(37,48) # 4th line for me
    #findloop(49,60) #5th line for me
#    findloop(120,130) #6th line for me.
    #findloop(73)

  # while True:
    #     keyno = int(input("Key : "))
        #   redhighlight_key(keyno)


if __name__ == "__main__":
    # To determine whether or not we are using a 64-bit version of Python,
    # we will check sys.maxsize. 64-bit Python will have a maxsize value of
    # 9223372036854775807, while 32-bit Python will have a mazsize value of
    # 2147483647.
    cue = CUESDK(r"C:\Users\FlagShipPC\Downloads\CUESDK.x64_2015.dll")
    cue.request_control(CAM.ExclusiveLightingControl)
    main()
