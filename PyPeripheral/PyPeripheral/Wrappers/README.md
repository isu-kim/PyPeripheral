# SDK Wrappers
 `SDK Wrapper` is Python Script that works in between SDK provided by the official developers and our library. 

## There are too many SDKs
For example, let's assume we have to turn all RGB LEDs in our Mouse to color RED.
- **Example for Corsair Mouse**
The following code will set Corsair Mouse's LED color RED (255, 0, 0)
```
import cuesdk

c = cuesdk.CueSdk()
c.connect
c.request_control()
# We even do not know which device index the mouse is assigned to
c.set_led_colors_buffer_by_device_index(?device_no?, {M_1, 255, 0, 0})
c.set_led_colors_buffer_by_device_index(?device_no?, {M_2, 255, 0, 0})
c.set_led_colors_buffer_by_device_index(?device_no?, {M_3, 255, 0, 0})
c.set_led_colors_buffer_by_device_index(?device_no?, {M_4, 255, 0, 0})
c.set_led_colors_flush_buffer()
```
- **Example for Razer Mouse**
The following code will set Razer Mouse's LED color RED (255, 0, 0)
```
import requests
import json

url = "http://localhost:54235/razer/chromasdk/"
jsondata = {
    "title": 'PyPheperial',
    "description": 'A Wrapper for PyPheperial',
    "author": {
        "name": 'Gooday2die',
        "contact": 'github.com/gooday2die/pypheperial'
    },
    "device_supported": ['keyboard', 'mouse', 'mousepad'],
    "category": 'application'
}

response = requests.post(url=url, json=jsondata)
uri = json.loads(response.text)['uri']

data = {
        "effect": "CHROMA_STATIC",
        "param": {
            "color": convert_hex(255, 0, 0)
        },
}
response = requests.post(url=uri+"/mouse", data=json.dumps(data))
effect_id = json.loads(response.text)['id']

data = {
    "id": str(effect_id)
}
response = requests.put(url=uri + "/effect", data=json.dumps(data))
```
### Writing different codes for all different SDKs are stupid and takes up too much time.

## Goal
The goal of each `SDK Wrapper` is to provide high-level interface of SDKs to provide easy use of library and polymorphism for ease of development. 
- **Setting Corsair Mouse RGB RED (255, 0, 0) using PyPeripheral**
```
c = Wrappers.Corsair.SDK()
rgb_value = {"Mouse": (255, 0, 0)}
c.set_rgb(rgb_value)
```
- **Setting Razer Mouse RGB RED (255, 0, 0) using PyPeripheral**
```
r = Wrappers.Razer.SDK()
rgb_value = {"Mouse": (255, 0, 0)}
r.set_rgb(rgb_value)
```
- **Setting All Mice RGB RED (255, 0, 0) using PyPeripheral**
```
e = Wrappers.Every.SDK()
rgb_value = {"Mouse": (255, 0, 0)}
e.set_rgb(rgb_value)
```

## Wrapper Abstraction Class Guide
Wrapper Abstraction Class is located as `Wrappers.abstractSDK.py` . This is an abstraction class that provides rough idea and guide for new Wrapper classes to be implemented into this library. If you would like to implement a SDK with your own style of code, make a child class with parent as `abstractSDK.SDK()`. Override each corresponding methods as its features. 
### 1. Connection
 `def connect(self)` : This is a method for connecting our Python library into SDK. When implementing this method, the method should be able to connect and check connection with SDKs. If it is not possible to connect SDKs, it is recommended to `raise` errors or exceptions. 
 - **Returns**: None
 - **Params**: None
### 2. Using SDK
`def use(self)` : This is a method for letting SDKs know that our Python Library would be using the SDK features. This method is meant to request control over SDK. If it is not possible to request control over SDK, it is recommended to `raise` errors or exceptions.
 - **Returns**: None
 - **Params**: None
### 3. Disabling SDK
`def disable(self)` : This is a method for letting SDK know that our Python Library finished using SDK. This method is meant to release control over SDK. This method should be called before exiting the program. There are some SDKs which require manual releasing after using the SDK. For example, Corsair's ICUE SDK would not automatically release itself for a certain amount of time if not released manually. If it is not possible to release control over SDK, it is recommended to `raise` errors or exceptions.
 - **Returns**: None
 - **Params**: None
### 4. Getting All Device Information
`def get_all_device_information(self)` : This method is for getting all connected device information from SDK. This method is expected to return a `dict` type object as its result in a format. A example is shown below.

```
{'MouseMat': ('MM800RGB', 0), 'Keyboard': ('K95 RGB PLATINUM', 1), 'Headset': ('VOID PRO USB', 2),  
'Motherboard': ('ASUS Motherboard', 3), ...}
```
Each `dict` object should contain `type` as its `key` and `tuple` type object containing the connected devices name, and index number as its value. If there is no index assigned by original SDKs, it is suggested to assign one by yourself. **There is no assigning rule, however there should be no multiple index numbers assigned to different devices.** The `type` of devices are listed below. **Please be aware that the list types can be updated later**
1. Mouse
2. Keyboard
3. Headset
4. MouseMat
5. HeadsetStand
6. Cooler
7. MemoryModule
8. Motherboard
9. GPU
10. ETC
11. ALL
 - **Returns**: `dict` type that contains information of connected devices. 
 - **Params**: None

### 5. Getting a Device Information

`def get_device_information(self, index)` : This method is for getting a single device information by index. This method is expected to return a `tuple` type object as its result in following format. A example is shown below. If it is not retrieve information by index, it is recommended to `raise` errors or exceptions. A example is shown below.
```
('Keyboard', 'K95 RGB PLATINUM')
```
`tuple` object must contain the devices `type` and device name as its values. 
 - **Returns**: `tuple` type that contains information of requested device. 
 - **Params**: `integer` type that represents the index of device

### 6. Setting a Device with RGB Colors
`def set_rgb(self, rgb_info)` : This method is to set a specific device's RGB color with provided arguments. This method is expected to take `tuple` of `dict` objects containing following data.
```
({Keyboard, (255,0,0)}, {Mouse, (255,0,0)}, {Headset, (255,0,0)} ...)
```
If requested as up above, this method should be able to set the whole device color as requested `dict` values. Each `dict` object contains `type` and `tuple` type of RGB values. For example, the request up above would set devices as below.
1. **Keyboard** : RGB 255, 0, 0
2. **Mouse** : RGB 255, 0, 0
3. **Headset** : RGB 255, 0, 0
 - **Returns**: None
 - **Params**: `tuple` object that contains `dict` that represents `type` and `tuple` object that contains RGB values.

### Hey, I made a new Wrapper SDK Class! What shall I do?
If you are willing to contribute to our project, and would like your Python Wrapper SDK Class as our library's official Wrapper Class, please Pull Request. However, please verify that the submitted Wrapper SDK Class is working on your devices also, please send me a proof that the code works. Unfortunately, I do not have that many devices to test with, so I am not able to check your code is working or not. My apologies for your inconvenience. Please PR in following format.

1. SDK's Name :
2. SDK Brand : 
3. Proof that the Code works (Video or Image URL) : 
4. Tested device's name : 