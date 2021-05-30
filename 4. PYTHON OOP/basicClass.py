class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()
point1.x = 10  # We are adding attribute to a object externally. We will do it better using Constructor
point1.draw()
print(point1.x)
