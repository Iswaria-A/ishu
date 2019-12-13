import mysql.connector
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="mydatabase")
mycursor=mydb.cursor()
sql="INSERT INTO customers (name,address) VALUES (%s,%s)"
val=("Michael","Highwayvillage,29")
mycursor.execute(sql,val)
mydb.commit()
print("1 record inserted,ID:",mycursor.lastrowid)