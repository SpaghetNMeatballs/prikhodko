from common import Point


def function(x, y):
    return x ** 2 + x * y + y ** 2 - 6 * x - 9 * y


def neldermead(
        points: list[Point],
        alpha: float = 1.,
        beta: float = 0.5,
        sigma: float = 2.,
        tolerance=10 ** -3,
) -> Point:
    for i in range(1, len(points)):
        assert points[i].function is points[i - 1].function, "Points have different functions"
        assert len(points[i].coordinates) == len(points[i - 1].coordinates), "Points have different dimensions"
    flag_end = False
    while not flag_end:
        # Подготовка и сортировка
        points.sort()
        xh, xg, xl = points[:3]
        # Находим центр тяжести точек
        xc = Point(coordinates=tuple(0 for i in points[0].coordinates), function=xh.function)
        for i in range(1, len(points)):
            try:
                xc += points[i]
            except:
                pass
        xc /= len(points) - 1
        # Отражение
        xr = xc * (1 + alpha) - xh * alpha
        # Оцениваем качество уменьшения функции
        check_list = [xr, xh, xg, xl]
        check_list.sort()
        match check_list.index(xr):
            case 0:
                xe = xc * (1 - sigma) + xr * sigma
                if xe < xr:
                    xh = xe
                else:
                    xh = xr
                flag = False
            case 1:
                xh = xr
                flag = False
            case 2:
                xh, xr = xr, xh
                flag = True
            case 3:
                flag = True
        # Сжатие
        if flag:
            xs = xh * beta + xc * (1 - beta)
            if xs < xh:
                xh = xs
            # Глобальное сжатие
            else:
                xh = xh + (xh - xl) / 2
                xg = xg + (xg - xl) / 2
        # Проверка сходимости
        deltas = [abs(xh.len_calc(xg)), abs(xh.len_calc(xl)), abs(xg.len_calc(xl))]
        cur_max = max(deltas)
        if cur_max <= tolerance:
            flag_end = True
        points = [xh, xg, xl]
    return points[0]


if __name__ == '__main__':
    a = Point((0, 0), function)
    b = Point((1, 0), function)
    c = Point((0, 1), function)
    print(neldermead([a, b, c]))
