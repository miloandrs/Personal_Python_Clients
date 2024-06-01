#!/usr/bin/env Python3

"""
Napalm Personal Client.
"""

# Imports
import napalm
import netmiko
import getpass
from typing import Any, Dict, List, Optional
# from logging import Logger
# import json


# Object Blueprints
# Authentication
class Authenticator:
    def __init__(self):
        self.username = "camilo"
        self.password = getpass.getpass()


class NetmikoConnect:
    def __init__(self, entry_hostname: str, authentication: Authenticator):
        pass
        

# Network Device
class NapalmConnect:
    def __init__(self, entry_hostname: str, authentication: Authenticator):
        # Get network driver
        napalm_network_driver = napalm.get_network_driver('ios')
        # Connect
        self.device = napalm_network_driver(
            hostname=entry_hostname,
            username=authentication.username,
            password=authentication.password,
            optional_args={
                "secret": authentication.password,
                "ssh_config_file": "~/.ssh/config"  # This is necessary for WSSH use.
            }
        )
    

    """
    Information gathering methods
    """
    def helper_send_command_timing(self, commands: List[str]) -> dict:
        responses = {}
        for command in commands:
            responses[command] = self.device.device.send_command_timing(command, delay_factor=2000)
        return responses

    def get_device_facts(self):
        # Should return all the info from a device
        self.device.open()
        facts_output = self.device.get_facts()
        self.device.close()
        return facts_output

    def get_device_firmware_version(self):
        # Should return only a string with the version number xx.xx.xx
        self.device.open()
        cli_run = self.device.cli(['show version | include Software,'])
        firmware_version_output = cli_run['show version | include Software,'][31:40]
        self.device.close()
        return firmware_version_output

    def get_device_environment(self):
        self.device.open()
        environment_output = self.device.get_environment()
        self.device.close()
        return environment_output

    def get_device_interfaces(self):
        self.device.open()
        interfaces_output = self.device.get_interfaces()
        self.device.close()
        return interfaces_output

    def get_device_fatal_errors(self):
        self.device.open()
        cli_run_active = self.device.cli(
            ['sh platform hardware fed switch active fwd-asic drops exceptions | i FATAL']
        )
        active_output = (
            f"\n{''.join(cli_run_active['sh platform hardware fed switch active fwd-asic drops exceptions | i FATAL'])}"
        )
        cli_run_standby = self.device.cli(
            ['sh platform hardware fed switch standby fwd-asic drops exceptions | i FATAL']
        )
        standby_output = (
            f"\n{''.join(cli_run_standby['sh platform hardware fed switch standby fwd-asic drops exceptions | i FATAL'])}"
        )
        self.device.close()

        return 'Active' + active_output + '\n' + '\n' + 'Standby' + standby_output + '\n'

    def get_device_mac_address_table(self):
        """
        Returns a list of object dictionaries in this format
            'mac': '01:00:0C:CC:CC:CC',
            'interface': '',
            'vlan': 0,
            'static': True,
            'active': True,
            'moves': -1,
            'last_move': -1.0,
        """
        self.device.open()
        mac_table_output = self.device.get_mac_address_table()
        self.device.close()
        return mac_table_output
    
    def get_bin_file_present(self) -> str:
        """
        Returns if any bin file is present in flash
        """
        self.device.open()
        binfile_cli = self.device.cli(
            ['show flash: | include bin']
        )
        binfile_cli_output = (
            f"\n{''.join(binfile_cli['show flash: | include bin'])}"
        )
        return binfile_cli_output
    
    def stage_bin_console(self, consoles_server: str, image_file: str):
        """
        Uses the console server to stage a image file into the switches
        Need to have this already downloaded to /tftpboot/
        """
        endpoint = f'tftp://{consoles_server}/{image_file}'
        self.device.open()
        self.helper_send_command_timing(
            ["copy {} flash:".format(endpoint)]
        )
        self.device.close()
        
        
    """
    Configuration methods
    """

    def configure_interface_access(self, interface: str, vlan : int, description: str):
        """
        configures interface for access or trunk
        """
        try:       
            self.device.open()
            self.device.load_merge_candidate(
                config=f"interface {interface}\ndescription {description}\nswitchport mode access\nswitchport access vlan {vlan}\npower inline auto\nend\n"
            )

            self.device.commit_config()
            
            return True
        except Exception:
            return False