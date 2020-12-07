#!/usr/bin/python3

import sys, socket, threading, subprocess

# def setNonBlocking(fd):
#     """
#     Set the file description of the given file descriptor to non-blocking.
#     """
#     flags = fcntl.fcntl(fd, fcntl.F_GETFL)
#     flags = flags | os.O_NONBLOCK
#     fcntl.fcntl(fd, fcntl.F_SETFL, flags)

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
        # print("Ready to read:")
        # buffer=b''
        while self._isRunning:
            data = self.sock.recv(1)
            # buffer += data
            # if b'\n' in buffer:
            #     sys.stdout.write(buffer.decode('utf-8'))
                # buffer=b''
            if not data:
                break
            sys.stdout.write(data.decode('utf-8'))
        # sys.stdout.write(buffer.decode('utf-8'))
        

def connect(hostToConnect='', portToConnect=-1, command=None):
    # Get host ip and port to connect to
    host = socket.gethostbyname(hostToConnect if hostToConnect != '' else input("Enter the host to connect to: "))
    port = portToConnect if portToConnect!=-1 else int(input("Enter port to connect to: "))
    proc = None

    print("Connecting to " + host + ":"+str(port))
    # Does not work
    # if file!=None:
    #     sys.stdout = file
    #     sys.stdin = file

    if command!=None:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=1, universal_newlines=True)
        sys.stdout = proc.stdin
        sys.stdin = proc.stdout

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.timeout(5)
    # Connect to the host and port provided
    connected = s.connect_ex((host, port))
    if connected == 0:
        sys.stdout.write("Connected...!\n")
    else:
        sys.stderr.write("Unable to connect error "+ str(connected) + "\n")
        sys.exit()
    # Start up the listener thread to print received packets onto stdout.
    opThread = writingThread(s)
    opThread.setDaemon(True)
    opThread.start()
    # Start sending anything written into stdin to the connected host.
    try:
        while 1:
            ip = sys.stdin.readline()
            s.send((ip).encode('utf-8'))
    except (KeyboardInterrupt, ConnectionAbortedError):
        # Incase of an interrupt stop the thread and quit
        sys.stdout.write("Quitting...")
        s.shutdown(socket.SHUT_WR)
        opThread.terminate()
        if proc!= None:
            proc.terminate()
        sys.exit()
    except Exception as err:
        sys.stderr.write("oops: "+str(err))

def listen(portToListen=-1, command=None):
    # Initialize listener on localhost
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostbyname("localhost")
    
    # Get port to listen on
    port = portToListen if portToListen != -1 else int(input("Enter port to listen on: "))

    print("Listening on " + str(port))

    # Bind and start lisening on port
    serverSocket.bind((host, port))
    serverSocket.listen(3)

    # Startup the subprocess command if provided
    if command!=None:
        proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=1, universal_newlines=True)
        sys.stdout = proc.stdin
        sys.stdin = proc.stdout

    # Continue once we have the connection
    clientSocket, address = serverSocket.accept()
    sys.stdout.write("Connected to "+ str(address) + "\n")

    # Start up the listener thread to print received packets onto stdout.
    opThread = writingThread(clientSocket)
    opThread.setDaemon(True)
    opThread.start()

    # Start sending anything written into stdin to the connected host.
    try:
        while 1:
            ip = sys.stdin.readline()
            clientSocket.send((ip).encode('utf-8'))
    except KeyboardInterrupt:
        # Incase of an interrupt stop the thread and quit
        sys.stdout.write("Quitting...")
        clientSocket.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except ConnectionAbortedError:
        clientSocket.shutdown(socket.SHUT_WR)
        opThread.terminate()
        sys.exit()
    except Exception as err:
        sys.stderr.write("oops: "+str(err))
    

def triggerModule(opts):
    port = -1
    isListener = False
    host=''
    command=None
    for opt, arg in opts:
        if opt in ("-l","--listen"):
            isListener = True
        elif opt in ("-p", "--port"):
            port = int(arg)
        elif opt in ("-t", "--host"):
            host = arg
        elif opt in ("-c", "--command"):
            command = [arg.split(" ")]
    if isListener:
        listen(port, command)
    else:
        connect(host, port, command)
# connect("localhost", 9876, ["nc localhost 9000"])
# listen([])
    