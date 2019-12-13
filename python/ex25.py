def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y
print("Select operations:")
print("1.Add")
print("2.Subtrat")
print("3.Multily")
print("4.Divide")
choice=input("Enter choice(1/2/3/4):")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice=='1':
	print(num1,"+",num2,"is",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"is",subtract(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"is",multiply(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"is",divide(num1,num2))
else:
	print("Invalid input")