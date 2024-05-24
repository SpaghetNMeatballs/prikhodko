import numpy as np
from scipy.optimize import fmin as Nelder_MID
# v-prikhodko@mail.ru

def P(x, r, equations, inequalities):
    sum_equations = np.sum([g(x) for g in equations]) ** 2
    array_g_x_inequalities = np.vectorize(
        lambda g, x: g(x),
        signature="(),(n)->()",
    )(inequalities, x)
    array_g_x_inequalities[array_g_x_inequalities < 0] = 0
    sum_inequalities = (array_g_x_inequalities**2).sum()
    ans = r / 2 * (sum_equations + sum_inequalities)
    return ans


def step2(x, r, bind_P, f):
    F_Rm = lambda x, f: Nelder_MID(f, x)
    F = lambda x: f(x) + bind_P(x, r)
    x = F_Rm(x, F)
    return (x, F(x))


def penalty_method(r, C, f, e, equations, inequalities):
    bind_P = lambda x, r: P(x, r, equations, inequalities)
    x = [0, 0]
    x = np.array(x, dtype=float)
    x, F_x = step2(x, r, bind_P, f)
    r = r * C
    temp_val = abs(bind_P(x, r))
    while temp_val > e:
        print(r, x[0], x[1], F_x, bind_P(x, r), f(x), sep="\t")
        x, F_x = step2(x, r, bind_P, f)
        r = r * C
    return x


if __name__ == "__main__":
    f = lambda x: x[0]**2+x[1]**2-3*x[0]
    equations = []
    inequalities = [
        lambda x: -2*x[0] + x[1]**2
    ]
    r = 1
    C = 10
    e = 0.01
    ans = penalty_method(
        r,
        C,
        f,
        e,
        equations,
        inequalities,
    )
    print(ans)
