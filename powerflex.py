from acceptedlist import acceptedlist,rejectedlist,quitlist
def powerflexfaultlookup():
    powerflexcall = input("Powerflex 525 fault list. Yes to enter, anything else to go back\n")
    if powerflexcall in acceptedlist:
        with open("525faultlist.txt", "r", encoding="utf-8") as list:
            for line in list:
                print(line.strip()) 
        menuanswer1=input("Would you like to go to menu? Y or N\n")
        if menuanswer1 in acceptedlist:
            startup()
        if input in rejectedlist:
            exit()
    else:
        print('error incorrect instruction recieved from user, going back')
        startup()
def powerflexfaultlookup2():
    powerflexcall2 = input("Powerflex 755 fault list. Yes to enter\n")
    if powerflexcall2 in acceptedlist:
        with open("755faultlist.txt","r", encoding="utf-8") as list:
            for line in list:
                print(line.strip())
                print("Successfully imported the powerflex 755 fault list")
        menuanswer1=input("Would you like to go to menu? Y or N\n")        
        if menuanswer1 in acceptedlist:
            startup()
        if input in rejectedlist:
            exit()
def startup():
    while True:
        startup=input("Powerflex troubleshooting script.\nF to list 525 faults\nF2 to list 755 faults\n")
        if startup == "F" or startup == "f":
            powerflexfaultlookup()
            break
        if startup == "F2" or startup == "f2":
            powerflexfaultlookup2()
            break
        if startup in quitlist:
            break
        else:
            print("wrong choice selected, restarting")
            startup
startup()
