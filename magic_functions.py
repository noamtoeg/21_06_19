'''
class Person():
    def __init__(self , name = 'default' ):
        self.name = name

noam = Person()
itay = Person()

noam.name= 'Noam'
itay.name = 'Itay'

print(noam.name)
print(itay.name)

class Point():
    def __init__(self , x=0, y=0 ):
        self.x = x
        self.y = y

p1 = Point(3.5,9.30)
print(p1.x)
'''
class MobilePhone():
    def __init__(self, brand , model , price):
        self.brand = brand
        self.model = model
        self.price = price

    def __eq__(self, other):
        if self.model == other.model and\
            self.brand == other.brand:
            return True
        else:
            return False
#    def add(self,other):
#        total = self.price + other.price
#        return total
    def __add__(self, other):
        return self.price + other.price

    def __gt__(self):__(self, other):
        return self.price > other.price

    def __repr__(self):
        return f'Phone({self.brand}, ' \
            f'{self.model})'

Phone1 = MobilePhone('Samsung','S8',500)
Phone2 = MobilePhone('Samsung','A8',370)
Phone3 = MobilePhone('Samsung','S8',550)

print(Phone1 == Phone2)
print(Phone1 == Phone3)
print(Phone3 == Phone2)

print(Phone1 + Phone3)



