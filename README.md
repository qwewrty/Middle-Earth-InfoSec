# Middle Earth InfoSec Tool
This is a human made ring of power to gain more information on other army's inventories and strategies to help in defending your castle. Feel free to make a copy of the ring and forge it into a powerful weapon for your adventure. Made by an amature forger and not by an elf, any kind of correction is welcome!

#### Manual
Welcome human, this is a human readable manual for using the middle-earth InfoSec tool. 
The following weapons are available for the adventure:
1. The eye of Sauron - nmap port scanner
2. Gandalf the Grey - Port scanner which isn't foreign
3. Smaug - netcat written in python
4. Elrond - nslookup - Used to help locate ~~winterfell~~ mordor on the map of middle earth 
without the help of smeagle.(Alright, we might have employed smeagle..)  
5. Password cracker (In the forge)
.  
.  
.  
And my axe.

### Installation and usage
Inorder to run this project just install python3, download this repo and run 
> `python3 meisc.py`

If you want to run a specific module directly like smaug you can do so using the -m argument as shown below.
> `python3 meisc.py -m smaug -lp 7654`

On Linux Systems you can just run as `./meisc.py`

Please note that the usage of "The eye of sauron" requires nmap to be installed on the machine. This functionality is commented out by default and can be enabled easily if required.

### Contributing guide
This project can be expanded to include multiple additional modules which can be easily plugged in. The following steps indicate how this can be done.
1. Write your module in a new file, let us say with name `Mithrandir.py`. This file should contain the method which provide the fuctionality of the module (let us assume that the method is `protectFrodo()`).
2. Edit meisc.py to include your file and add additional arguments if necessary. Edit the help message and the toolList to include your module. Add your method (`protectFrodo`) to the dictionary `functionDict` as the value with module number in the toolList as the key. Refer to `meisc.py` for the specified example included as comments.
3. If you want the module to be directly triggerrable or want to parse the arguments in your own way then write a method in your module with the signature `triggerModule(opts)` where `opts` is an array of tuples of the form `(opt, arg)` where opt is the option specified and arg is the value provided for that option. Note that if a module is specified using `-m`, `meisc.py` will not parse any arguments further, it hands over the control to the module completely.
4. Once the method is written just include the method in `moduleDict` with the module name as the key as shown in the example in `meisc.py`. 

That's it, simple.