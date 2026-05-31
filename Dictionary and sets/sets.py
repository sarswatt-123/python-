s={1,2,3,4,4}  
print(s,type(s))

a=set()
print(type(a))

#Methods of sets 

a1= {1,2,3,45,6}
a2= {34.76,76,78,45}        # intersection and union
print(a1.union(a2))

s.add(56)            # add method 
print(s)

print(s.issubset({1,2,3,4,5,6,4,56,6}))       #issubset 
