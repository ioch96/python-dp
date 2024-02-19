class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y


points = []

for x in range(1, 11):
    points.append(Point(x, x**2))

for point in points:
    print(f"({point.get_x()}, {point.get_y()})")
