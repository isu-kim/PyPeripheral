# PyPeripheral
### A Python Library for Controlling RGB Devices  
>This is a upgraded version of PyPeripheral that I wrote 3 years ago. If you would like to check pure python version of this project, please check [this branch](https://github.com/gooday2die/PyPeripheral/tree/OOP_Version)
  
### Motivation & Goal  
I got multiple RGB peripheral devices from multiple brands: Razer, Corsair, MSI. So, whenever I try to use a simple *rainbow shifting* effect for each devices, they do not sync. So the main motivation and goal of this project is to **"Provide a Python library for controlling every RGB devices all together"**   

## Installing this Project  
Installing this library for your personal project would be a piece of cake. There will be multiple ways of installing this project, however the easiest way would be using `pip`. 
  
  ### Manual Installation
 1. `clone` this repository to your system  
 2. `pip install .` in the directory `PyPeripheral` of this project.  
 3. It will automatically install all necessary dependencies as well.  
  
  ### Installation by PIP
  1. `pip install PyPeripheral`
  2. That's it!

### If you encounter those errors:
1. `ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory:`
2. `error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/`
 
Please check [here](https://github.com/gooday2die/PyPeripheral/blob/cython/github/KnownIssues.md) for support. 

## Examples
> Please note that current version of PyPeripheral supports two SDKs.
> - Corsair
> - Razer

Turning on RGBs of each devices is easy as below using PyPeripheral!
### Setting Corsair Keyboard Color Yellow
```
>>> from PyPeripheral import Corsair
>>> a = Corsair.sdk()
>>> a.connect()
True
>>> a.set_rgb({"Keyboard": (255, 255,0)})
1
```
### Setting Razer Mouse Color Red
```
>>> from PyPeripheral import Razer
>>> b = Razer.sdk()
>>> b.connect()
True
>>> b.set_rgb({"Mouse": (255, 255, 0)})
0
```
### Setting All Connected Devices Color Blue
```
>>> from PyPeripheral import All
>>> c = All.sdk()
>>> c.connect()
>>> c.set_rgb({"ALL": (0, 0, 255)})
```

## Using PyPeripheral
Will be updated soon


## Demos
For demonstration videos and gifs, please check [here](https://github.com/gooday2die/PyPeripheral/tree/Cython/Demos) for more information! The demo contains most loved **Screen Reactive Lightning** feature as well!
## Contributions  
I do not have every RGB devices on planet Earth. If you have any devices and brands that I do not possess, you can defintely help me out. Do not feel afraid contributing this project. It's open source and everyone can contribute to it.   
  
### I would like to contribute for a SDK  
Check [here](https://github.com/gooday2die/PyPeripheral/tree/Cython/PyPeripheral/AbstractSDK) for more information. This project would be a OOP style and abstraction style project. So everyone who is interested in this project can support this project by making a `SDK Wrapper` with their own style. **One and only rule is following the abstraction rules**, and beyond that, everything would be up to you. 
  
### I would like to volunteer as tester  
Download this project and run simple demos. demos will be provided in the script soon. If you have checked any issues, or confirmed that the program is working for your devices and your environment, let me know by sending a simple email to edina00@naver.com. I will very much appreciate your help and will upload your demo videos or images if provided.  
### I have found a bug  
Please report it through issue sections. Or, if you can manage to fix that bug yourself, please do a PR. Any Issues or PR are always welcomed!

## Supported SDKs

- Corsair ICUE SDK (By @Gooday2die)
- Razer Chroma SDK (By @Gooday2die)

## Confirmed Checking Devices
Check [here](https://github.com/gooday2die/PyPeripheral/blob/Cython/github/WorkingDevices.md) for more information

