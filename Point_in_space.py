import math
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def distance(self):
        z = round(math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2), 2)
        print(z)
point = Point(2, 4, 6, 8)
point.distance()