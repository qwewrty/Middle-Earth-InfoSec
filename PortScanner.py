#!/usr/bin/python3

import sys,socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def __scanPorts__(host, ports, timeout):
    s.settimeout(timeout)
    for port in ports:
        err = s.connect_ex((host, int(port)))
        if err:
            print("The port {} is closed : {}".format(port, err))
        else:
            print("The port {} is open!".format(port))

def scan(argv=[]):
    host = socket.gethostbyname(input("Enter the host to scan: "))
    ports = input("Enter the ports to scan: ")

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
    __scanPorts__(host, portArray, timeout)

# scan()
