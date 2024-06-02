#!/usr/bin/env Python3

"""
Napalm Personal Client Tests.
"""

# imports
import device_pooler
import executioner
from colorama import Fore, Back, Style
import re
import constants

# Global declaration


def main():
    """
    Main runtime code. 
    """
    while True:
        print(
            """
            Please select your use case
            Q or q to quit
            
            ***
            '1' : get_device_facts,
            '2' : get_device_firmware_version,
            '3' : get_device_environment,
            '4' : get_device_interfaces,
            '5' : get_device_fatal_errors,
            '6' : get_device_mac_address_table,
            '7' : get_bin_file_present,
            '8' : configure_interface_access,
            '9' : configure_interface_trunk,

            """
        )
        
        selection = input("Please enter your request: ")
        if re.match("^[qQ]$", selection):
            return True
        elif re.match("^[1-9]$|^[1-2][0]$|^(10)$", selection):
            devices = device_pooler.site_devices_selection(constants.site)
            for device in devices:
                try:
                    val = executioner.devices_interaction(device, selection)
                    print(val)
                except Exception:
                    print(Fore.RED + Style.BRIGHT + "Unable to connect, bad credentials or device issues" + Style.RESET_ALL)
                    continue
        else :
            print(Fore.RED + Style.BRIGHT + "Please enter a valid choice!" + Style.RESET_ALL)
            continue


if __name__ == "__main__":
    main()
