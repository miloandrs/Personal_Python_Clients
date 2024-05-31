#!/usr/bin/env python3
"""
Main interaction methods for connection_brocker.py
"""
# imports
from typing import List
import connection_broker
import device_pooler
from constants import site
from colorama import Fore, Back, Style

devices = device_pooler.site_devices_selection(site)
creds = connection_broker.Authenticator()
def devices_interaction(device, selection: str):
    """
    Please make your selection
    """
    run = connection_broker.NapalmConnect(device, creds)
    execution = {
        '1' : run.get_device_facts(),
        '2' : run.get_device_firmware_version(),
        '3' : run.get_device_environment(),
        '4' : run.get_device_interfaces(),
        '5' : run.get_device_fatal_errors(),
        '6' : run.get_device_mac_address_table(),
        '7' : run.get_bin_file_present()
        
        
    }
    
    formatted_device = '\n' + Fore.YELLOW + Style.BRIGHT + device + Style.RESET_ALL
    formatted_result = '\n' + Fore.GREEN + Style.BRIGHT + execution[selection] + Style.RESET_ALL
    return  formatted_device + formatted_result
    
    