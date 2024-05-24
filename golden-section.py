import math

gr = (math.sqrt(5) + 1) / 2


def gss(f, a, b, tol=1e-5):
    while abs(b - a) > tol:
        c = b - (b - a) / gr
        d = a + (b - a) / gr
        if f(c) < f(d):
            b = d
        else:
            a = c

    return (b + a) / 2


if __name__ == "__main__":
    f = lambda x: (x - 2) ** 2
    x = gss(f, 1, 5)
    print(f"{x}")
