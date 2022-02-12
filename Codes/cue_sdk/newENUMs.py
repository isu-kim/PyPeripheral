from enum import Enum, EnumMeta
#import Corsair_K95_PlatRGB.py

__all__ = ['CLK', 'CDT', 'CPL', 'CLL', 'CDC', 'CAM', 'CE']


# Taken from six.py. I didn't use enough six functionality to justify requiring the entire module.
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, 'temporary_class', (), {})


class CEnum(Enum):
    """ctypes compatible Enum"""
    @classmethod
    def from_param(cls, obj):
        return obj.value


class KeywordMeta(EnumMeta):
    """god help me
    things such as 1 and CDC_None don't work as enums, as 1 and None are invalid Python identifiers.
    So, to make it more convinient, this maps CLK[1] to CLK._1, CDC[None] to CDC._None, etc.

    Also, it allows more convinient membership testing for string values.
    """

    def __getitem__(self, item):
        if not isinstance(item, str):
            return super(KeywordMeta, self).__getitem__(str(item))
        return super(KeywordMeta, self).__getitem__(item)

    def __contains__(self, item):
        contains = super(KeywordMeta, self).__contains__(item)
        if contains is False:
            return item in self.__members__
        return contains


class CLK(CEnum, metaclass=KeywordMeta):

    '''
    CLK is for Corsair Keyboard LED Values.
    If you are going to light up just one key, use those here.
    Example) Corsair.ledon(CLK.K95G1 , 255 , 255 , 255 , 0 )
    '''

    Escape = 1,
    F1 = 2,
    F2 = 3,
    F3 = 4,
    F4 = 5,
    F5 = 6,
    F6 = 7,
    F7 = 8,
    F8 = 9,
    F9 = 10,
    F10 = 11,
    F11 = 12,
    GraveAccentAndTilde = 13,
    _1 = 14,
    _2 = 15,
    _3 = 16,
    _4 = 17,
    _5 = 18,
    _6 = 19,
    _7 = 20,
    _8 = 21,
    _9 = 22,
    _0 = 23,
    MinusAndUnderscore = 24,
    Tab = 25,
    Q = 26,
    W = 27,
    E = 28,
    R = 29,
    T = 30,
    Y = 31,
    U = 32,
    I = 33,
    O = 34,
    P = 35,
    BracketLeft = 36,
    CapsLock = 37,
    A = 38,
    S = 39,
    D = 40,
    F = 41,
    G = 42,
    H = 43,
    J = 44,
    K = 45,
    L = 46,
    SemicolonAndColon = 47,
    ApostropheAndDoubleQuote = 48,
    LeftShift = 49,
    NonUsBackslash = 50,
    Z = 51,
    X = 52,
    C = 53,
    V = 54,
    B = 55,
    N = 56,
    M = 57,
    CommaAndLessThan = 58,
    PeriodAndBiggerThan = 59,
    SlashAndQuestionMark = 60,
    LeftCtrl = 61,
    LeftGui = 62,
    LeftAlt = 63,
    Lang2 = 64,
    Space = 65,
    Lang1 = 66,
    International2 = 67,
    RightAlt = 68,
    RightGui = 69,
    Application = 70,
    LedProgramming = 71,
    Brightness = 72,
    F12 = 73,
    PrintScreen = 74,
    ScrollLock = 75,
    PauseBreak = 76,
    Insert = 77,
    Home = 78,
    PageUp = 79,
    BracketRight = 80,
    Backslash = 81,
    NonUsTilde = 82,
    Enter = 83,
    International1 = 84,
    EqualsAndPlus = 85,
    International3 = 86,
    Backspace = 87,
    Delete = 88,
    End = 89,
    PageDown = 90,
    RightShift = 91,
    RightCtrl = 92,
    UpArrow = 93,
    LeftArrow = 94,
    DownArrow = 95,
    RightArrow = 96,
    WinLock = 97,
    Mute = 98,
    Stop = 99,
    ScanPreviousTrack = 100,
    PlayPause = 101,
    ScanNextTrack = 102,
    NumLock = 103,
    KeypadSlash = 104,
    KeypadAsterisk = 105,
    KeypadMinus = 106,
    KeypadPlus = 107,
    KeypadEnter = 108,
    Keypad7 = 109,
    Keypad8 = 110,
    Keypad9 = 111,
    KeypadComma = 112,
    Keypad4 = 113,
    Keypad5 = 114,
    Keypad6 = 115,
    Keypad1 = 116,
    Keypad2 = 117,
    Keypad3 = 118,
    Keypad0 = 119,
    KeypadPeriodAndDelete = 120,

    #Those macro G keys here are for K95 Old version.
    #Which is not a valid value for K95 RGB Platnium.
    #If you are willing to use K95 RGB Platnium, use K95G1 to K95G6 Enums.

    G1 = 121,
    G2 = 122,
    G3 = 123,
    G4 = 124,
    G5 = 125,
    G6 = 126,
    G7 = 127,
    G8 = 128,
    G9 = 129,
    G10 = 130,
    VolumeUp = 131,
    VolumeDown = 132,
    MR = 133,
    M1 = 134,
    M2 = 135,
    M3 = 136,
    G11 = 137,
    G12 = 138,
    G13 = 139,
    G14 = 140,
    G15 = 141,
    G16 = 142,
    G17 = 143,
    G18 = 144,
    International5 = 145,
    International4 = 146,
    Fn = 147,
    Logo = 154,

    #Special LED Zones
    #K95 RGB Platinum LED Upper Bar Zones

    LP_Zone1 = 170,
    LP_Zone2 = 171,
    LP_Zone3 = 172,
    LP_Zone4 = 173,
    LP_Zone5 = 174,
    LP_Zone6 = 175,
    LP_Zone7 = 176,
    LP_Zone8 = 177,
    LP_Zone9 = 178,
    LP_Zone10 = 179,
    LP_Zone11 = 180,
    LP_Zone12 = 181,
    LP_Zone13 = 182,
    LP_Zone14 = 183,
    LP_Zone15 = 184,
    LP_Zone16 = 185,
    LP_Zone17 = 186,
    LP_Zone18 = 187,
    LP_Zone19 = 188,

    #Special LED Zones
    #K95 RGB Platinum Macro Keys

    K95G1 = 123,
    K95G2 = 126,
    K95G3 = 129,
    K95G4 = 138,
    K95G5 = 141,
    K95G6 = 144,

class CLM(CEnum, metaclass=KeywordMeta):

    '''
    CLM is for Corsair Mouse LED Values.
    If you are going to light up just one key, use those here.
    CLM zone values of mouse can vary from each other.
    Example) Corsair.ledon(CLK.CLM_1 , 255 , 255 , 255 , 0 )
    '''

    Z1 = 148,
    Z2 = 149,
    Z3 = 150,
    Z4 = 151,
    Z5 = 189,
    Z6 = 190,

class CLH(CEnum, metaclass=KeywordMeta):

    '''
    CLH is for Corsair Headset LED Values.
    If you are going to light up just one key, use those here.
    Corsair Headset just has two zones. Left and Right.
    Mic LED indicator is not controlled via this ICUE Software.
    Example) Corsair.ledon(CLH.LeftLogo , 255 , 255 , 255 , 0)
    '''

    LeftLogo = 152,
    RightLogo = 153,

class CLMM(CEnum, metaclass=KeywordMeta):
    
    '''
    CLMM is for Corsair Mouse Pad LED Values.
    If you are going to light up just one key, use those here.
    Corsair MM800 have 15 LED Zones. Starting from left top.
    Example) Corsair.ledon(CLMM.Zone1 , 255 , 255 , 255 , 0)
    '''
    
    Zone1 = 155,
    Zone2 = 156,
    Zone3 = 157,
    Zone4 = 158,
    Zone5 = 159,
    Zone6 = 160,
    Zone7 = 161,
    Zone8 = 162,
    Zone9 = 163,
    Zone10 = 164,
    Zone11 = 165,
    Zone12 = 166,
    Zone13 = 167,
    Zone14 = 168,
    Zone15 = 169,

class CLHSS(CEnum, metaclass=KeywordMeta):

    '''
    CLHSS is for Corsair Headset Stand LED Values.
    If you are going to light up just one key, use those here.
    Corsair Headset Stand has 9 LED zones.
    I personally do not have one, so I do not know where the LED numbering starts from.
    Example) Corsair.ledon(CLHSS.Zone1 , 255 , 255 , 255 , 0 )
    '''

    Zone1 = 191,
    Zone2 = 192,
    Zone3 = 193,
    Zone4 = 194,
    Zone5 = 195,
    Zone6 = 196,
    Zone7 = 197,
    Zone8 = 198,
    Zone9 = 199,

class CLD(CEnum, metaclass=KeywordMeta):

    '''
    CLD is for Corsair DIY LED Devices.
    Those might be LED Fans and Hydro devices. (I Guess...)
    
    I do not have Corsair Devices right here, so I do not know any exact mappings.

    However, these are official values from Corsair
    (Yes, I reverse engineered them from their project files.)

    CLD has 2 channels. C1 is the first channel, and C2 is the second channel.
    Again, just run a script going from 200 to 500, then you can know which LED value
    is for your own DIY device.
    
    For those who are unfamiliar with my project nor Python, here is a simple script that
    turns all the LEDs from ID 200 to 500. This would not take a long time before you can 
    actually see them working.
    
    Code:
    
    for i in range(200,500,1):
        Corsair.ledon(i,255,255,255,0)
        
    sleep(10)

    I personally do not have one, so I do not know where the LED numbering starts from.
    Example) Corsair.ledon(CLD_C1_2 , 255 , 255 , 255 , 0 )
    '''

    C1_1 = 200,
    C1_2 = 201,
    C1_3 = 202,
    C1_4 = 203,
    C1_5 = 204,
    C1_6 = 205,
    C1_7 = 206,
    C1_8 = 207,
    C1_9 = 208,
    C1_10 = 209,
    C1_11 = 210,
    C1_12 = 211,
    C1_13 = 212,
    C1_14 = 213,
    C1_15 = 214,
    C1_16 = 215,
    C1_17 = 216,
    C1_18 = 217,
    C1_19 = 218,
    C1_20 = 219,
    C1_21 = 220,
    C1_22 = 221,
    C1_23 = 222,
    C1_24 = 223,
    C1_25 = 224,
    C1_26 = 225,
    C1_27 = 226,
    C1_28 = 227,
    C1_29 = 228,
    C1_30 = 229,
    C1_31 = 230,
    C1_32 = 231,
    C1_33 = 232,
    C1_34 = 233,
    C1_35 = 234,
    C1_36 = 235,
    C1_37 = 236,
    C1_38 = 237,
    C1_39 = 238,
    C1_40 = 239,
    C1_41 = 240,
    C1_42 = 241,
    C1_43 = 242,
    C1_44 = 243,
    C1_45 = 244,
    C1_46 = 245,
    C1_47 = 246,
    C1_48 = 247,
    C1_49 = 248,
    C1_50 = 249,
    C1_51 = 250,
    C1_52 = 251,
    C1_53 = 252,
    C1_54 = 253,
    C1_55 = 254,
    C1_56 = 255,
    C1_57 = 256,
    C1_58 = 257,
    C1_59 = 258,
    C1_60 = 259,
    C1_61 = 260,
    C1_62 = 261,
    C1_63 = 262,
    C1_64 = 263,
    C1_65 = 264,
    C1_66 = 265,
    C1_67 = 266,
    C1_68 = 267,
    C1_69 = 268,
    C1_70 = 269,
    C1_71 = 270,
    C1_72 = 271,
    C1_73 = 272,
    C1_74 = 273,
    C1_75 = 274,
    C1_76 = 275,
    C1_77 = 276,
    C1_78 = 277,
    C1_79 = 278,
    C1_80 = 279,
    C1_81 = 280,
    C1_82 = 281,
    C1_83 = 282,
    C1_84 = 283,
    C1_85 = 284,
    C1_86 = 285,
    C1_87 = 286,
    C1_88 = 287,
    C1_89 = 288,
    C1_90 = 289,
    C1_91 = 290,
    C1_92 = 291,
    C1_93 = 292,
    C1_94 = 293,
    C1_95 = 294,
    C1_96 = 295,
    C1_97 = 296,
    C1_98 = 297,
    C1_99 = 298,
    C1_100 = 299,
    C1_101 = 300,
    C1_102 = 301,
    C1_103 = 302,
    C1_104 = 303,
    C1_105 = 304,
    C1_106 = 305,
    C1_107 = 306,
    C1_108 = 307,
    C1_109 = 308,
    C1_110 = 309,
    C1_111 = 310,
    C1_112 = 311,
    C1_113 = 312,
    C1_114 = 313,
    C1_115 = 314,
    C1_116 = 315,
    C1_117 = 316,
    C1_118 = 317,
    C1_119 = 318,
    C1_120 = 319,
    C1_121 = 320,
    C1_122 = 321,
    C1_123 = 322,
    C1_124 = 323,
    C1_125 = 324,
    C1_126 = 325,
    C1_127 = 326,
    C1_128 = 327,
    C1_129 = 328,
    C1_130 = 329,
    C1_131 = 330,
    C1_132 = 331,
    C1_133 = 332,
    C1_134 = 333,
    C1_135 = 334,
    C1_136 = 335,
    C1_137 = 336,
    C1_138 = 337,
    C1_139 = 338,
    C1_140 = 339,
    C1_141 = 340,
    C1_142 = 341,
    C1_143 = 342,
    C1_144 = 343,
    C1_145 = 344,
    C1_146 = 345,
    C1_147 = 346,
    C1_148 = 347,
    C1_149 = 348,
    C1_150 = 349,

    C2_1 = 350,
    C2_2 = 351,
    C2_3 = 352,
    C2_4 = 353,
    C2_5 = 354,
    C2_6 = 355,
    C2_7 = 356,
    C2_8 = 357,
    C2_9 = 358,
    C2_10 = 359,
    C2_11 = 360,
    C2_12 = 361,
    C2_13 = 362,
    C2_14 = 363,
    C2_15 = 364,
    C2_16 = 365,
    C2_17 = 366,
    C2_18 = 367,
    C2_19 = 368,
    C2_20 = 369,
    C2_21 = 370,
    C2_22 = 371,
    C2_23 = 372,
    C2_24 = 373,
    C2_25 = 374,
    C2_26 = 375,
    C2_27 = 376,
    C2_28 = 377,
    C2_29 = 378,
    C2_30 = 379,
    C2_31 = 380,
    C2_32 = 381,
    C2_33 = 382,
    C2_34 = 383,
    C2_35 = 384,
    C2_36 = 385,
    C2_37 = 386,
    C2_38 = 387,
    C2_39 = 388,
    C2_40 = 389,
    C2_41 = 390,
    C2_42 = 391,
    C2_43 = 392,
    C2_44 = 393,
    C2_45 = 394,
    C2_46 = 395,
    C2_47 = 396,
    C2_48 = 397,
    C2_49 = 398,
    C2_50 = 399,
    C2_51 = 400,
    C2_52 = 401,
    C2_53 = 402,
    C2_54 = 403,
    C2_55 = 404,
    C2_56 = 405,
    C2_57 = 406,
    C2_58 = 407,
    C2_59 = 408,
    C2_60 = 409,
    C2_61 = 410,
    C2_62 = 411,
    C2_63 = 412,
    C2_64 = 413,
    C2_65 = 414,
    C2_66 = 415,
    C2_67 = 416,
    C2_68 = 417,
    C2_69 = 418,
    C2_70 = 419,
    C2_71 = 420,
    C2_72 = 421,
    C2_73 = 422,
    C2_74 = 423,
    C2_75 = 424,
    C2_76 = 425,
    C2_77 = 426,
    C2_78 = 427,
    C2_79 = 428,
    C2_80 = 429,
    C2_81 = 430,
    C2_82 = 431,
    C2_83 = 432,
    C2_84 = 433,
    C2_85 = 434,
    C2_86 = 435,
    C2_87 = 436,
    C2_88 = 437,
    C2_89 = 438,
    C2_90 = 439,
    C2_91 = 440,
    C2_92 = 441,
    C2_93 = 442,
    C2_94 = 443,
    C2_95 = 444,
    C2_96 = 445,
    C2_97 = 446,
    C2_98 = 447,
    C2_99 = 448,
    C2_100 = 449,
    C2_101 = 450,
    C2_102 = 451,
    C2_103 = 452,
    C2_104 = 453,
    C2_105 = 454,
    C2_106 = 455,
    C2_107 = 456,
    C2_108 = 457,
    C2_109 = 458,
    C2_110 = 459,
    C2_111 = 460,
    C2_112 = 461,
    C2_113 = 462,
    C2_114 = 463,
    C2_115 = 464,
    C2_116 = 465,
    C2_117 = 466,
    C2_118 = 467,
    C2_119 = 468,
    C2_120 = 469,
    C2_121 = 470,
    C2_122 = 471,
    C2_123 = 472,
    C2_124 = 473,
    C2_125 = 474,
    C2_126 = 475,
    C2_127 = 476,
    C2_128 = 477,
    C2_129 = 478,
    C2_130 = 479,
    C2_131 = 480,
    C2_132 = 481,
    C2_133 = 482,
    C2_134 = 483,
    C2_135 = 484,
    C2_136 = 485,
    C2_137 = 486,
    C2_138 = 487,
    C2_139 = 488,
    C2_140 = 489,
    C2_141 = 490,
    C2_142 = 491,
    C2_143 = 492,
    C2_144 = 493,
    C2_145 = 494,
    C2_146 = 495,
    C2_147 = 496,
    C2_148 = 497,
    C2_149 = 498,
    C2_150 = 499,






class CDT(CEnum):
    """
    Enumeration containing available device types.
    """
    Unknown = 0
    Mouse = 1
    Keyboard = 2
    Headset = 3
    Mousepad = 4


class CPL(CEnum):
    """
    Enumeration containing available device types.
    """
    Invalid = 0  # dummy value

    # valid values for keyboard
    US = 1
    UK = 2
    BR = 3
    JP = 4
    KR = 5

    # valid values for mouse
    Zones1 = 6
    Zones2 = 7
    Zones3 = 8
    Zones4 = 9


class CLL(CEnum):
    """
    Enumeration containing available logical layouts for keyboards.
    """
    Invalid = 0  # dummy value
    US_Int = 1
    NA = 2
    EU = 3
    UK = 4
    BE = 5
    BR = 6
    CH = 7
    CN = 8
    DE = 9
    ES = 10
    FR = 11
    IT = 12
    ND = 13
    RU = 14
    JP = 15
    KR = 16
    TW = 17
    MEX = 18


# contains list of device capabilities
class CDC(CEnum, metaclass=KeywordMeta):
    _None = 0
    Lighting = 1
CDC._member_map_['None'] = CDC._None


# contains list of available SDK access modes
class CAM(CEnum):
    ExclusiveLightingControl = 0


# contains shared list of all errors which could happen during calling of Corsair* functions
class CE(CEnum):
    # if previously called function completed successfully
    Success = 0
    # CUE is not running or was shut down or third-party control is disabled in CUE settings(runtime error)
    ServerNotFound = 1
    # if some other client has or took over exclusive control (runtime error)
    NoControl = 2
    # if developer did not perform protocol handshake(developer error)
    ProtocolHandshakeMissing = 3
    # if developer is calling the function that is not supported by the server (either because protocol has broken by
    # server or client or because the function is new and server is too old. Check CorsairProtocolDetails for details)
    # (developer error)
    IncompatibleProtocol = 4
    # if developer supplied invalid arguments to the function (for specifics look at function descriptions).
    # (developer error)
    InvalidArguments = 5

