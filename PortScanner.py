#!/usr/bin/python3

import sys,socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def __scanTcpPorts__(host, ports, timeout):
    tcpSocket.settimeout(timeout)
    print("TCP ports:")
    for port in ports:
        err = tcpSocket.connect_ex((host, int(port)))
        if err:
            print("The port {} is closed : {}".format(port, err))
        else:
            print("The port {} is open!".format(port))

def scan(hostToScan="", portsToScan=""):
    host = socket.gethostbyname(hostToScan if hostToScan!="" else input("Enter the host to scan: "))
    ports = portsToScan if portsToScan!="" else input("Enter the ports to scan: ")

    print("Scanning " + host)
    arrays = ports.split(",")
    portArray = []
    for arr in arrays:
        if "-" in arr:
            [start, end] = arr.split("-")
            for i in range(int(start), int(end)+1):
                portArray.append(str(i))
        else:
            portArray.append(arr)

    timeout = 5
    __scanTcpPorts__(host, portArray, timeout)

def triggerModule(opts):
    host=""
    ports=""
    for opt, arg in opts:
        if opt in ("-p", "--port"):
            ports=arg
        elif opt in ('-H', '--host'):
            host=arg
    scan(host, ports)
# scan()
