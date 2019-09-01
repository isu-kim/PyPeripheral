from socket import *


global debug #for debugging purpose.
debug = False


global serverSock
global connectionSock
global addr


def serverInit(server):
    global serverSock
    global connectionSock
    global addr

    if server:
        print("[Communications] Please Establish Connection from Remote Device")
        serverSock = socket(AF_INET, SOCK_STREAM)
        serverSock.bind(('', 5005))
        serverSock.listen(1)
        connectionSock, addr = serverSock.accept()
        init()

    else:
        print("[Communications] Server Is Turned OFF")


def debugON():
    global debug
    debug = True

def debugOFF():
    global debug
    debug = False

'''
#for socket server initialization.
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 5005))
serverSock.listen(1)
connectionSock, addr = serverSock.accept()
'''

def ServerGetData():
    global debug
    getdata = connectionSock.recv(1024)  # Now receiving data
    if debug:
        print('From Client : ', getdata.decode('utf-8')) #just for checking values, commented for dev options
    return getdata.decode('utf-8')

def ServerSendData(senddata):
    global debug
    connectionSock.send(senddata.encode('utf-8'))  # Sending back data
    if debug:
        print('Sent Data to Client : ' +str(senddata)) #just for checking values, commented for dev options.

def CloseServer():
    serverSock.shutdown(SHUT_RDWR)
    serverSock.close()

def ServerHandshake():
    data = str(ServerGetData())
    if (data == "32190984"):
        print("[INFO] Connection Established!")
        print("[INFO] Connecting from : " + str(addr))
        return True # right key and is established
    else :
        print("[ERROR] Wrong Key")
        return False # wrong key and is not established


'''
Number codes
32190984 : Connection Establish Handshake Code
220 : Received Proper Command
990 : Received improper Command (Syntax error or Attribute error)
880 : Terminating Connection

'''


def init():
    while True:
        if (ServerHandshake()):
            ServerSendData("32190984")
            break

#init()
