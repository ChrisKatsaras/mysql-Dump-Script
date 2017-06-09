# MySQL Dump Script

Script that dumps SQL database on a schedule

## Configuration:
> command = "mysqldump -h localhost -uroot -p DATABASENAME"
Change localhost to desired host
Change DATABASENAME to desired database

> p.sendline("") 
Put your mysql password in between the quotes.


## Running: 

To run in background:
> nohup {fullpath} filename &
