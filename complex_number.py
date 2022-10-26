import math
from math import sqrt


class ComplexNumber(object):

    def __init__(self, real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
        print("{} {} {}i".format(self.real_part,"+" if self.imaginary_part>=0 else "-" ,abs(self.imaginary_part)))

    def conjugate(self):
        return ComplexNumber(self.real_part,-self.imaginary_part)

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part, self.imaginary_part - other.imaginary_part)

    def __mul__(self, other):
        return ComplexNumber((self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part),
                       (self.imaginary_part * other.real_part) + (self.real_part * other.imaginary_part))

    def __truediv__(self, other):
        conj=other.conjugate()
        denominator=other*conj
        #return den
        denominator=denominator.real_part
        numerator=self*conj
        return(ComplexNumber(numerator.real_part/denominator,numerator.imaginary_part/denominator))

    def __abs__(self):
        return math.sqrt(self.real_part**2+self.imaginary_part**2)
    def __eq__(self,other):
        return  self.real_part==other.real_part and self.imaginary_part==other.imaginary_part

class Complex(object):
    def __init__(self, real=0, imag=0):
        self.real_part = real
        self.imaginary_part = imag
        #print("{} {} {}i".format(self.real_part, "+" if self.imaginary_part >= 0 else "-", abs(self.imaginary_part)))

    def __eq__(self, other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
c=ComplexNumber(1,-2)

d=ComplexNumber(1,-2)
print(c+d)

