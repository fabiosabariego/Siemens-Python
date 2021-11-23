from tkinter import ttk
from tkinter import *
import time
import snap7

IP = '192.168.1.10'
RACK = 0
SLOT = 1

DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 259

plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cpu_info()
print(f'Module Type: {plc_info.ModuleTypeName}')

state = plc.get_cpu_state()
print(f'State:{state}')

db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)

product_name = db[0:256].decode('UTF-8').strip('\x00')
print(f'PRODUCT NAME: {product_name}')

product_value = int.from_bytes(db[256:258], byteorder='big')
print(f'PRODUCT VALUE: {product_value}')

product_status = bool(db[258])
print(product_status)

time.sleep(15)