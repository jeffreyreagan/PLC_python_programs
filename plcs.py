from acceptedlist import listlist

import time
import pylogix


Machines_ip= dict({'Cupper1':'172.16.11.31/backplane/4','Cupper2':'172.16.21.31/backplane/4','Cupper3':'172.16.31.31/backplane/4','ss11':'172.16.12.21','ss12':'172.16.14.21','ss13':'172.16.14.31','ss14':'172.16.14.41','ss15':'172.16.15.31','ss16':'172.16.15.41','ss21':'xx.xx.xx.xx','ss22':'xx.xx.xx.xx','ss23':'xx.xx.xx.xx','ss24':'xx.xx.xx.xx','ss25':'xx.xx.xx.xx','ss26':'xx.xx.xx.xx','ss31':'xx.xx.xx.xx','ss32':'xx.xx.xx.xx','ss33':'xx.xx.xx.xx','ss34':'xx.xx.xx.xx','ss35':'xx.xx.xx.xx','ss36':'xx.xx.xx.xx'})

possible_connection_request=''

def search_plc_ips():
    global possible_connection_request
    possible_connection_request=input('List for all or search by machine name ex:Cupper1\n')
    if possible_connection_request in Machines_ip:
        formattedip = Machines_ip.pop(possible_connection_request)
        print(formattedip)
        connection(formattedip)
        return possible_connection_request
        #select_plc_connection()
        
        
    elif possible_connection_request in listlist:
        print(list(Machines_ip.items()))
        search_plc_ips()
    else:
        search_plc_ips()
#def select_plc_connection():
 #   print('You have selected ' + possible_connection_request +'\n') 
  #  while True:
   #     connection()
    #    time.sleep(1)
     #   print("am i making it here")
def connection():
    formatted_ip, slot = connection.split('/')
    plc= pylogix.PLC()
    plc.IpAddress = formatted_ip
    plc.ProcessorSlot = int(slot)
    plc.Open()
    print("am i making it here")
    if plc.comm == True:
        print('connected')
    else:
        print('did not connect')
while True:
    search_plc_ips()
    connection()
