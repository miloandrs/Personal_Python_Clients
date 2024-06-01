#from typing import List
import connection_broker
#import device_pooler
#from constants import site
from colorama import Fore, Back, Style

creds = connection_broker.Authenticator()
run = connection_broker.NapalmConnect("lab-casa-acc-sw-1-1.miloandrs.com", creds)

test = run.configure_interface_access('Gi1/0/1', 30, 'Unifi AP')
print(Fore.GREEN + Style.BRIGHT + test + Style.RESET_ALL)