#!/usr/bin/python3

import getopt, sys, PortScanner, netcat #, FastScanner

def usage():
    print ("\nMiddle-Earth-InfoSec")
    print ("Usage: middle-earth <options>\n")
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
    # "2": FastScanner.scan,
    "3": netcat.connect,
    "4": netcat.listen
    # "fast-scanner": nmap.nmap
}

moduleDict = {
    "smaug": netcat.triggerModule
}

toolList = """\n1. Slow Scanner
2. Fast Scanner
3. Smaug Connector
4. Smaug Listener
5. NSLookup(in dev)
6. Password Hash cracker(in dev)"""

def defaultExecution():
    tool = input(toolList+"\nWhat do you want to use: ")
    toCall = functionDict.get(tool)
    if toCall:
        toCall()

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
            elif opt in ("-w", "--write"):
                print ("List will extracted from "+arg)
                sys.exit()
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