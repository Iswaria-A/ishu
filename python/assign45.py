def sum_arr(arr,size):
 if (size==0):
  return 0
 else:
  return arr[size-1]+sum_arr(arr,size-1)
n=int(input("Enter the number of elements for the list:"))
a=[]
for i in range(0,n):
	element=int(input("Enter the elements:"))
	a.append(element)
print("The list is:")
print(a)
print("Sum of items in the list:")
b=sum_arr(a,n)
print(b)