from common import Point


def function(x, y):
    return x**2 + x * y + y**2 - 6 * x - 9 * y


def neldermead(
    points: list[Point],
    maxiter: int | None,
    alpha: float = 1.0,
    gamma: float = 2,
    rho: float = 0.5,
    sigma=0.5,
    tolerance=10**-3,
) -> Point:
    for i in range(1, len(points)):
        assert (
            points[i].function is points[i - 1].function
        ), "Points have different functions"
        assert len(points[i].coordinates) == len(
            points[i - 1].coordinates
        ), "Points have different dimensions"
    current_iter = 0
    while True:
        current_iter += 1
        if maxiter and current_iter > maxiter:
            break
        points.sort()
        b, g, w = points

        mid = (b + g) / 2

        xr = mid + (mid - w) * alpha
        if b < xr < w:
            w = xr
            points = [b, g, w]
            continue

        if xr < b:
            xe = mid + (mid - w) * gamma
            if xe < xr:
                w = xe
                points = [b, g, w]
                continue
            else:
                w = xr
                points = [b, g, w]
                continue

        xc = mid + (mid - w) * rho
        if xc < w:
            w = xc
            points = [b, g, w]
            continue

        g = b + (g - b) * sigma
        w = b + (w - b) * sigma
        points = [b, g, w]

    return points[0]


if __name__ == "__main__":
    point_a = Point((0, 0), function)
    point_b = Point((1, 0), function)
    point_c = Point((0, 1), function)
    print(neldermead([point_a, point_b, point_c], 20).coordinates)
