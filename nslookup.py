import socket

def __reverse_lookup__(ip):
    try:
        print(socket.gethostbyaddr(ip))
    except socket.herror as err:
        print("Cannot resolve address: "+ str(err))

def __lookup__(host):
    try:
        print(socket.gethostbyname_ex(host))
    except socket.gaierror as err:
        print("Cannot resolve name: "+ str(err))

def __call_proper_lookup__(host):
    try:
        # Check if valid IP
        socket.inet_aton(host)
        
        # If IP do a rev lookup 
        __reverse_lookup__(host)
    except socket.error:
        # Else do a normal lookup
        __lookup__(host)

def nslookup():
    host = input("Enter valid IP address or hostname to perform lookup: ")
    __call_proper_lookup__(host)

def triggerModule(opts):
    host=''
    for opt, arg in opts:
        if opt in ('-H', '--host'):
            host=arg
    __call_proper_lookup__(host)
    
    
