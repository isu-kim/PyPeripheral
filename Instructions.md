## Screen Reactive Lighting Setup
If you would like to to try Screen Reactive Lighting (SRL), this is the instructions that you should use.

I will try to explain these instructions in both non-programmer and programmer (Especially Python) perspective. If you do not have any knowledge about Python or any other Programming language, please refer to the **Non-Programmer** section. However, If you are familiar with Python and its OOP concept, please refer to **Programmer** section below. 

I am quite sure that this project would not work in some PCs since, I have not tested them all. If so, please let me know by email (edina00@naverDOTCOM). I would be happy to guide you with specific instructions. 

## Programmer
This section is for those who are familiar with Python and its OOP concepts. There are some dependencies that you must install in order for this Python program to run. Those are the following dependencies that you should install. 

 - **Numpy**
For image processing.
 - **Scipy**
 - **MSS**
For taking screenshots per interval.
 - **Pillow (PIL)**
PIL is not able to install via pip anymore, so please use Pillow instead.
- **Requests** 
For REST API control in using Razer SDK.

Please Install those dependecncies before using this program.
After installing those dependencies, run demo files. (Rainbow,py and screenreactive.py are some demo files). If you can successfully run those two scripts, you can pretty much use all the functions that I have provided. Otherwise, please check Errors and report them to me if you cannot solve them yourself. Also, This script is confirmed running on Python 3.7.4, I highly recommend you using 3.7.4 for best performance. Also, Python below 3.0 might not be able to run this script. Also, be sure to use Python 3.7.4 64bit.

## Non-Programmer
For Non-programmer and those who have no knowledge regarding Python, this is the right instruction for you. As this project PyPheperial reads, this project is written in Python language. In order for you to run all those fancy stuff,, you should install Python itself, and some other programs in order for this script to run. **Please  note that this program is not perfect at all means. This might have a lot of bugs, and even can be unable to run on your PC.** 

**Step 1. Installing Python.**
Visit [https://www.python.org/downloads/](https://www.python.org/downloads/) in order for you to download Python. I would highly recommend you downloading **version 3.7.4**. Especially versions below 3.0 might not be able to run this script at all. **Please install python with default settings, since it is best for beginners to use.  Also, be sure to use Python 3.7.4 64bit.**

**Step 2. Checking Python**
Please go and cmd (yeah that black background with white texts). Enter the code below.

    python
If the result is something like this

    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
   You have successfully installed Python. Please close this cmd window and follow step 3.

If Not, and if the error is something like this

    'python' is not recognized as an internal or external command, operable program or batch file.

Path of Python is not successfully set. Please refer to 
[https://stackoverflow.com/questions/7054424/python-not-recognized-as-a-command](https://stackoverflow.com/questions/7054424/python-not-recognized-as-a-command) For soloution.

If those do not work, please let me know. 
This step is the most significant step for this script to work.

**Step 3. Installing dependencies**
Enter those following commands in cmd.

    python -m pip install numpy
This might take some time. 

    python -m pip install scipy
This might also take some time.

    python -m pip install MSS

This one

    python -m pip install pillow


And this one also.

    python -m pip install requests



If you have successfully installed all the dependencies, you are almost ready to use this program.

**Step 4. Launching Program**
Please unzip the zip file in the release section. By unzipping you get some files and directories.

 - Wrapper (Directory)
 - main.py
 - Rainbow.py
 - screenreactive.py

There is no need for you to visit Wrapper directory at all. It contains some of key scripts for this one to run. If you wish to edit some of them, please do it at your own risk.

First, double click main.py. If the black window comes in and out, something had  gone wrong. Then please take following steps.

 - Rightclick main.py
 - Open with IDLE
 - Run script (F5)
 - There would be some error information
 - Check information and send it to me (edina00@naverDOTCOM)

If this script sucesfully works, please enter the devices connected. Follow the instructions in the program. Only uppercase letters are recognized. Write CORSAIR instead of Corsair. And also, if you have more than one device per category, please enter all of them. 

*Ex) If you have one Razer mouse and one Corsair mouse, please Enter CORSAIR,RAZER in the mouse section.* (Order does not matter here). Unfortunately there are only two main SDKs that this program supports. 

If all the things go as intended, and if nothing crashed, it is time for you to take another step into this project.

Run Rainbow.py. This will ask you the speed of rainbow shifting effect. Higher the faster.

Lastly, please run screenreactive.py. This will ask you if you would like debuging mode or not. Enter False to this prompt. You are ready to go.




## ETC
If anything goes wrong, please make a contact to me via email (edina00@naverDOTCOM). I would be more than happy to help you out with my script. 
