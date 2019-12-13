nterms=int(input("How many terms to be entered:"))
n1=0
n2=1
count=2
if nterms < 0:
	print("Enter a positive number")
elif nterms==0:
	print("Fibanocci series")
	print(n1)
else:
	print("Fibanocci series")
	print(n1,',',n2,end=',')
	while count < nterms:
		nth=n1+n2
		print(nth,end=',')
		n1=n2
		n2=nth
		count+=1