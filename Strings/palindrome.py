# How to check a given string is palindrome or not 

s=input("Enter your string :")
if s==s[::-1]:
    print("yes your string is palindrome")
else:
    print("Not palindrome ")