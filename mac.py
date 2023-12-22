
import subprocess
import optparse

def new_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change the mac address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="New mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("please specify a interface, use --help for more information")
    elif not  options.new_mac:
        parser.error("please specify a new_mac, use --help for more information")
    return options

def change_mac(interface,new_mac):
    print("Changing the MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = new_args()
change_mac(options.interface, options.new_mac)




