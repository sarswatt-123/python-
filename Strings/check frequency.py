s = input("Enter the string :")
term = input("Enter the term you search for : ")
counter = 0 
for i in s:
    if i == term :
        counter=counter+1
print("The frequency of your term is : ", counter )        