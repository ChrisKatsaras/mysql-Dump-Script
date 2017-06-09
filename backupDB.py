#!/usr/bin/env python
#Script to backup DB
#Run in background using nohup {fullpath} filename &

import subprocess
import datetime
import time
import schedule
import pexpect

def dump():
	print "Dumping DB"
	#Get current datetime
	strtime = str(datetime.datetime.now())
	#Timestamped filename
	filename = time.strftime("%Y-%m-%d-%H:%M:%S")+"DUMP.sql"
	#Command for dumping database. Simply change Alt-Data-Collectin to be whatever DB you require
	command = "mysqldump -h localhost -uroot -p DATABASENAME"

	with open(filename, "w+") as file:
		p = pexpect.spawn(command)
		p.expect("Enter password: ")
		p.sendline("") #Replace with mysql password
		q = p.read()
		p.wait()
		file.write(q)
	return

#############Different upload ratios######
schedule.every().day.at("15:15").do(dump)
#schdule.every.hour.do(dump)
#schedule.every(10).minutes.do(dump)
#schedule.every(60).seconds.do(dump)
##########################################

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute before attempting to call function again