A=[[1,5,9,6],
    [2,6,-1,8],
    [5,3,7,1]]

print("A=",A)
print("A[1]=",A[1])
print("A[1][2]=",A[1][2])

column=[];
for row in A:
	column.append(row[1])
print("2nd column is",column)


