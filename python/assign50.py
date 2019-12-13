import os
import csv
path="C:\\Users\\Aishwarya\\Desktop\\Mashupstack\\python\\new"
x=os.listdir(path)
for y in x:
	if y.endswith('.csv') and not y.endswith('sample.csv'):
		# print(y)
		a=open(y,'r')
		next(a)
		b=a.readlines()
		for g in b:
			c=g.split(',')
			u=c[2]
			print(u)
			csvfile=open("01022017_all.csv","a")
			csvfile.write(u)
			csvfile.write('\n')
			csvfile.close()
			
	    