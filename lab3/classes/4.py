# Write the definition of a Point class. Objects from this class should have a

# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

#Point class - class with representation of point in space, using coordinate systen (x,y), common used in geometrical and graphical applications

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.x}, {self.y}"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distances_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return(dx ** 2 + dy ** 2)** 0.5
    
point1 = Point(int(input("Coordinates of first point:\n")), int(input()))
point2 = Point(int(input("Coordinates of second point:\n")), int(input()))

point1.move(int(input("Move first point on:\n")), int(input()))

print(point1.distances_to(point2))