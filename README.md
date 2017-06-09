# MySQL Dump Script

Script that dumps SQL database on a schedule

![alt tag](https://media.giphy.com/media/5YO4km322zuNy/giphy.gif) 


## Configuration:
> command = "mysqldump -h localhost -uroot -p DATABASENAME"
Change localhost to desired host
Change DATABASENAME to desired database

> p.sendline("") 
Put your mysql password in between the quotes.


## Running: 

To run in background:
> nohup {fullpath} filename &
