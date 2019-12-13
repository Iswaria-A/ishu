import csv
def file_read(fname):
	txt=open(fname)
	next(txt)
	a=txt.readlines()

	print("3rd row of csv file:",a[2])
	print("First 3 lines of csv file:",a[0],a[1],a[2])
	for x in a:
		y=x.split(',')
		print("2nd column of csv file:",y[1])
file_read("Book1.csv")
