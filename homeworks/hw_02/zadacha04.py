import math
import mpmath

mpmath.mp.dps = 50



def r_bad(x, y):
    return math.sqrt(x * x + y * y)


def r_good(x, y):
    m = max(abs(x), abs(y))
    if m == 0:
        return 0.0
    return m * math.sqrt((x / m)**2 + (y / m)**2)


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


print("   x    |   плохо    |  хорошо    |  ошибка плохого | ошибка хорошего")
print("----------------------------------------------------------------------")
for x in [1e-200, 1e-160, 1e-100, 1.0, 1e100, 1e160, 1e200]:
    exact = mpmath.sqrt(mpmath.mpf(x)**2 + mpmath.mpf(x)**2)
    b = r_bad(x, x)
    g = r_good(x, x)
    print(f"{x:.0e} | {b:.3e}  | {g:.3e}  | {rel_err(b, exact):.2e}        | {rel_err(g, exact):.2e}")
