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
    match selection:
        case '1':
            execution = run.get_device_facts()
        case '2':
            execution = run.get_device_firmware_version()
        case '3':
            execution = run.get_device_environment()
        case '4':
            execution = run.get_device_interfaces()
        case '5':
            execution = run.get_device_fatal_errors()
        case '6':
            execution = run.get_device_mac_address_table()
        case '7':
            execution = run.get_bin_file_present()
        case '8':
            print(f"'\n' {Fore.MAGENTA}{Style.BRIGHT}Requires privilege 15{Style.RESET_ALL}")
            _interface = input('Enter interface: ')
            _vlan = int(input('Enter vlan number: '))
            _description = input('Enter description: ')
            execution = run.configure_interface_access(_interface, _vlan, _description)
        case '9':
            print(f"'\n' {Fore.MAGENTA}{Style.BRIGHT}Requires privilege 15{Style.RESET_ALL}")
            _interface = input('Enter interface: ')
            _description = input('Enter description: ')
            _native_vlan = input('Enter native vlan: ')
            _allowed_vlan = input('Enter allowed vlan(s) (for multiple x-xx): ')
            execution = run.configure_interface_trunk(_interface, _description, _native_vlan, _allowed_vlan)



    formatted_device = f"'\n' {Fore.YELLOW}{Style.BRIGHT}{device}{Style.RESET_ALL}"
    formatted_result = f"'\n' {Fore.GREEN}{Style.BRIGHT}{execution}{Style.RESET_ALL}"
    return  formatted_device + formatted_result
    
    