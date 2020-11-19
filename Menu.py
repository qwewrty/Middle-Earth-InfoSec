#!/usr/bin/python3

import getopt, sys, PortScanner, netcat #, FastScanner

def usage():
    print ("\nMiddle-Earth-InfoSec")
    print ("Usage: middle-earth <options>\n")
    print ("Options:")
    print ("-h                                Print this help message.")
    print ("-l <file>, --list=<file>          The list will be extracted from the specified file")
    print ("")

functionDict = {
    "1": PortScanner.scan,
    # "2": FastScanner.scan,
    "3": netcat.connect,
    "4": netcat.listen
    # "fast-scanner": nmap.nmap
}

toolList = """\n1. Slow Scanner
2. Fast Scanner
3. Netcat
4. NSLookup(in dev)
5. Password Hash cracker(in dev)"""

def defaultExecution():
    tool = input(toolList+"\nWhat do you want to use: ")
    toCall = functionDict.get(tool)
    if toCall:
        toCall()

def parseOptions(argv):
    if len(argv)==0:
        defaultExecution()

    try:
        opts, args = getopt.getopt(argv, "hl:", ["help", "list="])
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit()
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