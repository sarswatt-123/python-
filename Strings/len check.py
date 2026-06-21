#           How to check the length of the string without using len fucntion 

str = input("Enter your string : ")
counter =0
for i in str:
    counter=counter+1
print("The len of the string is ",counter)