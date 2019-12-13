def file_lengthy(fname):
	with open(fname) as f:
		for i,l in enumerate(f):
			pass
		return i+1
print("Number of lines in file:",file_lengthy("text.txt"))