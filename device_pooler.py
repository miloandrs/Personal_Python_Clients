#!/usr/bin/env python3
"""
Main interaction methods for connection_brocker.py
"""
# imports
from typing import List
from colorama import Fore, Back, Style

def site_devices_selection(site: str) -> List:
    devices = [
        f"{site}-fc-cor-r-a-1",
        f"{site}-fc-cor-r-a-2",
        f"{site}-fc-dis-r-a-1",
        f"{site}-fc-dis-r-a-2",
    ]
    #devices = ['cvg5-co-dis-sw0101', 'cvg5-co-dis-sw0102', 'cvg5-co-dis-sw0201', 'cvg5-co-dis-sw0202', 'cvg5-co-dis-sw0301', 'cvg5-co-dis-sw0302', 'cvg5-co-dis-sw0401', 'cvg5-co-dis-sw0402', 'cvg5-co-dis-sw0501', 'cvg5-co-dis-sw0502', 'cvg5-co-dis-sw0601', 'cvg5-co-dis-sw0602', 'cvg5-co-dis-sw0701', 'cvg5-co-dis-sw0702', 'cvg5-co-dis-sw0801', 'cvg5-co-dis-sw0802', 'cvg5-co-dis-sw0901', 'cvg5-co-dis-sw0902', 'cvg5-co-dis-sw1001', 'cvg5-co-dis-sw1002', 'cvg5-co-dis-sw1201', 'cvg5-co-dis-sw1202']
    return devices

