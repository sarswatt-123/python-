"""
 There are some methods of list 

                    Python List Method
            Method	                        Description

            append(x)	                    Adds an item to the end of the list
            extend(iterable)	            Adds multiple items from another iterable
            insert(i, x)	                Inserts item at a specific index
            remove(x)	                    Removes first occurrence of value
            pop([i])	                    Removes and returns item at index
            clear()	                        Removes all items
            index(x[, start[, end]])	    Returns index of first occurrence
            count(x)	                    Counts occurrences of a value
            sort()	                        Sorts the list in place
            reverse()	                    Reverses the list
            copy()	                        Returns a shallow copy


"""
l1= [23,56,78,45,67,35,24,89,45]

# Sort function 
l1.sort()
print(l1)

#reverse function 
l1.reverse()
print(l1)

# remove function 
l1.remove(23)
print(l1)

# insert function 
l1.insert(3, 34567)  # put 34567 at the 3rd index of the list 
print(l1)

l2= [45,655,678,345,34,344,98]
print(l2.pop(2))
print(l2)