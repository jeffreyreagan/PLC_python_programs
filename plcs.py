

Machines_ip= dict({'Cupper1':'1','Cupper2':'xxx.xx.xx.xx','Cupper3':'xx.xx.xx.xx','ss11':'xx.xx.xx.xx','ss12':'xx.xx.xx.xx','ss13':'xx.xx.xx.xx','ss14':'xx.xx.xx.xx','ss15':'xx.xx.xx.xx','ss16':'xx.xx.xx.xx','ss21':'xx.xx.xx.xx','ss22':'xx.xx.xx.xx','ss23':'xx.xx.xx.xx','ss24':'xx.xx.xx.xx','ss25':'xx.xx.xx.xx','ss26':'xx.xx.xx.xx','ss31':'xx.xx.xx.xx','ss32':'xx.xx.xx.xx','ss33':'xx.xx.xx.xx','ss34':'xx.xx.xx.xx','ss35':'xx.xx.xx.xx','ss36':'xx.xx.xx.xx'})


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