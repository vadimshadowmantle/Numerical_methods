import math
import mpmath

mpmath.mp.dps = 50


def f_bad(x):
    return math.log(1 + x)


def f_good(x):
    return math.log1p(x)


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


print("   x    |   плохой      |   хороший     |    эталон     | ош. плохого | ош. хорошего")
print("--------------------------------------------------------------------------------------")
for k in range(1, 17):
    x = 10.0**-k
    ex = mpmath.log(1 + mpmath.mpf(x))
    b = f_bad(x)
    g = f_good(x)
    print(f"{x:.0e}  | {b:.6e}  | {g:.6e}  | {mpmath.nstr(ex, 7):<13} | "
          f"{rel_err(b, ex):.2e}    | {rel_err(g, ex):.2e}")
