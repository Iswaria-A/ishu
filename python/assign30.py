def file_read(fname):
	content_array =[]
	with open(fname) as f:
		for lines in f:
			content_array.append(lines)
			print(content_array)
file_read("text1.txt")
