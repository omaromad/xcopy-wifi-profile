import subprocess
import os
os.system("mkdir wifi")
info = subprocess.run(["powershell" , "netsh wlan export profile key=clear folder=wifi"],shell=True, capture_output=True)
print (info)
