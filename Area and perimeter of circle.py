#Area and perimeter of a circle

class Circle:
    def __init__ (self, radius):
        self.radius = radius
    def  area(self):
        A = 3.142 * self.radius * self.radius
        return A
    def perimeter(self):
        P = 2 * 3.142 * self.radius
        return P

radius = Circle(14)
print(radius.area())
print(radius.perimeter())
    
