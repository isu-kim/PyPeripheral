import json
import requests

global debug
debug = False


def debug_on():
    global debug
    debug = True
    if debug:
        print("[RAZER] Razer SDK Debug Mode On")


def debug_off():
    global debug
    debug = False
    print("[INFO] Razer SDK Debug Mode OFF")


def error_info(error_id):
    if error_id == -1:
        print("[RAZER] Error : Invalid ")
        
    elif error_id == 5:
        print("[RAZER] Error : Access Denied")
        
    elif error_id == 6:
        print("[RAZER] Error : Invalid Handle")
        
    elif error_id == 50:
        print("[RAZER] Error : Not Supported")
        
    elif error_id == 87:
        print("[RAZER] Error : Invalid Parameter")
        
    elif error_id == 1062:
        print("[RAZER] Error : Service Not Started")
        
    elif error_id == 1167:
        print("[RAZER] Error : Device Not Connected")
        
    elif error_id == 1168:
        print("[RAZER] Error : Element Not Found")
        
    elif error_id == 1235:
        print("[RAZER] Error : Request Aborted")
        
    elif error_id == 1247:
        print("[RAZER] Error : Already Initialized")
        
    elif error_id == 4309:
        print("[RAZER] Error : Resource Disabled")
        
    elif error_id == 4319:
        print("[RAZER] Error : Device Not Supported or Available.")
        
    elif error_id == 5023:
        print("[RAZER] Error : The Group is in Invalid State")
        
    elif error_id == 259:
        print("[RAZER] Error : No More Items")
        
    elif error_id == 2147500037:
        print("[RAZER] Error : Unexpected Error")
        

def convert_hex(r, g, b):
    # BGR Format
    hr = "0x{:02x}".format(r)
    hg = "0x{:02x}".format(g)
    hb = "0x{:02x}".format(b)
    bgrval = int("0x"+str(hb).replace("0x", "")+str(hg).replace("0x", "")+str(hr).replace("0x", ""), 16)
    if debug:
        print("[RAZER] Converted RGB : ("+str(r), str(g), str(b)+") to BGR Hex Value "
              + str("0x"+str(hb).replace("0x", "") + str(hg).replace("0x", "") + str(hr).replace("0x", "")))

    return bgrval


def get_uri():
    global debug

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

    if debug:
        print("[INFO] Razer SDK Rest Session ID : " + str(json.loads(response.text)['sessionid']))
        print("[INFO] Razer SDK Rest API URI : " + str(uri))

    return uri


def create_mouse_effect(effect_name, r, g, b, uri):
    data = {
            "effect": effect_name,
            "param": {
                "color": convert_hex(r, g, b)
            },
    }
    try:
        response = requests.post(url=uri+"/mouse", data=json.dumps(data))

        if json.loads(response.text)['result'] == 0:
            effect_id = json.loads(response.text)['id']

            if debug:
                print("[RAZER] Successfully Created Mouse Effect ID : " + str(effect_id))
            return effect_id

        else:
            error_info(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createMouseEffect Function")

    except TypeError:
        print("[RAZER] ERROR in createMouseEffect Function , Device does not seem to exist")
        return None


def create_keyboard_effect(effect_name, r, g, b, uri):
    data = {
            "effect": effect_name,
            "param": {
                "color": convert_hex(r, g, b)
            },
    }
    try:
        response = requests.post(url=uri+"/keyboard", data=json.dumps(data))

        if json.loads(response.text)['result'] == 0:
            effect_id = json.loads(response.text)['id']

            if debug:
                print("[RAZER] Successfully Created Keyboard Effect ID : "+str(effect_id))
            return effect_id

        else:
            error_info(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createKeyboardEffect Function")

    except TypeError:
        print("[RAZER] ERROR in createKeyboardEffect Function , Device does not seem to exist")
        return None


def create_mousepad_effect(effect_name, r, g, b, uri):
    data = {
            "effect": effect_name,
            "param": {
                "color": convert_hex(r, g, b)
            },
    }
    try:
        response = requests.post(url=uri+"/mousepad", data=json.dumps(data))
        if json.loads(response.text)['result'] == 0:
            effect_id = json.loads(response.text)['id']
            if debug:
                print("[RAZER] Successfully Created Mouse Pad Effect ID : " + str(effect_id))
            return effect_id
        else:
            error_info(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createMousePadEffect Function")
    except TypeError:
        print("[RAZER] ERROR in createMousePadEffect Function , Device does not seem to exist")
        return None


def create_headset_effect(effect_name, r, g, b, uri):
    data = {
            "effect": effect_name,
            "param": {
                "color": convert_hex(r, g, b)
            },
    }
    try:
        response = requests.post(url=uri+"/headset", data=json.dumps(data))

        if json.loads(response.text)['result'] == 0:
            effect_id = json.loads(response.text)['id']

            if debug:
                print("[RAZER] Successfully Created Headset Effect ID : " + str(effect_id))
            return effect_id

        else:
            error_info(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createHeadsetEffect Function")

    except TypeError:
        print("[RAZER] ERROR in createHeadsetEffect Function , Device does not seem to exist")
        return None


def create_etc_effect(effect_name, r, g, b, uri):
    data = {
            "effect": effect_name,
            "param": {
                "color": convert_hex(r, g, b)
            },
    }
    try:
        response = requests.post(url=uri+"/chromalink", data=json.dumps(data))

        if json.loads(response.text)['result'] == 0:
            effect_id = json.loads(response.text)['id']

            if debug:
                print("[RAZER] Successfully Created ETC Effect ID : " + str(effect_id))
            return effect_id

        else:
            error_info(json.loads(response.text)['result'])
            print("[RAZER] ERROR in createETCEffect Function")

    except TypeError:
        print("[RAZER] ERROR in createETCEffect Function , Device does not seem to exist")
        return None


def set_effect(effect_id, uri):
    if effect_id == 0:
        print("[RAZER] Effect ID invalid : " + str(effect_id))
        return

    data = {
        "id": str(effect_id)
    }
    response = requests.put(url=uri + "/effect", data=json.dumps(data))
    if debug:
        print(json.loads(response.text)['result'])  # 0 means success
    if json.loads(response.text)['result'] == 0:
        if debug:
            print("[RAZER] Successfully Set Effect ID : " + str(effect_id))
        return True  # returns true if setting effect was successful.
    else:
        error_info(json.loads(response.text)['result'])
        print("[RAZER] ERROR in setEffect Function")
        return False  # returns false if setting effect was failure


def heartbeat(uri):
    response = requests.put(url=uri + "/heartbeat", data=None)
    if debug:
        print("[RAZER] Heartbeat Tick : " + str(json.loads(response.text)['tick']))
