"""Concept of tuples 

It  is also a hetrogeneous data structure that is used to store the collections of data but it is 
a immutable type we cannot change the items from it .
  
"""
a= ()
print(type(a))

b= (1,)   # if i can only dtore the one item in tuples 
print(type(b))

c= (23,45,4,"teena" , "riya" , 567 , 4577 )
print(c)



"""  ---------------------------------Methods of tuples---------------------------------------- """

t=(34,56,356,67,832,56,5677,332)


no=t.count(56)
print(no)


print(t.index(34))

print(len(t))
