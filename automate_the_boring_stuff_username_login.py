'''Automate the boring stuff'''

'''FLOW CONTROL, username login with multiple tries.'''
import subprocess
import os

title = 'Automate the boring stuff, Ep. 1 flow control'
print(title)
import time
# set username variable value here:
username_1 = 'Jeffrey' 
username_2 = 'Elly'

#login function

def mylogin():
    myName = ''
    count = 0
    while myName != (username_1 or username_2) and count != 5:
        print('What is your name?')
    #must use inside while loop to get count updated value
        count_remaining = 4 - count
        count += 1
        myName = input()
        if myName == (username_1 or username_2):  
            count = 5
            print('Success, ' + myName)
            time.sleep(3)
            print('What would you like to do? Try: Play guess the number')
            if input() == 'Play guess the number':
                import guess_the_number
            elif input == ('Open email'):
                import email_iteration_2
        if myName == username_2:  
            count = 5
            print('Success, ' + myName)
            time.sleep(10)
            break 
    # to convert count remaining into printable format
        str(count_remaining)
        if myName != username_1 and username_2 != myName:
            print('incorrect name! You have ', count_remaining, ' attemps remaining')
print('Do you want to log in?')


def no_startup():
    print('okay? Exiting now.')
#startup function

def startup():
    if input() == "yes":
        mylogin()
    else:
        no_startup()
        time.sleep(3)

#run 

startup()
