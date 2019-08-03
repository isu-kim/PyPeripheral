import requests
import json
import time

global doneInit # for checking if init is done.
global debug

debug = False
doneInit = False


def debugON():
    global debug
    debug = True

def debugOFF():
    global debug
    debug = False

def PostReq(URL , jsondata):
    global debug
    Response = requests.post(url = URL , json = jsondata )
    jsonResult = json.loads(str(Response.text))

    if debug:
        print(Response.text)

    return jsonResult

def KeepAlive():
    Response = requests.put("http://localhost:54235/razer/chromasdk/heartbeat")
    print(Response.text)

def init():
    global doneInit
    url = "http://localhost:54235/razer/chromasdk/"
    data = {
        "title": 'PyPheperial',
        "description":  'A Wrapper for PyPheperial',
        "author": {
            "name":'Gooday2die',
            "contact": 'github.com/gooday2die/pypheperial'
        },
        "device_supported": ['keyboard', 'mouse', 'mousepad'],
        "category": 'application'
    }

    jsonResult = PostReq(url , data)

    if jsonResult['sessionid'] != None :
        print("[INFO] Razer SDK Initialization Success")
        print("[INFO] Razer SDK Session ID : " + str(jsonResult['sessionid']))
        doneInit = True

    else:
        print("[ERROR] Razer SDK Initialization Failed")
        print("Check If Razer SDK is enabled")


def MouseSTATICOn():
    url = "http://localhost:54235/razer/chromasdk/mouse"


    data = {
    "effect": "CHROMA_STATIC",
    "param": {
        "color": 255
        },
    }



    PostReq(url , data)



def MouseLEDOff():

    url = "http://localhost:54235/razer/chromasdk/mouse"

    data = {
    "effect": "CHROMA_NONE"
    }

    PostReq(url , data)


debugON()
#init()


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

print(Response)
print(Response.text)
print(json.loads(Response.text)['uri'])
uri = json.loads(Response.text)['uri']


data = {
    "effect": "CHROMA_STATIC",
    "param": {
        "color": 0xfb
    },
}


response = requests.post(url = uri+"/mouse" , data = json.dumps(data))
print(response)
print(json.loads(response.text))
effectid = json.loads(response.text)['id']





#print(effectid)


'''
response = requests.put(url = uri+"/mouse" , data = json.dumps(data))

print(response)
print(json.loads(response.text))
'''

data = {
    "id" : str(effectid)
}

response = requests.put(url = uri+"/heartbeat" , data = None)
print(response)
print(response.text)

response = requests.put(url = uri+"/heartbeat" , data = None)
print(response)
print(response.text)

response = requests.put(url = uri+"/effect" , data = json.dumps(data))
print("effect " + str(response))
print(json.loads(response.text))
time.sleep(1)





data = {
    "effect": "CHROMA_NONE"
}


response = requests.post(url = uri+"/mouse" , data = json.dumps(data))
print(response)
print(json.loads(response.text))
effectid = json.loads(response.text)['id']




data = {
    "id" : str(effectid)
}



response = requests.put(url = uri+"/effect" , data = json.dumps(data))
print("effect " + str(response))
print(json.loads(response.text))
time.sleep(1)
