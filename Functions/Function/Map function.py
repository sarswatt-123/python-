# square the items of a list
a=list(map(lambda x : x**2 , [1,2,3,4,5]))
print(a)



# odd/even labelling of list items
b= list(map(lambda x: "even" if x%2==0 else "odd" , [1,2,3,4,5]))
print(b)




# fetch names from a list of dict
users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

d=list(map(lambda users:users["gender"],users))
print(d)