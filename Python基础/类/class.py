class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")


point = Point(10, 5)
point_x = point.x
point_y = point.y
print(point_x)
print(point_y)
point.move()
