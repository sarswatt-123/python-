dict={"teena":20, 
              "sumit":45,
              "vivek":23,
              "fruit":"mango",
              "subject":"maths"
              }


# ---------------------------Methods of Dictionary----------------------------------
print(dict)
print(dict.items())
print(dict.keys())
print(dict.values())

dict.update({"garima":45})
print(dict)


#dict.clear()
#print(dict)
#print(dict.items())

print(dict.pop("fruit"))   

print(dict.get("Harry"))       # it will return the none value if item is not in the dict 
print(dict["Harry"])           # it will through the error if itm is not in the dict 