class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    # def __init__(self,Point1,Point2):
    #     self.Point1 = Point1
    #     self.Point2 = Point2
    
    # Point1_x = Point1.x
    # Point1_y = Point1.y
    # Point2_x = Point2.x
    # Point2_y = Point2.y
    def status(self):
        a = self.x
        b = self.y
        print(f'x 값 :{a.x},{b.x}')
        print(f'y 값 :{a.y},{b.y}')
        pass
    
    
    # def get_area(self):
    #     Point1_x = self.x
    #     Point1_y = self.y
    #     Point2_x = self.x
    #     Point2_y = self.Point2.y
    #     print(abs(Point2_x - Point1_x) * abs(Point2_y - Point1_y))

    # def get_perimeter(self):
    #     Point1_x = self.Point1.x
    #     Point1_y = self.Point1.y
    #     Point2_x = self.Point2.x
    #     Point2_y = self.Point2.y
    #     length = abs(Point2_x - Point1_x)
    #     height = abs(Point2_y - Point1_y)
    #     print(2*(length + height))

    # def is_square(self):
    #     Point1_x = self.Point1.x
    #     Point1_y = self.Point1.y
    #     Point2_x = self.Point2.x
    #     Point2_y = self.Point2.y
    #     length = abs(Point2_x - Point1_x)
    #     height = abs(Point2_y - Point1_y) 
    #     if length == height:
    #         return True
    #     return False


p1 = Point(4,3)
p2 = Point(1,2)
print(p1.x,p1.y)
print(p2.x,p2.y)
R1 = Rectangle(p1,p2)
R1.status()
# print(R1.get_area())
# print(R1.get_perimeter())
# print(R1.is_square())