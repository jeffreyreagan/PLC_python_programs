'''PLC CONNECT'''
import time
import pylogix
from plcs import possible_connection_request

user_selected_ip= possible_connection_request

def connection():
    plc= pylogix.PLC()
    plc.IpAddress = user_selected_ip
    plc.Open()
    print(plc.IPAddress)
    if plc.conn == True:
        print('connected')
    else:
        print('did not connect')
