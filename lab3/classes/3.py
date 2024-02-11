#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. 
#The Rectangle class has a method which can compute the area.

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        print("Area of rectangle:", self.length * self.width)
        
rect = Rectangle(int(input("Length: ")), int(input("Width: ")))
rect.area()

#done