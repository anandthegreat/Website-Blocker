
import time

from datetime import datetime as dt

website_list=[]
startHr=-1
endHr=-1

hosts_path="/etc/hosts"

redirect="127.0.0.1"

def initialization():
	global website_list,startHr,endHr
	website_list=["www.facebook.com","facebook.com","youtube.com", "www.youtube.com"]	#By default, these websites will be blocked
	userdata=open('blockedwebsites.txt','w+')											#Create a file for new user and add his details
	startHr=int(input('Enter Starting Hour of your Work\n'))
	endHr  =int(input('Enter the Ending Hour of your Work\n'))
	userdata.write(str(startHr)+'\n')
	userdata.write(str(endHr)+'\n')
	print("How many websites you want to block ???")
	number=int(input())
	print("Enter the websites which distracts you! I'll handle it :}")
	for x in range(number):
		web=input()
		website_list.append(web)
	for website in website_list:			#Store these websites in the file.
		userdata.write(website+'\n')


try:
	userdata=open('blockedwebsites.txt','r')		#This text file stores the user details: Starting, Ending hours and blocked websites.
	lines=userdata.readlines()
	startHr=int(lines[0])
	endHr=int(lines[1])
	exclude=0
	for web in lines:
		if(exclude>=2):								#exclude first 2 lines of the file as they contain starting and ending hours
			website_list.append(web)
		else:
			exclude=exclude+1

except FileNotFoundError:
	initialization()								#If the user is running this script for the first time



    
while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,startHr) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,endHr):

        print("Working hours!")

        with open(hosts_path,'r+') as file:
        	
            content=file.read()

            for website in website_list:

               if website in content:

                    pass

               else:
               	file.write(redirect+" "+ website+"\n")

			

    else:

        with open(hosts_path,'r+') as file:

            content=file.readlines()

            file.seek(0)

            for line in content:

                if not any(website in line for website in website_list):

                    file.write(line)

            file.truncate()

        print("Non-working hours!")

    time.sleep(5)