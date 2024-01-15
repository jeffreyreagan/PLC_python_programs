import time
from pylogix import PLC
import msvcrt

plc_ips = ["172.16.14.51"]

#initialize PLC connections
plcs = [PLC() for _ in plc_ips]

for i in range(len(plc_ips)):
    plcs[i].IPAddress = plc_ips[i]
    plcs[i].PLC_Type = "ControlLogix"
try:
    while True:
        for i in range(len(plcs)):
            if plcs[i].IPAddress:
                
                #read tag values for cans until inspection required
                cans_since_inspection = plcs[i].Read("inspection_counter.acc")

                missed_inspection = plcs[i].Read("missed_inspection")

                print(f"PLC {i + 1}: cans_since_inspection = {cans_since_inspection}, missed_inspection = {missed_inspection}")
            
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8')
                if key == 'r':
                    for plc in plcs:
                        plc.Write("",1)
        time.sleep(1)
except KeyboardInterrupt:
    print("program terminated")           
    
