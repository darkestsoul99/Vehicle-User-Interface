from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, QTime
from phone_book import *
import os
import time

class PhoneBookWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui = Ui_phoneBook()
        self.ui.setupUi(self)
        self.phone_no = []
        self.name = []
        self.phonebook = {}
        self.get_phone_no()
        self.ui.callButton.clicked.connect(self.callButton)
        self.ui.endCallButton.clicked.connect(self.endCallButton)


    def get_phone_no(self):
        command = 'adb shell content query --uri content://contacts/phones/  --projection display_name:number'
        data = os.popen(command).readlines()  # ------------------------------ getting all contacts data from phone
        count = 0  # -------------------------------------------------- count to replicate row no.
        for i in data:
            i = i.replace('Row: ' + str(count) + ' display_name=', '')  # ------- removing unwanted character
            i = i.replace('number=', '')  # --------------------------------- removing unwanted character
            i = i.split(
                ',')  # --------------------------------- separateing name and phone no. and creating their list

            temp = i[1]  # --------------------------------- index of the phone no. for removing - \n space and +91
            temp = temp.replace('\n', '')
            temp = temp.replace(' ', '')
            temp = temp.replace('-', '')
            temp = temp.replace('+90', '')

            self.phone_no.append(temp)
            self.name.append(i[0])
            phone_no = temp  # ------------------------------------ Phone number
            name = i[0]  # ------------------------------------ name

            self.phonebook[name] = phone_no
            self.ui.listWidget.addItem(name)
            print(phone_no, '\t', name)  # ----------------------------------- printing phone no. and name
            count += 1  # ----------------------------------- changing row no. for next data
        print(self.phone_no)
        print(self.name)

    def callButton(self):
        self.ui.callStatus.setText("Current Call : " + self.name[self.ui.listWidget.currentRow()])
        self.call()

    def endCallButton(self):
        self.ui.callStatus.setText("No current Call")
        os.system('adb shell input keyevent KEYCODE_ENDCALL')

    def call(self):
        string = str(self.phone_no[self.ui.listWidget.currentRow()])
        print(string)
        command1 = 'adb shell am start -a android.intent.action.CALL -d tel:' + '+90' + string  # ----cmd. to make call
        command2 = 'adb shell input tap 210 2183'  # --------------- cmd. to tap the speaker button
        print('calling.. ' + self.name[self.ui.listWidget.currentRow()])
        os.system(command1)  # ----------------------- executing the cmd
        time.sleep(2)
        os.system(command2)
        time.sleep(2)
        os.system('adb shell input tap 864 1857')

