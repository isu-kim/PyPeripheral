# Demos
This directory is for demonstration of the library. Currently there are following demonstrations.
- Screen Reactive
- Rainbow All
- Static Color
### Please choose one of following
- [I know Python or Programming!](## Programmers)
- [Nope I do not know any Programming...](## Non-Programmers.)

## Programmers

### Screen Reactive
This demo reacts to the most dominant color of the screen. Then sets all device's LED into the dominant color. [Someone from Stackoverflow](https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image) got me Idea of this demo. 

**Demo #1 : Night Vision Goggles** 

![NightVisionDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo1.gif?raw=true)


**Demo #2 : FlashBang**  

![FlashbangDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo2.gif?raw=true)


**Demo #3 : Blood** 

![BloodDemo](https://github.com/gooday2die/PyPheperial/blob/master/Pics/demo3.gif?raw=true)


**Please note that getting most dominant color from the screen is kind of slow and generates delays. I am working on reducing delays and would be fixed in the future** Dependencies are following libraries. 
- Numpy : `pip install numpy`
- Scipy : `pip install scipy`
- MSS : `pip install mss`
- Pillow (AKA PIL) : `pip install pillow`
- PyPeripheral : `pip install PyPeripheral`

Please install those libraries using. Then run `ScreenReactive.py` with Python.

### Rainbow All
This demo turns every device's color into a single rainbow shifting effect. The default speed is set to 10. However if you would like to make it slower or faster, please modify `RainbowAll.py`. The speed is set as `step` in the script. Dependencies are following libraries.
- PyPeripheral : `pip install PyPeripheral`


### Static Color
This demo turns every device's color into a single static color. The default value is set to `(255, 0,0` which is RED in RGB. If you would like to modify the colors, please modify `StaticColor.py` and set it as you would like. Dependencies are following libraries.
- PyPeripheral : `pip install PyPeripheral`

## Non-Programmers
No worries! For Non-programmer and those who have no knowledge regarding Python, this is the right instruction for you. As this project PyPeripheral reads, this project is written in a programming language named Python. In order for you to run all those fancy stuff, you should install Python itself, and some other programs in order for this script to run. **Please  note that this program is not perfect. This might have a lot of bugs, and even can be unable to run on your PC.** 

### Step 1. Installing Python.
Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) in order for you to download Python. I would highly recommend you downloading **any version that is above 3.7**. Especially versions below 3.0 might not be able to run this script at all. **Please install python with default settings, since it is best for beginners to use.  Also be sure to use any version above 3.7**, A detailed tutorial of downloading Python can be found [here](https://phoenixnap.com/kb/how-to-install-python-3-windows).

### Step 2. Checking Python
Once you have finished downloading Python and it seems that you have installed python, please press `windows + r` and type in `cmd`. This will bring up a *Black screen with white characters* (seems like hacking right?)

    python
If the result is something like this

    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
   You have successfully installed Python. Please close this window and follow step 3.

If Not, and if the error is something like this

    'python' is not recognized as an internal or external command, operable program or batch file.

Path of Python is not successfully set. Please refer to 
[https://stackoverflow.com/questions/7054424/python-not-recognized-as-a-command](https://stackoverflow.com/questions/7054424/python-not-recognized-as-a-command) For soloution.

If those do not work, please let me know. 
This step is the most significant step for this script to work.

### Step 3. Download this Program
Please download the **latest** version of release from [here](https://github.com/gooday2die/PyPeripheral/releases/). Then unzip the file in a place that you would like to place at.

### Step 3. Installing dependencies
This program needs a bit more programs in order to work. This is called `dependeny`. This might seem a bit tricky but you have to download those `dependencies` in order for this program to work. **Please note that this needs internet connection and would take some time depending on your PC's spec and network  status.**

- From the folder that you have unzipped from **Step 3**, please double click a file named `installer.bat`. Your computer might or might not warn you from executing this file, but this is nothing suspicious. 
- If you cannot trust me or think the file is suspicious, you can install all the dependencies yourself. by following steps.
- - Open up `cmd` by pressing `window + r` at the same time. Enter `cmd` and open up the black screen with white letters. 
- - Execute following commands on by one:
- 1. `pip install numpy`
- 2. `pip install scipy`
- 3. `pip install mss`
- 4. `pip install pillow`
- 5. `pip install PyPeripheral`

If you have successfully installed all the dependencies, you are almost ready to use this program.

### Step 4. Launching Program**
1. Please download the latest release from [release](https://github.com/gooday2die/PyPeripheral/releases) section up above. Download the `.zip` file and unzip it with any tool that you would like to use. 
2. After you have unzipped the `.zip` file, you can see several files in the folder. **Please note that the files that you are seeing might change from time to time**. 
3. If you have installed all those `dependencies` by **Step 3**, please `double click` a file named `runner.bat`. Your PC might or might not warn you from executing `runner.bat`. The file is not suspicious file. However, if you cannot trust me or think the file is malicious, you can open up the program by `double clicking` the file named `GUI.py`
4. When you see the screen below, it means that you have set everything up correctly.
![enter image description here](https://raw.githubusercontent.com/gooday2die/PyPeripheral/OOP_Version/Demos/ui_pics/ui_1.png)

- On the left side of the program, you are able to see 3 buttons: (Screen Reactive, Rainbow All, Static Color). Those buttons will let you choose which feature to use. 
- - Screen Reactive : Reacts to the screen like [this](### Screen Reactive)
- - Rainbow All : Makes all your devices do a Rainbow Shift effect. Type in `Speed` for the speed of the rainbow shift effect.
- - Static Color: Set all your devices in a color that you would like. Type in `R` , `G`, `B` valuse for your RGB value that you would like to set your devices. 
- On the right side of the program, you are able to see your connected devices. Currently my program only supports **Corsair, Razer** at the moment. If you cannot see your connected devices in right side, please restart your PC or restart your Corsair ICUE or Razer Synapse. 
- On right side of the program, you can see a `Exit` Button for exiting the program. You **Can** use the `X` button, **however I do not suggest you doing so**. If you would like to Exit this program, please press `Exit` button instead of `X` button. 


## I have encountered a bug!
I am sorry to hear that. I have tested the devices on my PC. So, I might have missed some devices or could not test them. **You encountering the bug means that you are the first one that is using that device with this program!** If you would like to help this project by spending your small time for us, I would gladly fix whatever the bug as much as possible. There are two options that you can help us with bugs.

- **Issues at Github**: If you know how to open up issues or do PRs, please do so. **Please feel free to PR or open up issues**
- **Email me**: If you do not know how to use Github, or do not have a Github account, that's OK. Please send me a email at edina00@naver.com. I live in South Korea, so I might take some time to response. 