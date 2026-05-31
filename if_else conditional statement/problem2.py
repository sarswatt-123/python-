"""
 2. Write a program to find out whether a student has passed or failed if it requires a total of
    40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
    input from the user.

"""
hindi  =    int(input("Enter marks hindi :"))
english=    int(input("Enter  marks english :"))
maths  =    int(input("Enter marks maths "))
percentage = (hindi + english +maths) /300 *100

if(percentage>40 and hindi>=33 and english>=33 and maths>=33):
    print("student is pass")
    print("Your percentage is :",percentage)
else:
    print("Student is fail")
    print("try next year :",percentage)   