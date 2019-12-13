character=input("Enter the string:")
x={}
for y in character:
	if y in x:
		x[y]+=1
	else:
		x[y]=1
print(x)