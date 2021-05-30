# Constructor is defined by __init__ in python
class Point:
    def __init__(self,x,y):  # This is a constructor which will run on Object Creation
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        # We can print attribute values of the same object in across all methods
        print(f'Draw and the value of x is {self.x}')


point1 = Point(10,20)
point1.x = 11  # We can also change attribute value of objects
point1.draw()
# print(point1.x)
