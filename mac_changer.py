#!/usr/bin/python3
#things to implement later
#add a network scanner to get the mac address of the host network
#automate the changing of the mac address based on the host network device 


import subprocess
import optparse
import re

def get_arguments():
    parser= optparse.OptionParser()
    parser.add_option("-c","--class", dest="class_1", help="THE class to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (options,arguments)= parser.parse_args()

    if not options.class_1:
        parser.error("type PYTHON3 MAC_CHANGER.PY --HELP")
    elif not options.new_mac:
         parser.error("type PYTHON3 MAC_CHANGER.PY --HELP ")
    return options
    

def change_mac_add(network_class_1 , new_mac_add) :
    print('\n[+]changing mac address for '+ options.class_1 + " to " + options.new_mac)
#not safe
    # subprocess.call("sudo ifconfig " + options.class_1 + " down" , shell=True)
    # subprocess.call("sudo ifconfig " + options.class_1 + " hw ether "+ options.new_mac,shell=True)
    # subprocess.call("sudo ifconfig " + options.class_1 + " up ",shell=True)
#safe
    subprocess.call(["sudo" ,"ifconfig", options.class_1, "down"])
    subprocess.call(["sudo" ,"ifconfig", options.class_1, "hw","ether", options.new_mac])
    subprocess.call(["sudo" ,"ifconfig", options.class_1, "up"])
    
#to print  the output of the result
def get_old_mac (class_1):
    ifconfig = subprocess.check_output(["ifconfig",options.class_1])
    ifconfig = subprocess.check_output(["ifconfig",options.class_1])
    ifconfig= ifconfig.decode('UTF-8')
    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if mac_address_result:
        #print('your mac address has been changed to ' + options.new_mac)
        return(mac_address_result.group(0))
    else:
        print(" \n[!] THE SELECTED INTERFACE HAS NO MAC ADDRESS VALUE (ETHER).")
        exit()

options= get_arguments()

old_mac = get_old_mac(options.class_1)

print('\nyour old_mac_address ' + str(old_mac))

change_mac_add(options.class_1, options.new_mac)

current_mac = get_old_mac(options.class_1)
if current_mac == options.new_mac:
 print('\n MAC ADDRESS WAS SUCCESSFULLY CHANGED TO  ' + str(current_mac))
else:
    print("[-] MAC Address did not get changed .")
