## Corsair ICUE LED Mappings
I found out that all the Corsair devices connected to ICUE can be simply controlled via their LED code, **regardless** of their type (Mice, Mousepad, Keyboard, HeadPhones).

Since Corsair did not gave us official mapping system for their devices, I found it in the dirty way; "Brute Force". I do know that it is dirty. However, It is clear known fact that the number of connected LEDs would not exceed 200. So it was pretty much worth it. This took a while for me to find it all by my hand. 

(I also borrowed mappings from the project [cue_sdk by 10se1ucgo](https://github.com/10se1ucgo/cue_sdk) however, a number of LEDs were missing and misplaced at least for me.) 

Took about 5 hours for me to find out all of these.
There might be missing LEDs since I do not possess them all by myself. So, please keep them in mind. Also, I have added a simple python script for you to find your own LED Mappings. If you have other types of Corsair Devices, and would like to help this project, please submit your LED Mappings to me. It would be a massive help.

If you would like to run this whole program, PyPheperial, you can just swap the enumerations file for your disposal. 

ex) if you use K95 RGB , you can just rename K95_RGB_PLAT.py into enumerations.py. Everything would work.

I am planning to make a auto support for this program, so you might not see this directory later in the future. 

If you would like to borrow these key mappings for other projects, feel free to do so. I do not want anyone else to do this dirty work again.

## K95 RGB Mappings
**NOT K95 OLD Version With 18 Macro Keys.**
If you use that one, it is just fine for you to use normal enumerations file.

![K95 RGB Model.](https://github.com/gooday2die/PyPheperial/raw/master/Codes/cue_sdk/enumerations/pics/K95.png)

**Normal Keys**

    Escape = 1
    F1 = 2
    F2 = 3
    F3 = 4
    F4 = 5
    F5 = 6
    F6 = 7
    F7 = 8
    F8 = 9
    F9 = 10
    F10 = 11
    F11 = 12
    GraveAccentAndTilde = 13
    _1 = 14
    _2 = 15
    _3 = 16
    _4 = 17
    _5 = 18
    _6 = 19
    _7 = 20
    _8 = 21
    _9 = 22
    _0 = 23
    MinusAndUnderscore = 24
    Tab = 25
    Q = 26
    W = 27
    E = 28
    R = 29
    T = 30
    Y = 31
    U = 32
    I = 33
    O = 34
    P = 35
    BracketLeft = 36
    CapsLock = 37
    A = 38
    S = 39
    D = 40
    F = 41
    G = 42
    H = 43
    J = 44
    K = 45
    L = 46
    SemicolonAndColon = 47
    ApostropheAndDoubleQuote = 48
    LeftShift = 49
    NonUsBackslash = 50
    Z = 51
    X = 52
    C = 53
    V = 54
    B = 55
    N = 56
    M = 57
    CommaAndLessThan = 58
    PeriodAndBiggerThan = 59
    SlashAndQuestionMark = 60
    LeftCtrl = 61
    LeftGui = 62
    LeftAlt = 63
    Lang2 = 64 #none for US
    Space = 65
    Lang1 = 66 #none for US
    International2 = 67 # none for US
    RightAlt = 68
    RightGui = 69
    Application = 70
    LedProgramming = 71 #none for US
    Brightness = 72
    F12 = 73
    PrintScreen = 74
    ScrollLock = 75
    PauseBreak = 76
    Insert = 77
    Home = 78
    PageUp = 79
    BracketRight = 80
    Backslash = 81
    NonUsTilde = 82
    Enter = 83
    International1 = 84  # none for US
    EqualsAndPlus = 85
    International3 = 86 # none for US
    Backspace = 87
    Delete = 88
    End = 89
    PageDown = 90
    RightShift = 91
    RightCtrl = 92
    UpArrow = 93
    LeftArrow = 94
    DownArrow = 95
    RightArrow = 96
    WinLock = 97
    Mute = 98
    Stop = 99
    ScanPreviousTrack = 100
    PlayPause = 101
    ScanNextTrack = 102
    NumLock = 103
    KeypadSlash = 104
    KeypadAsterisk = 105
    KeypadMinus = 106
    KeypadPlus = 107
    KeypadEnter = 108
    Keypad7 = 109
    Keypad8 = 110
    Keypad9 = 111
    KeypadComma = 112 #none for US
    Keypad4 = 113
    Keypad5 = 114
    Keypad6 = 115
    Keypad1 = 116
    Keypad2 = 117
    Keypad3 = 118
    Keypad0 = 119
    KeypadPeriodAndDelete = 120
**Upper LED Bar Zone**    
The Keyboard has 19 diffrent LED zones in the upper keyboard. (Confirmed by Corsair)

    UpperLedBar1 = 170
    UpperLedBar2 = 171
    UpperLedBar3 = 172
    UpperLedBar4 = 173
    UpperLedBar5 = 174
    UpperLedBar6 = 175
    UpperLedBar7 = 176
    UpperLedBar8 = 177
    UpperLedBar9 = 178
    UpperLedBar10 = 179
    UpperLedBar11 = 180
    UpperLedBar12 = 181
    UpperLedBar13 = 182
    UpperLedBar14 = 183
    UpperLedBar15 = 184
    UpperLedBar16 = 185
    UpperLedBar17 = 186
    UpperLedBar18 = 187
    UpperLedBar19 = 188
**Macro Key Zone**

    G1 = 123
    G2 = 126
    G3 = 129
    G4 = 138
    G5 = 141
    G6 = 144


## Corsair Glaive Pro RGB
I am not quite sure that there is a LED in scroll wheel. 
Otherwise, my mouse is just broken.. :b

The left and right side LED bars are controlled at once. 
![Glaive RGB PRO](https://github.com/gooday2die/PyPheperial/raw/master/Codes/cue_sdk/enumerations/pics/GLAIVE.png)


    GLAV_1 = 189 # side LEDs
    GLAV_2 = 148 # Corsair Logo
    GLAV_3 = 149 # Front LED

## MM800 POLARIS 
MM800 has 15 different LED zones on the surface. (Confirmed by Corsair)
![MM800](https://github.com/gooday2die/PyPheperial/raw/master/Codes/cue_sdk/enumerations/pics/MM800.png)


    MM800_1 = 155 # Mousepad LED #1 from left top.
    MM800_2 = 156 # Mousepad LED #2 from left top.
    MM800_3 = 157 # Mousepad LED #3 from left top.
    MM800_4 = 158 # Mousepad LED #4 from left top.
    MM800_5 = 159 # Mousepad LED #5 from left top.
    MM800_6 = 160 # Mousepad LED #6 from left top.
    MM800_7 = 161 # Mousepad LED #7 from left top.
    MM800_8 = 162 # Mousepad LED #8 from left top.
    MM800_9 = 163 # Mousepad LED #9 from left top.
    MM800_10 = 164 # Mousepad LED #10 from left top.
    MM800_11 = 165 # Mousepad LED #11 from left top.
    MM800_12 = 166 # Mousepad LED #12 from left top.
    MM800_13 = 167 # Mousepad LED #13 from left top.
    MM800_14 = 168 # Mousepad LED #14 from left top.
    MM800_15 = 169 # Mousepad LED #15 from left top.
## Void Pro RGB 
**This is wired model.** 
I am not sure about the wireless model.
There are two controllable LEDs in both Right and Left.
Mute button and Mic On and Off button is not controllable right now.

![VoidProRGB](https://github.com/gooday2die/PyPheperial/raw/master/Codes/cue_sdk/enumerations/pics/VOIDPRO.png)


    # Headset leds
    CLH_LeftLogo = 152
    CLH_RightLogo = 153

    VOIDPRO_L = 152
    VOIDPRO_R = 153


