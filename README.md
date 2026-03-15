MAC Address Changer (Python)

A simple Python command line tool that changes the MAC address of a network interface on Linux systems.

This project is a small networking / cybersecurity utility built to practice working with:

Python CLI tools

Linux networking commands

Regular expressions

System privilege checks

---------------------------------------------------------------------------------------------------------
Features

Change the MAC address of a network interface
Verify if the MAC address was successfully changed
Command line interface using argparse
Root privilege check

---------------------------------------------------------------------------------------------------------
Requirements

Python 3/ 
Linux system/ 
ifconfig command installed/ 
rich package (pip install rich)

---------------------------------------------------------------------------------------------------------
Usage 

sudo python mac_changer.py -i <interface> -m <new_mac>

Example:

the first byte must be an even number ! 

sudo python mac_changer.py -i eth0 -m 00:11:22:33:44:55

---------------------------------------------------------------------------------------------------------
Author
Cybersecurity student interested in:

Networking/
Linux/
Python security tools/
Ethical hacking

