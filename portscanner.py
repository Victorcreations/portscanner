import socket as sock
import queue
import sys
import colorama
from portart import asci
from colorama import Fore,Style
colorama.init(autoreset=True)



print(Fore.LIGHTBLUE_EX + asci)
print("\n")


q = queue.Queue()

HOST_IP = str(input("{}{}Enter HOST_IP here --> ".format(Fore.LIGHTGREEN_EX,Style.BRIGHT)))
START_PORT = int(input("{}{}Enter START_PORT here,(Starting port must be from 1 to 65,535) -->".format(Fore.LIGHTGREEN_EX,Style.BRIGHT)))
END_PORT = int(input("{}{}Enter END_PORT here -->".format(Fore.LIGHTGREEN_EX,Style.BRIGHT)))

for lenght in HOST_IP:
    if len(sys.argv) > 15 and len(sys.argv) < 7:
        print("{}{}Not enough characters IP must be in the format of 0.0.0.0 ".format(Fore.LIGHTGREEN_EX,Style.BRIGHT))
        sys.exit()
    if len(HOST_IP.split(".")) != 4:
        print("{}{}Not in proper format IP must be in the format of 0.0.0.0 and must contain \".\" in between".format(Fore.LIGHTGREEN_EX,Style.BRIGHT))
        sys.exit()

for i in range(START_PORT,END_PORT + 1):
    q.put(i)
    
def port_scan():
    open_ports = False
    while not q.empty():
        port = q.get()
        try:
            with sock.socket(sock.AF_INET,sock.SOCK_STREAM) as s:
                res = s.connect_ex((HOST_IP,port))
                if res == 0:
                    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT} PORT {port} is open in {HOST_IP}")
                    open_ports = True
        except KeyboardInterrupt:
            print(" \n Process interrupted".format(Fore.LIGHTRED_EX,Style.BRIGHT))                          
        except ConnectionRefusedError:
            print("Some problem occured".format(Fore.LIGHTRED_EX,Style.BRIGHT))
        finally:
            s.close()
            
    if not open_ports:
        print("No ports are open".format(Fore.LIGHTRED_EX,Style.BRIGHT))

port_scan()
