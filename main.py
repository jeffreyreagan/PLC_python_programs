import subprocess
import os
import time
import sys
from acceptedlist import acceptedlist,rejectedlist,quitlist,pwdlist

title = 'Main'
# set username variable value here:
username_1 = ['Jeffrey','Jeff','jeff','Jeffrey'] 
username_2 = ['Elly','elly']
username_3 = 'guest'
username_4 = ''

#login function

def mylogin():
    myName = ''
    count = 0
    while myName not in username_1 or myName not in username_2 and count != 5:
        count_remaining = 5 - count
        print('What is your name? You have ' + str(count_remaining) + ' attempts left')
        count += 1
        myName = input()
        if myName in username_1 or myName in username_2:
                count = 5
                print('Success, ' + myName)
                pwdinput=input('\nwhat is your password?\n')
                if pwdinput in pwdlist:
                    applications()
        # to convert count remaining into printable format
        str(count_remaining)
        if myName not in username_1 or myName not in username_2:
            print('Incorrect name! You have ', count_remaining, ' attempts remaining')
            print (myName)

def applications():
            print('What would you like to do? Try: open guess the number, open pong, open email api, open powerflex, open plcs')
            choice = input()
            if choice == 'open guess the number':
                import guess_the_number
                print("imported guess_the_number")
            elif choice == 'open pong':
                import Pong
                print("imported Pong")
            elif choice == 'open email api':
                print('Yes')
                import email_iteration_2
                subprocess.run([sys.executable, "email_iteration_2.py"], check=True)
                print("imported email_iteration_2")
            elif choice == ('open powerflex'):
                import powerflex
            elif choice == ('open plcs'):
                 import plcs
            elif choice in quitlist:
                quit()
            else:
                print('exit confirmed')

def no_startup():
    print('Startup Error; Exiting now.')
    quit()

def startup():
    answer1=input("Continue to login?\n")
    if answer1 in acceptedlist:
        mylogin()
    else:
        time.sleep(3)
        no_startup()

#run 

startup()