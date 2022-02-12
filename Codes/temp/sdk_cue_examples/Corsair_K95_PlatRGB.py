'''
+ PyPheperial by Gooday2die
This file is for K95 RGB Platinum LED key bindings.
It might not be applicable to other Corsair Keyboards.

Feel free to use this file and chart for your disposal.
'''


class CLK(CEnum, metaclass=KeywordMeta):
    """
    Enumeration containing available keys
    """
    CLI_Invalid = 0  # dummy value

    # keyboard leds

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

    #First Line

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

    #Second Line

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

    #Third Line

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

    #4th Line

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

    #5th line

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

    #6th line

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


    UpperLedBar1 = 188


    '''
    All none for US
    G1 = 121
    G2 = 122
    G3 = 123
    G4 = 124
    G5 = 125
    G6 = 126
    G7 = 127
    G8 = 128
    G9 = 129
    G10 = 130
    '''


    VolumeUp = 131
    VolumeDown = 132
    MR = 133
    M1 = 134
    M2 = 135
    M3 = 136
    G11 = 137
    G12 = 138
    G13 = 139
    G14 = 140
    G15 = 141
    G16 = 142
    G17 = 143
    G18 = 144
    International5 = 145
    International4 = 146
    Fn = 147

    # Mouse leds
    CLM_1 = 148
    CLM_2 = 149
    CLM_3 = 150
    CLM_4 = 151

    # Headset leds
    CLH_LeftLogo = 152
    CLH_RightLogo = 153

    Logo = 154
    CLI_Last = 154
CLK._member_map_['1'] = CLK._1
CLK._member_map_['2'] = CLK._2
CLK._member_map_['3'] = CLK._3
CLK._member_map_['4'] = CLK._4
CLK._member_map_['5'] = CLK._5
CLK._member_map_['6'] = CLK._6
CLK._member_map_['7'] = CLK._7
CLK._member_map_['8'] = CLK._8
CLK._member_map_['9'] = CLK._9
CLK._member_map_['0'] = CLK._0
