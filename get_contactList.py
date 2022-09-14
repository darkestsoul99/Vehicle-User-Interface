
import os

class phoneBook():
	def __init__(self):
		self.phonebook = {}
		self.get_phone_no()


	def get_phone_no(self):
		command = 'adb shell content query --uri content://contacts/phones/  --projection display_name:number'
		data = os.popen(command).readlines()  # ------------------------------ getting all contacts data from phone
		count=0        #-------------------------------------------------- count to replicate row no.
		for i in data:
			i=i.replace('Row: '+str(count)+' display_name=','')   #------- removing unwanted character
			i=i.replace('number=','')   #--------------------------------- removing unwanted character
			i=i.split(',')              #--------------------------------- separateing name and phone no. and creating their list

			temp=i[1]                   #--------------------------------- index of the phone no. for removing - \n space and +91
			temp=temp.replace('\n','')
			temp=temp.replace(' ','')
			temp=temp.replace('-','')
			temp=temp.replace('+91','')

			phone_no=temp            #------------------------------------ Phone number
			name=i[0]                #------------------------------------ name

			self.phonebook[name]=phone_no

			print(phone_no,'\t',name) #----------------------------------- printing phone no. and name
			count+=1                  #----------------------------------- changing row no. for next data

		return self.phonebook

	def find_no(self, name=''):
		if name!='':
			if name in self.phonebook:
				return self.phonebook[name]
			else:
				return 'no contact'
		else:
			pass