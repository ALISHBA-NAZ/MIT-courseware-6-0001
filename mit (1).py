import math
# problem set 0
x = int(input("enter any number :"))
y = int(input("enter any number :"))
result = x**y
print("x raised to the power of y:", result)
log = math.log2(x)
z=int(log)
print("log base 2 of x :", z)

# new lecture

# Function calls
def add(x ,y):
    return x+y
 
def mult(x, y):
    print(x*y)

add(1, 2)
print(add(2, 3))
mult(3, 4)
print(mult(4, 5))

#Function as arguments
def sq(func, x):
    y = x**2
    return func(y)

def f(x):
    return x**2

calc = sq(f, 2)
print(calc)

from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def color(self):
        print("white")

class suzuki(car):
    pass

class TATA(car):
    def mileage(self):
        print("mileage is 20kmph")
    
class honda(car):
    def mileage(self):
        print("mileage is 25kmph")

c1 = car()
m1 = suzuki()
d1 = TATA()
d1,mileage


class CMD(ABC):
    def cd(self,dir):
        pass

    def exit(self):
        pass

class child(CMD)


