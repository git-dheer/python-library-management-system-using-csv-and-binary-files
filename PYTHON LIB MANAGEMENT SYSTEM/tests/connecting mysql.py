import mysql.connector
mypass = "root" #use your own password
mydatabase="db" #The database name
con = mysql.connector.connect (host="localhost",user="root",password=mypass,database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor