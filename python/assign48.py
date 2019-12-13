import os
path="C:\\Users\\Aishwarya\\Desktop\\Mashupstack\\python\\text files"
x=os.listdir(path)
for y in x:
 a=y[2:4]
 array={"01":"Jan","02":"Feb","03":"March","04":"April","05":"May","06":"June","07":"July","08":"Aug","09":"Sept","10":"Oct","11":"Nov","12":"Dec"}
 for z in array:
 	if z in a:
 		print(array[z]+"-"+y)