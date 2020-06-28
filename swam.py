#
#    ____ _        _ _    _  _
#   / ___\\ \    / // \  | \/ |
#   \__  \ \ \/\/ // ^ \ | \/ |
#   |____/  \_/\_//_/ \_\|_||_|
#            

import os
import socket
import sys
os.system("clear")
def logo():
     print  """
                           ~Writeen By

           ____   ___  ____ _____
          |  _ \ / _ \|  _ \_   _|
          | |_) | | | | |_) || |
          |  __/| |_| |  _ < | |
          |_|    \___/|_| \_\|_|
                                      """

inlogo = """
          ____   _      _   _    _  _
         / ___\ \ \    / / / \  | \/ |
         \__  \  \ \/\/ / / ^ \ | \/ |
         |____/   \_/\_/ /_/ \_\|_||_|
            ~~~

                                   """


def menu():

   print (inlogo + """
   {0}--Information Gathering
   {1}--GET IP Adreess
   {2}--Wireless Wifi Hacking 
   {3}-Exit
 """)
   c=raw_input("swam~# ")
   os.system("clear")
   if c =="0":
      info()
   elif c =="1":
      ipadd()
   elif c =="2":
      wireless()
   elif c =="3":
      logo()
      sys.exit()
   elif c ==" ":
        menu()
   else:
        menu()

def info():
    print(inlogo)
    print("  {1}--Nmap ")
    print("  {2}--Port Scanning")
    print("  {3}--Host To Ip ")
    print("  {99}-Back To Main Menu \n\n")
    c2 = raw_input("swam~# ")
    if c2 == "1":
        os.system('clear')
        nmap()
    if c2 == "2":
        clearScr()
        ports()
    elif c2 =="3":
         h2ip()
    elif c2 == "99":
        clearScr()
        menu()
    elif c2 == "":
        menu()
    else:
        menu()

def ports():
    clearScr()
    target = raw_input('Enter Target IP : ')
    print "------Scanning All PORTS ------\n \n"
    os.system("nmap  -p 1-65535 %s" % target)
    info()
def h2ip():
    host = raw_input("Enter  Host  Name : ")
    ips = socket.gethostbyname(host)
    print("Lp Ip ->",ips)
    lp=os.system("nslookup %s"%host )
    info()
def nmap():

    c3 = raw_input("Like to Installl nmap ? Y / N : ")
    if c3 =="Y" :
        os.system("git clone https://github.com/nmap/nmap.git")
        os.system("cd nmap && ./configure && make && make install")
        print "--[]Nmap Susscessfully Installed --Ready To use "
        nscan()
    elif c3 == "N":
         print "--[!*!]Think nmap Already Installed :---  "
         nscan()

    elif c3 == "":
        menu()
    else:
        menu()

def nscan():
       cho=raw_input("Enter Host Name || IP ->")
       os.system("nmap -Pn -O %s" %cho )
       info()

def ipadd():
    i=raw_input("Enter L->(loacl Ip ) P->(Public ip) L/P -->")
    if i =="L":
       print "----[!] Your Local Ip is 'inet' ** "
       os.system("ifconfig | 'grep' 'inet'  ")
       menu()
    elif i =="P":
       print "--Your Public Ip-- "
       os.system("curl ifconfig.co -4 ")
       menu()
    else:
       menu()


def clearScr():
      os.system('clear')

def wireless():
   clearScr()
   print("[!][!]  Comming Soon .... ")
   print("[!] Using airodump,aircrak ")
   print("[!!]Using Powerfull Tool BLACK_MAMBA By PORT(AK-47)")
   print("[**] Follow https://www.guthub.com/Akumar7042/Black_Mamba.git [!]")
   menu()



if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Thanks For Use Finishing up...\r"),
        time.sleep(0.25)

