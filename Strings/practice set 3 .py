# How to detect the double space in any string 

letter = "Hello Welcome to the C  programming "

print(letter.find("  "))


# is doublespace is present they give the index number of the double space 

# but if double space is not present then they will give -1 

print(letter.replace(" ", "  "))


# ye hamesha nayi string banake usko print krega purani jo original string hai usko changenhi krega agar hum usko print karayenge to 
# wo as it is print hogi   isko immutability of string         khte hai   