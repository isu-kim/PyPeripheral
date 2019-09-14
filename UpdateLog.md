I would be posting update logs here in order for people and me to understand what is going on from September 2019. Before September, all the update logs "can" be found by using Github's commitment history system, which is not suggested. I would be posting some personal comments about the project going on. There might be jokes, do not take these too seriously. :)
***
**2019.09.05**  

 - Working on Config files for multiple use. 
 -  Added Basic GUI Module.

**_Personal Comments:_**
  For Config files, I would be just using simple text files. I do not want my program to find all the connected devices every time they run. It is way less effective. Corsair Does support connected device list, however, Razer does not. To make things worse, it even does not return values if the effect setting was physically valid.

I do not have any experience with GUI, So I might not be able to make something fancy. Would try my best for the design. I will keep everything straight forward as much as possible. However, I am just an Computer Science and Engineering student who is never familiar with Arts and Design... (Never got better than grade C. Back in high school, my art teacher got surprised of the result of my work. Of course in bad way.)

Also, personally, a new semester had begun. That would make me study useless subjects that would never help me out with my life. Those subjects would take time from me coding. I hate those.

I am kind of having difficulties in developing this program in Python. There are toooooooo many limits by using Python than the comfort of using Python. I thought there might have been some more good modules that would help me out with this project. However, the reality was cruel. Seriously, who uses Python for hardware control? All the SDKs that are provided by the Manufacturers are written in C++ or C#. So I am planning to learn C++ and implement this whole project to that language. Might need some time for me to learn C++ skills. I would miss my PyCharm...

Lastly, there had been someone who just sent me an email regarding this project. That guy offered me test support using his devices. That was nice of him. I just wanted to reply the email. However, I was not able. I have sent my email from two different email service providers, however, I was not able to send that at all. Outlook just failed. If you are seeing this text, I am sorry for my late reply.
***
**2019.09.07** 

 - Config file work is fully done
 -  Efficient Commands
 - Made some Classes for OOP 
 - Working on GUIs

***Personal Comments***
 Config file is now fully working. When you first run this program, it would generate a file called Config.txt. Inside that file, it should look like this.

    #PyPheperial Config File
    #Please DO NOT change anything from this file unless you know how it works.
    MOUSE=RAZER,CORSAIR
    KEYBOARD=CORSAIR
    MOUSEPAD=CORSAIR
    HEADSET=CORSAIR
    ETC=CORSAIR
    EOF

It stores informations regarding SDKs for the program to use in the future. Before this update, this program was just kind of brute force. Regardless of the SDKs of your device, this program used to command every device connected to the PC. This was kind of unefficient and not only took more time but more resource as well. 

Classes.
That is the main update of this project. Although I am still working on turning this project into OOP based project, some of major things are already shifted to OOP Classes. Actually, to be honest, I did not know how to use Classes. That was the main thing that I had not used a single Class in my project, which was kind of dumb. Now I know how to use Classes a little bit in order to organize all the functions and variables neatly for myself and others as well.

Now working on Tkinter for GUIs. As I have mentioned up above, I am a seriously bad designer. I had never developed GUIs at all. Personally, I am more used to CLI environment. This would make some think that I am just a geek (Joking). So, If there are someone with Tkinter skills, please let me know. I need some of your help with this project. I can develop GUIs in slower pace, however, I have bunch of other things to do with this project; SDK Wrapping, Reactive keys, and other things. 
