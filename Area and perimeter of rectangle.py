#Area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        #Compute the area of the rectangle.
        return self.length * self.width

    def compute_perimeter(self):
        #Compute the perimeter of the rectangle.
        return 2 * (self.length + self.width)

    
if __name__ == "__main__":
    # Create a rectangle with length 5 and width 3
    rectangle1 = Rectangle(5, 3)

    # Compute and print the area of the rectangle
    area = rectangle1.compute_area()
    print("Area of the rectangle:", area)

    # Compute and print the perimeter of the rectangle
    perimeter = rectangle1.compute_perimeter()
    print("Perimeter of the rectangle:", perimeter)
