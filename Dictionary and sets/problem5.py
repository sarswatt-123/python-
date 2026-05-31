# Can u change the values inside list which is in set 

s={8,7,12,"harry",[1,2]}
s(list.insert(23,4))
print(s)


# We do not put the list into set 
# "Mutable objects cannot be elements of a set."
# If an object can change after creation (like list, dict, set), Python won't allow it inside a set.
