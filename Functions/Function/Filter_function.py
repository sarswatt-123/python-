# filter out those number which is greater than 5 

a=list(filter(lambda x: x>5,[1,5,6,7,89,9,33,22,2,3,2]))
print(a)



# filter those fruits form the list whose name starts with a 

b=list(filter(lambda x :x.startswith("a"),['apple',"mango",'banana','annanaas']))
print(b)




# using reduce function to find the sum of numbers in the list 
import functools
c=functools.reduce(lambda x,y:x+y,[1,2,3,4,5])
print(c)





# find min number in the list 
import functools
d=functools.reduce(lambda x,y : x if x<y else y,[23,45,67,43,45])
print(d)