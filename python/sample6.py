my_list=[4,5,9,0]
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))


print(my_iter.__next__())
print(my_iter.__next__())