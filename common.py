class Point:
    coordinates: tuple[float]
    value: float
    function: callable

    def __init__(self, coordinates: tuple, function: callable):
        self.coordinates = coordinates
        self.function = function
        self.value = self.function(*self.coordinates)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        if type(other) is Point:
            assert self.function is other.function, "Points have different functions"
            assert len(self.coordinates) == len(other.coordinates), "Points have different dimensions"
            new_coords = tuple(self.coordinates[i] + other.coordinates[i] for i in range(len(self.coordinates)))
            return Point(coordinates=new_coords, function=self.function)
        else:
            raise Exception("Wrong type passed")

    def __mul__(self, other):
        if type(other) is float or type(other) is int:
            return Point(tuple(i * other for i in self.coordinates), self.function)
        else:
            raise Exception("Wrong type passed")

    def __sub__(self, other):
        if type(other) is Point:
            assert self.function is other.function, "Points have different functions"
            assert len(self.coordinates) == len(other.coordinates), "Points have different dimensions"
            new_coords = tuple(self.coordinates[i] - other.coordinates[i] for i in range(len(self.coordinates)))
            return Point(coordinates=new_coords, function=self.function)
        else:
            raise Exception("Wrong type passed")

    def __truediv__(self, other):
        if type(other) is float or type(other) is int:
            new_coords = tuple(self.coordinates[i] / other for i in range(len(self.coordinates)))
            return Point(coordinates=new_coords, function=self.function)
        else:
            raise Exception(f"Wrong type passed: {type(other)}")

    def len_calc(self, other):
        if type(other) is Point:
            assert self.function is other.function, "Points have different functions"
            assert len(self.coordinates) == len(other.coordinates), "Points have different dimensions"
            result = 0
            for i in range(len(self.coordinates)):
                result += self.coordinates[i] - other.coordinates[i]
            return result
        else:
            raise Exception("Wrong type passed")


def function(x, y):
    return x ** 2 + x * y + y ** 2 - 6 * x - 9 * y


if __name__ == '__main__':
    b = Point((0, 1), function)
    g = Point((1, 0), function)
    w = Point((0, 0), function)
    mid = (b + g) / 2
    xr = mid * 2 - w
    xe = xr * 2 - mid
    print(xe.coordinates)
