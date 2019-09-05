import json
import requests

global debug
debug = False


def debugON():
    global debug
    debug = True
    if debug:
        print("[RAZER] Razer SDK Debug Mode On")

def ErrorInfo(errorid):
    if errorid == -1:
        print("[RAZER] Error : Invalid ")
    elif errorid == 5:
        print("[RAZER] Error : Access Denied")
    elif errorid == 6:
        print("[RAZER] Error : Invalid Handle")
    elif errorid == 50:
        print("[RAZER] Error : Not Supported")
    elif errorid == 87:
        print("[RAZER] Error : Invalid Parameter")
    elif errorid == 1062:
        print("[RAZER] Error : Service Not Started")
    elif errorid == 1167:
        print("[RAZER] Error : Device Not Connected")
    elif errorid == 1168:
        print("[RAZER] Error : Element Not Found")
    elif errorid == 1235:
        print("[RAZER] Error : Request Aborted")
    elif errorid == 1247:
        print("[RAZER] Error : Already Initialized")
    elif errorid == 4309:
        print("[RAZER] Error : Resource Disabled")
    elif errorid == 4319:
        print("[RAZER] Error : Device Not Supported or Available.")
    elif errorid == 5023:
        print("[RAZER] Error : The Group is in Invalid State")
    elif errorid == 259:
        print("[RAZER] Error : No More Items")
    elif errorid == 2147500037:
        print("[RAZER] Error : Unexpected Error")

def debugOFF():
    global debug
    debug = False
    print("[INFO] Razer SDK Debug Mode OFF")


def convertHex(R,G,B):
    #BGR Format
    Hr = "0x{:02x}".format(R)
    Hg = "0x{:02x}".format(G)
    Hb = "0x{:02x}".format(B)
    BGRVal = int("0x"+str(Hb).replace("0x","")+str(Hg).replace("0x","")+str(Hr).replace("0x","") , 16)
    if debug:
        print("[RAZER] Converted RGB : ("+str(R),str(G),str(B)+") to BGR Hex Value " + str("0x"+str(Hb).replace("0x","")+str(Hg).replace("0x","")+str(Hr).replace("0x","")))

    return BGRVal


def geturi():
    global debug

    URL = "http://localhost:54235/razer/chromasdk/"
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

    Response = requests.post(url=URL, json=jsondata)
    uri = json.loads(Response.text)['uri']

    if debug:
        print("[INFO] Razer SDK Rest Session ID : " + str(json.loads(Response.text)['sessionid']))
        print("[INFO] Razer SDK Rest API URI : " + str(uri))


    return uri

def createMouseEffect(effectName , r , g ,b , uri):
    data = {
            "effect": effectName,
            "param": {
                "color": convertHex(r , g ,b)
            },
    }
    try:
        response = requests.post(url=uri+"/mouse", data=json.dumps(data))
        if json.loads(response.text)['result'] == 0:
            effectid = json.loads(response.text)['id']
            if debug:
                print("[RAZER] Successfully Created Mouse Effect ID : " + str(effectid))
            return effectid
        else:
            ErrorInfo(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createMouseEffect Function")
    except TypeError:
        print("[RAZER] ERROR in createMouseEffect Function , Device does not seem to exist")
        return None



def createKeyboardEffect(effectName , r , g ,b , uri):
    data = {
            "effect": effectName,
            "param": {
                "color": convertHex(r , g ,b)
            },
    }
    try:
        response = requests.post(url=uri+"/keyboard", data=json.dumps(data))
        if json.loads(response.text)['result'] == 0:
            effectid = json.loads(response.text)['id']
            if debug:
                print("[RAZER] Successfully Created Keyboard Effect ID : "+str(effectid))
            return effectid
        else:
            ErrorInfo(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createKeyboardEffect Function")

    except TypeError:
        print("[RAZER] ERROR in createKeyboardEffect Function , Device does not seem to exist")
        return None



def createMousePadEffect(effectName , r , g ,b , uri):
    data = {
            "effect": effectName,
            "param": {
                "color": convertHex(r , g ,b)
            },
    }
    try:
        response = requests.post(url=uri+"/mousepad", data=json.dumps(data))
        if json.loads(response.text)['result'] == 0:
            effectid = json.loads(response.text)['id']
            if debug:
                print("[RAZER] Successfully Created Mouse Pad Effect ID : " + str(effectid))
            return effectid
        else:
            ErrorInfo(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createMousePadEffect Function")
    except TypeError:
        print("[RAZER] ERROR in createMousePadEffect Function , Device does not seem to exist")
        return None



def createHeadsetEffect(effectName , r , g ,b , uri):
    data = {
            "effect": effectName,
            "param": {
                "color": convertHex(r , g ,b)
            },
    }
    try:
        response = requests.post(url=uri+"/headset", data=json.dumps(data))
        if json.loads(response.text)['result'] == 0:
            effectid = json.loads(response.text)['id']
            if debug:
                print("[RAZER] Successfully Created Headset Effect ID : " + str(effectid))
            return effectid
        else:
            ErrorInfo(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createHeadsetEffect Function")
    except TypeError:
        print("[RAZER] ERROR in createHeadsetEffect Function , Device does not seem to exist")
        return None


def setEffect(effectid , uri):
    if effectid == None:
        print("[RAZER] Effect ID invalid : " + str(effectid))
        return

    data = {
        "id": str(effectid)
    }
    response = requests.put(url=uri + "/effect", data=json.dumps(data))
    if debug:
        print(json.loads(response.text)['result']) # 0 means success
    if json.loads(response.text)['result'] == 0:
        if debug:
            print("[RAZER] Successfully Set Effect ID : " + str(effectid))
        return True #returns true if setting effect was successful.
    else:
        ErrorInfo(json.loads(response.text)['result'])
        print("[RAZER] ERROR in setEffect Function")
        return False #returns false if setting effect was failure

def heartbeat(uri):
    response = requests.put(url=uri + "/heartbeat", data=None)
    if debug:
        print("[RAZER] Heartbeat Tick : " + str(json.loads(response.text)['tick']))

