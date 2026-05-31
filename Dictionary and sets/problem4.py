# create an empty dictionary  and alllo 4 freinds they enter theri name as key and add their langiage as values

d={}

name=input("Enter their name :")
lang = input("Enter your language :")
d.update({name:lang})

name=input("Enter their name :")
lang = input("Enter your language :")
d.update({name:lang})

name=input("Enter their name :")         # If the name of two friends are same then the last updated name is shown only in the dict teen
lang = input("Enter your language :")
d.update({name:lang})

name=input("Enter their name :")          # If the values are same then it did not affect on dict 
lang = input("Enter your language :")
d.update({name:lang})

print(d)