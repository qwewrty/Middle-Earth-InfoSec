#!/usr/bin/python3

import socket, nmap

scanner = nmap.PortScanner()

def scan():
    host = socket.gethostbyname(input("Enter the host to scan"))
    print(host)
    ports = input("Enter the ports to scan")
    scanner.scan(host, ports)
    for host in scanner.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, scanner[host].hostname()))
        print('State : %s' % scanner[host].state())

        for proto in scanner[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = scanner[host][proto].keys()
            for port in lport:
                print('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))

