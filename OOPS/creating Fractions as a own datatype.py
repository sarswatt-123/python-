# cretinf fraction as a data type 
class Fraction :
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __add__(self, other):
        new_num=self.num*other.den + other.num * self.den
        new_den=self.den * other.den

        return "{}/{}".format(new_num,new_den)
    

    def __sub__(self, other):
        new_num=self.num*other.den - other.num * self.den
        new_den=self.den * other.den

        return "{}/{}".format(new_num,new_den)
    

    def __mul__(self, other):
        new_num=self.num*other.num 
        new_den=self.den * other.den

        return "{}/{}".format(new_num,new_den)
    

    def __truediv__(self, other):
        new_num=self.num*other.den 
        new_den=self.den * other.num

        return "{}/{}".format(new_num,new_den)
    
    def convert_to_decimal(self):
        return self.num/self.den
    


    def __str__(self):  # Magic methods 
        return "{}/{}".format(self.num,self.den)

fr1=Fraction(3,4)    
fr2=Fraction(1,2)
fr1.convert_to_decimal()
# 3/4
# whenever we want to print the object __str__ code will automatically execute 
print(fr1)
print(fr2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr2 * fr2)
print(fr1 / fr2)
