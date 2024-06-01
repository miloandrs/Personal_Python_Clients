#from typing import List
import connection_broker
#import device_pooler
#from constants import site
from colorama import Fore, Back, Style

creds = connection_broker.Authenticator()
run = connection_broker.NapalmConnect("lab-casa-acc-sw-1-1.miloandrs.com", creds)

test = run.get_device_firmware_version()
print(Fore.GREEN + Style.BRIGHT + test + Style.RESET_ALL)