class Point:
    def __init__ (self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def status(self):
        a = self.x
        b = self.y
        print(f'x 값 :{a.x},{b.x}')
        print(f'y 값 :{a.y},{b.y}')
        pass
    
    
    def get_area(self):
        a = self.x
        b = self.y
        print(abs(a.x - b.x) * abs(a.y - b.y))

    def get_perimeter(self):
        a = self.x
        b = self.y
        length = abs(a.x - b.x)
        height = abs(a.y - a.y)
        print(2*(length + height))

    def is_square(self):
        a = self.x
        b = self.y
        length = abs(a.x - b.x)
        height = abs(a.y - b.y) 
        if length == height:
            return True
        return False


p1 = Point(4,3)
p2 = Point(1,2)
print(p1.x,p1.y)
print(p2.x,p2.y)
R1 = Rectangle(p1,p2)
R1.status()
print(R1.get_area())
print(R1.get_perimeter())
print(R1.is_square())