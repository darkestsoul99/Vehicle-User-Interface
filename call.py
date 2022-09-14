from get_contactList import *
import os
import time

def call(person):
    phonebook = phoneBook()
    contactList = phonebook.get_phone_no()
    if person in contactList:   #------------------------------ Searching the call book
        ph_no=contactList[person]     #------------------------ Phone no. of the person

        command1='adb shell am start -a android.intent.action.CALL -d tel:'+ph_no  #----cmd. to make call
        command2='adb shell input tap 210 2183'  #--------------- cmd. to tap the speaker button
        print('calling.. '+person)
        os.system(command1)  #----------------------- executing the cmd
        time.sleep(2)
        os.system(command2)
    else:
        print('no saved contact')

person='Dodo'
call(person)