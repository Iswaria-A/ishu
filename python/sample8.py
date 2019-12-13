A=[[1,5,9,7],
    [2,3,6,4],
    [-4,5,8,7]]
B=[[1,2,5,4],
   [6,5,7,3],
   [2,-9,7,-5]]

result=[[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]
for i in range(len(A)):
	for j in range(len(A[0])):
		result[i][j]=A[i][j]+B[i][j]
for r in result:
	print(r)