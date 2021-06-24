from calculator import Calculator
import math

class Functional_calculator(Calculator):

    def __init__(self):
        super().__init__() #get all of calculator's methods

    def circle_area(self, r):
        return math.pi*(r*r) #pi r squared

    def square_area(self, x):
        return x*x #x squared

    def triangle_area(self, x, h):
        return 0.5*x*h #half base times height

#cal = Functional_calculator()
#print(cal.circle_area(5))
#print(cal.divide(10, 3))