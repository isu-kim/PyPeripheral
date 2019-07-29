
## Wrappers 
These codes would be for wrapping SDKs for Python. 
I will provide some functions definitions for you.

## Corsair SDK
Since most of my personal devices are Corsair, I am more into ICUE Wrapping and those kind of things. 

Can Do
 - **Set LED light for specific key**
 It is able to set specific LED colour in using RGB Values.
 
 Working On
 - **Key** **Reactive **Lightn**ing**
This would take a while since the process is almost brute force. I have to sniff USB traffics and make a new driver for my Corsair devices. Would take a lot of time for me to finish.

- **Grid Conversion**
To make things more easy to use, I am planning to set all the grids for the LED devices. 


Functions in Python

 - **range_float(start,stop,step)**
Just like the original Python function "range". Just in float form.


- **debug(None)**
For checking if the debug mode is on. Returns Boolean

- **debugON(None)**
Start debugging
- **debugOFF(None)**
Ends debugging

- **DeviceInfo(None)**
lists all the device information and returns an array regarding the information. Example results below.

>[INFO] There are 4 connected Corsair devices.
Device #1 CorsairDeviceInfo(type=<CDT.Mousepad: 4>, model='MM800RGB', physicalLayout=<CPL.Invalid: 0>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)
Device #2 CorsairDeviceInfo(type=<CDT.Mouse: 1>, model='GLAIVE RGB', physicalLayout=<CPL.Zones3: 8>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)
Device #3 CorsairDeviceInfo(type=<CDT.Keyboard: 2>, model='K95 RGB PLATINUM', physicalLayout=<CPL.US: 1>, logicalLayout=<CLL.NA: 2>, capsMask=<CDC.Lighting: 1>)
Device #4 CorsairDeviceInfo(type=<CDT.Headset: 3>, model='VOID PRO USB', physicalLayout=<CPL.Invalid: 0>, logicalLayout=<CLL.Invalid: 0>, capsMask=<CDC.Lighting: 1>)

- **RequestControl(None)**
Send request to ICUE for SDK control. You can just not use this function and set the LED colours, however, it is recommended to use this function before use.

- **ReleaseControl(None)**
Releases  control back to ICUE from SDK control. You can just  not use this function and shutdown the program. However, It is recommended to use this function before shutdown for safety.

- **ledOn(LED_ID,RVal,GVal,BVal,Duration)**
Sets a specific LED as specific RGB Color value. 
Check [Here](https://github.com/gooday2die/PyPheperial/blob/master/Codes/cue_sdk/enumerations/README.md) for more information regarding LED_IDs. 
You can set LED_ID as a CLK.Value or just integer. Both would work. Example below.
>ledOn(CLK.G1,255,0,0,0.2) 
>Turns G1 Macro key into (255,0,0) Red Colour for 0.2 Sec

- **ledSmoothOn(LED_ID,RVal,GVal,BVal,Duration)**
Lights up a specific LED smoothly. It automatically dims after lighting up. Example below.
> ledSmoothOn(CLK.Escape,255,0,0,0.01)
> Lights up ESC key into (255,0,0) smoothly for 0.01 smoothness


- **BlackLED(LED_ID)**
 Turn off a specific LED. You can perform this just by RGB value 0,0,0 instead. 

- **KeyboardCheck(None)**
Checks the keyboard model and lights green LEDs for success.

- **MouseCheck(None)**
Checks the mouse model and lights green LEDs for success.

- **MousePadCheck(None)**
Checks the mousepad model and lights green LEDs for success.

- **HeadPhoneCheck(None)**
Checks the headphone model and lights green LEDs for success.

- **FirstInit(None)**
Checks All the connected devices and requests control over ICUE.

- **DeviceID(DeviceList)**
Finds the number that matches the Devices. No need for Devs to control

- **Variable : debug**
Variable that stores the debug state.

- **Variable : DeviceList**
List that stores all devices

- **Variable : NewDeviceID**
List that stores all devices for future use. No need for other Devs to use

- **Variable : DeviceType**
List that stores all device types for future use. No need for other Devs to use



## Razer SDK
Would be working on it soon after I finish Corsair.
