
## Wrappers 
These codes would be for wrapping SDKs for Python. 
I will provide some functions definitions for you.

## Corsair SDK
Since most of my personal devices are Corsair, I am more into ICUE Wrapping and those kind of things. 
***
**Functions Available**


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
Finds the number that matches the Devices. No need for Devs to control **Serious Spaghetti Code. Do not try to understand the mechanism inside the function :(**. 

***
**Global Variables**
 - **bool debug**
For checking whether debug mode is on or not.
 - **list DeviceList**
For Listing all the connected devices.
 - **list NewDeviceID**
For Listing all the connected devices. Do not modify this variable. If modified, init process cannot be correctly done.
 - **list DeviceType**
For Listing all the connected devices. Do not modify this variable. If modified, init process cannot be correctly done.***

## Razer SDK
I do have Razer DeathAdder Elite Version which supports Chroma SDK so it would work with other devices. However, I cannot assure that your device would work as well. 
This wrapper took a lot of time for me to develop. As I mentioned before, I am freshmen right now and do not have decent amount of knowledge of RESTful API and HTTP requests. I first was mistaken that URL and URI is same thing but typo :( That made my journey whole worse. I had to get some official examples and reverse engineered it for me to use it in my code. Remember, URL and URI is different thing. Again You can check the full RESTful API from Razer official developer website [here](https://assets.razerzone.com/dev_portal/REST/html/index.html#intro_sec). 
Before you dive into the Razer SDK, you must know the workflow of SDK.
![enter image description here](https://raw.githubusercontent.com/gooday2die/PyPheperial/master/Codes/Wrappers/Razer_SDK_Workflow.png)
Razer SDK by using RESTful API is done in three major steps. 

 1. **Initialization**
Developer sends the application data to REST server by PUT or POST via HTTP. Receives URI and Session info as return value.

2. **Creating Effects**
By that Returned URI  and Session value, we are now able to create Effects. We can set specific LED values and lighting patterns using Effects. And when we create new effect by using API, the server returns Effect ID. Remember, **No physical lighting is changed till here**.

3. **Setting Effects**
By that Returned Effect ID, we request the server to perform physical actions. We send Effect ID to Effect section in Rest Server and when the request is successful, physical things work. **Physical lighting is changed here**


Thanks so much Razer for shitty Documentation. I had to figure out this whole process by myself. 
***
**Functions Available**

 - **debugON(None)**
Start debugging
 - **debugOFF(None)**
Ends debugging
 - **ErrorInfo(errorid)**
Shows more detailed information regarding the error id given. Check [Razer Official Document](https://assets.razerzone.com/dev_portal/REST/html/_rz_errors_8h.html) for more info.
 - **convertHex(R,G,B)**
Simple RGB converter. Razer SDK uses BGR values which is awkward. I decided to use RGB because other SDKs such as Corsair ICUE supports RGB values. And seriously, who the in the world uses BGR format? This function returns BGR hex values. Example below.
>convertHex(255,0,0)
>returns 0x0000ff
 - **geturi(None)**
Requests REST API a session. Session URI would be given as return value. Example Below. That session URI would be used continuously whenever we request any actions using REST api. Example below.
> geturl()
> returns "http://localhost:51019/chromasdk"
 - **createMouseEffect(Effect Name , R , G , B , URI)**
Create mouse led effect. Effect names could be found in the [Razer Official Document Here](https://assets.razerzone.com/dev_portal/REST/html/md__r_e_s_t_external_04_8mouse.html), When this function is called, and successfully requests a Effect ID to the REST API server, it returns Effect ID as return value. This returned Effect ID MUST be sent to the Effect function for physical action to occur.  I would make the effect more easy to use in the future. This function would be fixed or changed into another form in the future. Example below.
> createMouseEffect("CHROMA_STATIC" , 255, 0, 0, "http://localhost:51019/chromasdk")
> returns "AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97"
 - **createHeadsetEffect(Effect Name , R , G , B , URI)**
Create headset led effect. Effect names could be found in the [Razer Official Document Here](https://assets.razerzone.com/dev_portal/REST/html/md__r_e_s_t_external_06_8headset.html), Similar to createMouseEffect Function. **Could not check this working, Since I do not have Razer Headset.** Example below.
> createHeadsetEffect("CHROMA_STATIC" , 255, 0, 0, "http://localhost:51019/chromasdk")
> returns "AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97"
 - **createKeyboardEffect(Effect Name , R , G , B , URI)**
Create Keyboard led effect. Effect names could be found in the [Razer Official Document Here](https://assets.razerzone.com/dev_portal/REST/html/md__r_e_s_t_external_03_8keyboard.html), Similar to createMouseEffect Function. **Could not check this working, Since I do not have Razer Keyboard.** Example below.
> createHeadsetEffect("CHROMA_STATIC" , 255, 0, 0, "http://localhost:51019/chromasdk")
> returns "AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97"
 - **createKeyboardEffect(Effect Name , R , G , B , URI)**
Create Keyboard led effect. Effect names could be found in the [Razer Official Document Here](https://assets.razerzone.com/dev_portal/REST/html/md__r_e_s_t_external_03_8keyboard.html), Similar to createMouseEffect Function. **Could not check this working, Since I do not have Razer Keyboard.** Example below.
> createKeyboardEffect("CHROMA_STATIC" , 255, 0, 0, "http://localhost:51019/chromasdk")
> returns "AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97"
 - **createMousePadEffect(Effect Name , R , G , B , URI)**
Create Mouse Pad led effect. Effect names could be found in the [Razer Official Document Here](https://assets.razerzone.com/dev_portal/REST/html/md__r_e_s_t_external_05_8mousemat.html), Similar to createMouseEffect Function. **Could not check this working, Since I do not have Razer Keyboard.** Example below.
> createMousePadEffect("CHROMA_STATIC" , 255, 0, 0, "http://localhost:51019/chromasdk")
> returns "AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97"
 - **setEffect(Effect ID , URI)**
Sets Effects to physical devices. Without this function executed with effect id, lighting would not be changed. Example below.
> setEffect("AFEBFDBA-641B-4430-AFB4-C4BF38AE7A97" , "http://localhost:51019/chromasdk" )
Would change the LED color if executed correctly.
 - **heartbeat(uri)**
 Puts a NULL value to REST API server in order not to shutdown the session.
***
**Global Variables**
 - **bool debug**
For checking whether debug mode is on or not.

***
**Example Code**
Since Razer SDK is quite more difficult for users to handle than Corsair ICUE, I will show you an example. 

    razeruri = geturi()
    effectid = createMouseEffect("CHROMA_STATIC" . 255 , 0 , 0 , razeruri)
    setEffect(effectid , razeruri)
or

    setEffect(createMouseEffect("CHROMA_STATIC" . 255 , 0 , 0 , geturi()) , geturi())
***
## Future Developments
There would be more supported SDKs from Peripheral companies. 
However, I currently do not have any other devices to test. 
I am going to work on interfaces and ease of use of this program itself. Not the wrappers. 
