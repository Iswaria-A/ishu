import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")
mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE customers(name varchar(100),address varchar(100))")