#int,string,book, 3 types of data types
class Book:
    def __init__(self,pages):
        self.page=pages
    def __add__(self, other):   #magic method
        return Book(self.page+other.page)
    def __str__(self):
        return str(self.page)
    #def __sub__(self, other):
    #def __truediv__(self, other):
    #def __mul__(self, other):

b1=Book(100)
b2=Book(2)
b3=Book(2)
print(b1+b2+b3) #(will goto add method, by seeing + operator)