#!/usr/bin/env python3
"""
Main interaction methods for connection_brocker.py
"""
# imports
from typing import List
from colorama import Fore, Back, Style

def site_devices_selection(site: str) -> List:
    devices = [
         f"{site}-casa-acc-sw-1-1.miloandrs.com"
    ]
    return devices



