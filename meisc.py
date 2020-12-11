#!/usr/bin/python3

import getopt, sys, PortScanner, netcat #, FastScanner

def usage():
    print ("\nMiddle-Earth-InfoSec")
    print ("Usage: python3 meisc.py\n")
    print ("Module Usage: python3 meisc.py -m <module_name> <options>\n")
    print ("Options:")
    print ("-h                                  Print this help message.")
    print ("-m <module>, --module=<module>      Trigger the module specified directly instead of showing the menu")
    print ("-p <port>, --port=<port>            Specify the port to use")
    print ("-H <hostname>, --host=<hostname>    Specify hostname for operations")
    print ("-c <command>, --command=<command>   Specify the command to execute and connect to")
    print ("-l, --listen                        Listen for a connection")
    print ("")

functionDict = {
    "1": PortScanner.scan,
    # "2": FastScanner.scan, # This is a very powerful module if extended to utilize its capablities.
    "3": netcat.connect,
    "4": netcat.listen
    # "fast-scanner": nmap.nmap
    #"5": Mithrandir.protectFrodo
}

moduleDict = {
    "galadriel": PortScanner.triggerModule,
    "smaug": netcat.triggerModule
    #"mithrandir": Mithrandir.triggerModule
}

toolList = """\n1. Galadriel - Port scanner which isn't foreign?
2. The eye of Sauron - nmap port scanner
3. Smaug Connector - netcat connector
4. Smaug Listener - netcat listener
5. Elrond - NSLookup(in the forge)
6. Password Hash cracker(in the forge)"""
#7. Mithrandir 

def defaultExecution():
    try:
        tool = input(toolList+"\nWhat do you want to use: ")
        toCall = functionDict.get(tool)
        if toCall:
            toCall()
        else:
            print("Sorry the sword is broken and is unavailabe at the moment.")
            sys.exit()
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit()

def triggerModule(opts, selection):
    module = moduleDict.get(selection)
    if module:
        print("Triggering " + selection)
        module(opts)
    else:
        print("No such module available")
        sys.exit()

def parseOptions(argv):
    if len(argv)==0:
        defaultExecution()

    try:
        opts, args = getopt.getopt(argv, "hm:lp:c:tH:", ["help", "module=", "listen", "port=", "command=", "host="])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
            elif opt in ("-m", "--module"):
                triggerModule(opts, arg)
                break
            else:
                usage()
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)
    
def main(argv):
    if len(argv) == 0:
        defaultExecution()
    parseOptions(argv)
    

if __name__ == '__main__':
    main(sys.argv[1:])