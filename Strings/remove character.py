s = input("Enter the string :")
term = input("Enter the term you remove  for : ")
result =" "
for i in s :
    if i !=term:
        result=result+i
print(result)