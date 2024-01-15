

Machines_ip= dict({'Cupper1':'1','Cupper2':'xxx.xx.xx.xx',})

def search_plc_ips():
    answers=input('search by machine name ex:Cupper1\n')
    if answers in Machines_ip:
        print(Machines_ip.pop(answers))
        search_plc_ips()
    else:
        search_plc_ips()
while True:
    search_plc_ips()
    break