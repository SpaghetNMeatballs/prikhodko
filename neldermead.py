from common import Point


def neldermead(
        points: list[Point],
        alpha: float = 1.,
        beta: float = 0.5,
        sigma: float = 2.,
        tolerance=10 ** -6,
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
        xc = Point(coordinates=(0 for i in points[0].coordinates))
        for i in range(1, len(points)):
            xc += points[i]
        xc /= len(points) - 1
        # Отражение
        xr = xc * (1 + alpha) - alpha * xh
        # Оцениваем качество уменьшения функции
        check_list = [xr, xh, xg, xl]
        check_list.sort()
        match check_list.index(xr):
            case 0:
                xe = xc * (1 - sigma) + xr * sigma
                if xe.value < xr:
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
        if max(deltas) <= tolerance:
            flag_end = True
    return points[0]
