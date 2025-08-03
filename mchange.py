import subprocess
import re
import argparse
from rich import print
import os

def coml () :
 parser = argparse.ArgumentParser(description="MAC ADDR CHANGER > ")
 parser.add_argument("-i","-interface",dest="interface", required=True,help="Network interface")
 parser.add_argument("-m","-mac", dest="new_mac", required=True,help="MAC Address")
 args = parser.parse_args()
 return args
###############################################3

def macch(interface, new_mac):
    print(f"CHANGE THE MAC OF THE INTERFACE: {interface} TO > {new_mac} ")
    subprocess.call(["ifconfig",interface, "down"])
    subprocess.call(["ifconfig", interface,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
###############################################3
def check(interface):
    result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    macs = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result)
    if macs :
        return macs.group(0)
    else :
        print("Couldn't find the mac..!")
###############################################3
option = coml()
if os.geteuid() != 0:
    print("[red]Please run this script with sudo/root privileges![/red]")
    exit()
macch(option.interface, option.new_mac)

currentmac = check(option.interface)

print(f"Current mac > {currentmac} ")


new_mac = check(option.interface)
if new_mac == option.new_mac:
    print(f"[green]MAC ADDR CHANGED SUCCESSFULLY TO >[/green] {new_mac}")
else :
    print("[red]MAC ADDR DID NOT CHANGE [/red]") 


 