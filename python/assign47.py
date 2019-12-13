import os
path="C:\\Users\\Aishwarya\\Desktop\\Mashupstack\\python"
x=os.listdir(path)
for y in x:
	if ".txt" in y:
		print(y)