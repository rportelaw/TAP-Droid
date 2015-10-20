import os
import urllib.request
import random
import glob
import time

print (30 * '-')
print ("1. Record")
print ("2. Convert")
print ("3. Run")
print (30 * '-')

while True:

    ## Get input ###
    choice = input('Enter: ')

    ### Convert string to int type ##
    try:
        choice = int(choice)
    except:
        choice = None

    ### Take action as per selected menu-option ###
    if choice == 1:
            print ("Recording")
            print ("Please unplug your phone from USB port when you finish your tapping routine")
            print ("Yep, you have to do that :(")
            os.system("adb shell getevent -l | grep 'POSITION' > myinput.sh")
    elif choice == 2:
            print ("Enter a file name for script you want to record:")
            filename = input()
            cmd = "python3 convert.py > "+filename+".sh"
            print ("Now magic hapens!")
            os.system(cmd)
            os.remove("myinput.sh")
    elif choice == 3:
            print ("Enter a name of file you want to run:")
            filename = input()
            cmd1 = "sh "+filename+".sh"
            print ("Aaaaand RUN!")
            os.system(cmd1)
    else:    ## default ##
            print ("U mad bro? You can only type 1, 2 and 3 _shrugs_")


