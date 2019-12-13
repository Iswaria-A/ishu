import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")
mycursor=mydb.cursor()
sql="UPDATE customers SET address='Cannyon 123' WHERE address='Highwayvillage,29'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")