email = input("Enter the email id : ")
password = input("Enter your password")

if (email =="teenasaraswat04@gmail.com") and (password =="1234"):
    print("wecome")
elif (email =="teenasaraswat04@gmail.com") and (password != "1234"):
    print("Incorrect password")
    password=input("Enter password again ")
    if password =="1234":
        print("Welcome finally !!")
    else:
        print("tumse na ho paayega ")    
else :
    print("Incorrect credentials ")    