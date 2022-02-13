# PyPeripheral  
### A Python Library for Controlling RGB Devices  
>Hello to those who have been starring this repository for a long time. My first commit for this project was 3 years ago. However, I could not update the project since I no longer had the access to my old PC. My old PC had all those Peripheral devices to test with. However, I just got back to my place where I can access my old PC. So I will be updating this project as much as possible. I am sorry for letting you guys wait, and lets get started.  
  
### Motivation & Goal  
I got multiple RGB peripheral devices from multiple brands: Razer, Corsair, MSI. So, whenever I try to use a simple `rainbow` effect for each devices, they do not sync. So the main motivation and goal of this project is to **"Provide a Python library for controlling every RGB devices all together"**   
## Installing this Project  
Installing this library for your personal project would be a piece of cake. There will be multiple ways of installing this project, however the easiest way would be using `pip`.  However, in near future, I will be providing that support as  soon as possible.  
  
  ### Manual Installation
 1. `clone` this repository to your system  
 2. `pip install .` in the directory `PyPeripheral` of this project.  
 3. It will automatically install all necessary dependencies as well.  
  
  ### Installation by PIP
  1. `pip install PyPeripheral`
  2. That's it!
  
## Examples
> Please note that current version of PyPeripheral supports two SDKs.
> - Corsair
> - Razer

### Setting Corsair Keyboard's Color All Red

```
from PyPeripheral import Corsair
c = Corsair.SDK()
c.connect()
c.set_rgb({"Keyboard": (255, 0, 0)})
```

### Setting Razer Mouse Color All Blue
```
from PyPeripheral import Razer
r = Razer.SDK()
r.connect()
r.set_rgb({"Mouse": (0, 0, 255)})
```

### Setting Every Device All Green
```
from PyPeripheral import All
a = All.SDK()
a.connect()
a.set_rgb({"All": (0, 255, 0)})
```
## Demos
For demonstration videos and gifs, please check [here](https://github.com/gooday2die/PyPeripheral/tree/OOP_Version/Demos) for more information! The demo contains most loved **Screen Reactive Lightning** feature as well!
## Contributions  
I do not have every RGB devices on planet Earth. If you have any devices and brands that I do not possess, you can defintely help me out. Do not feel afraid contributing this project. It's open source and everyone can contribute to it.   
  
### I would like to contribute for a SDK  
`Wrapper/abstractSDK.py` has all the information for abstraction. Check [here](https://github.com/gooday2die/PyPeripheral/blob/OOP_Version/PyPeripheral/PyPeripheral/Wrappers/abstractSDK.py) for more information. This project would be a OOP style and abstraction style project. So everyone who is interested in this project can support this project by making a `SDK Wrapper` with their own style. **One and only rule is following the abstraction rules**, and beyond that, everything would be up to you. For example, If you would like to support this project by providing a `SDK Wrapper` for Logitech, you are very much welcomed.  
  
### I would like to volunteer as tester  
Download this project and run simple demos. demos will be provided in the script soon. If you have checked any issues, or confirmed that the program is working for your devices and your environment, let me know by sending a simple email to edina00@naver.com. I will very much appreciate your help and will upload your demo videos or images if provided.  
### I have found a bug  
Please report it through issue sections. Or, if you can manage to fix that bug yourself, please do a PR. Any Issues or PR are always welcomed!