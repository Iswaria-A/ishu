x="awesome"
def myfunc():
	print("python is " + x)
myfunc()


x="awesome"
def myfunc():
	global x
	x="fantastic"
myfunc()

print("python is " + x)


z=input("enter the name")
print(z)


a=5
print(type(a))