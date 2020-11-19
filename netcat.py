#!/usr/bin/python3

import sys, socket, threading

class writingThread (threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self._isRunning = True
        self.sock = sock

    def run(self):
        try:
            self.readAll()
        except ConnectionAbortedError:
            sys.exit()
            
    def terminate(self):
        self._isRunning = False
    
    def readAll(self):
        print("Ready to read:")
        buffer=b''
        while self._isRunning:
            data = self.sock.recv(1024)
            buffer += data
            if b'\n' in buffer:
                print(buffer.decode('utf-8'), end='')
                buffer=b''
            if not data:
                break
        print(buffer.decode('utf-8'))
        

def connect(hostToConnect='', portToConnect=-1):
    # Get host ip and port to connect to
    host = socket.gethostbyname(hostToConnect if hostToConnect != '' else input("Enter the host to connect to: "))
    port = portToConnect if portToConnect!=-1 else int(input("Enter port to connect to: "))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.timeout(5)
    # Connect to the host and port provided
    connected = s.connect_ex((host, port))
    if connected == 0:
        print("Connected...!")
    else:
        print("Unable to connect error "+ str(connected))
        sys.exit()
    # Start up the listener thread to print received packets onto stdout.
    opThread = writingThread(s)
    opThread.start()
    # Start sending anything written into stdin to the connected host.
    try:
        while 1:
            ip = input()
            s.send((ip+"\r\n").encode('utf-8'))
            # writingThread(s).start()
    except KeyboardInterrupt:
        # Incase of an interrupt stop the thread and quit
        print("Quitting...")
        s.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except ConnectionAbortedError:
        s.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except Exception as err:
        print("oops: "+str(err))

def listen(portToListen=-1):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostbyname("localhost")
    
    port = portToListen if portToListen != -1 else int(input("Enter port to listen on: "))

    serverSocket.bind((host, port))
    serverSocket.listen(3)
    clientSocket, address = serverSocket.accept()
    print("Connected to ", str(address))
    opThread = writingThread(clientSocket)
    opThread.start()

    try:
        while 1:
            ip = input()
            clientSocket.send((ip+"\r\n").encode('utf-8'))
    except KeyboardInterrupt:
        # Incase of an interrupt stop the thread and quit
        print("Quitting...")
        clientSocket.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except ConnectionAbortedError:
        clientSocket.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except Exception as err:
        print("oops: "+str(err))
    

# connect([])
# listen([])
    