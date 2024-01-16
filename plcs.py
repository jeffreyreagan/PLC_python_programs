from acceptedlist import listlist,acceptedlist,rejectedlist,quitlist
import time
import pylogix

Machines_ip= dict({'Cupper1':'172.16.11.31/backplane/4','Cupper2':'172.16.21.31/backplane/4','Cupper3':'172.16.31.31/backplane/4','ss11':'172.16.12.21','ss12':'172.16.14.21','ss13':'172.16.14.31/2','ss14':'172.16.14.41','ss15':'172.16.15.31','ss16':'172.16.15.41','ss21':'xx.xx.xx.xx','ss22':'xx.xx.xx.xx','ss23':'xx.xx.xx.xx','ss24':'xx.xx.xx.xx','ss25':'xx.xx.xx.xx','ss26':'xx.xx.xx.xx','ss31':'xx.xx.xx.xx','ss32':'xx.xx.xx.xx','ss33':'xx.xx.xx.xx','ss34':'xx.xx.xx.xx','ss35':'xx.xx.xx.xx','ss36':'xx.xx.xx.22'})

possible_connection_request=''

def search_plc_ips():
    global possible_connection_request
    global formattedip
    possible_connection_request=input('List for all or search by machine name ex:Cupper1\n')
    if possible_connection_request in Machines_ip:
        formattedip = Machines_ip.pop(possible_connection_request)
        print(formattedip)
        return possible_connection_request
    elif possible_connection_request in listlist:
        print(list(Machines_ip.items()))
        search_plc_ips()
    else:
        search_plc_ips()

def connection():
    parts = formattedip.split('/')
    if len(parts) == 3:
        formatted_ip, backplane, slot = formattedip.split('/')
        print("Formatted ip:",formatted_ip,"Slot #:", slot)
    elif len(parts) == 1:
        formatted_ip = formattedip.split('/')
        print("Formatted ip:",formatted_ip)
    else:
        formatted_ip,slot = formattedip.split('/')
        print('Formatted ip:',formatted_ip,'slot:',slot)

def restart_menu_quit():
    restart_quit_request=input('Would you like to restart(Y), menu(menu), or quit? \n')
    if restart_quit_request in acceptedlist:
        print('restarting')
        search_plc_ips()
        connection()
        restart_menu_quit()
    elif restart_quit_request == 'menu':
        import main
    elif restart_quit_request in quitlist:
        print('quitting')
        quit()
    else:
        restart_menu_quit()
while True:
    search_plc_ips()
    connection()
    restart_menu_quit()

#issue removing the dictionary keys each time they are called

'''    #plc= pylogix.PLC()
    
    #plc.IpAddress = formatted_ip
    #plc.ProcessorSlot = int(slot)
    #plc.Open()
    #print("am i making it here")
    #if plc.comm == True:
      #  print('connected')
    #else:
     #   print('did not connect')'''
'''phased out "cleaned up" code
#def select_plc_connection():
 #   print('You have selected ' + possible_connection_request +'\n') 
  #  while True:
   #     connection()
    #    time.sleep(1)
     #   print("am i making it here")'''