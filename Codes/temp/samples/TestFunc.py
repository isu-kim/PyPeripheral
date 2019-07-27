from cue_sdk import *

cue = CUESDK(r"C:\Users\FlagShipPC\Downloads\CUESDK.x64_2015.dll")
# must define corsair SDK dll directory.
# DO NOT FORGET 'r'. OTHERWISE, IT WOULD NOT WORK.

print(cue.get_device_count())
# for counting my number of devices.

print(cue.get_device_info(0))
print(cue.get_device_info(1))
print(cue.get_device_info(2))
print(cue.get_device_info(3))
# i currently have 4 devices. it starts from 0 


'''
PROGRAM RESULTS 

4
CorsairDeviceInfo(type=<CDT.Mousepad: 4>, model='MM800RGB', physicalLayout=<CPL.Invalid: 0>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)
CorsairDeviceInfo(type=<CDT.Mouse: 1>, model='GLAIVE RGB', physicalLayout=<CPL.Zones3: 8>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)
CorsairDeviceInfo(type=<CDT.Keyboard: 2>, model='K95 RGB PLATINUM', physicalLayout=<CPL.US: 1>, logicalLayout=<CLL.NA: 2>, capsMask=<CDC.Lighting: 1>)
CorsairDeviceInfo(type=<CDT.Headset: 3>, model='VOID PRO USB', physicalLayout=<CPL.Invalid: 0>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)

'''
