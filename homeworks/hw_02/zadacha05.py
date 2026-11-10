import math
import mpmath

mpmath.mp.dps = 50


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


a, c = 1.0, 1.0
print("    b    |  ошибка плохого  | ошибка хорошего")
print("---------------------------------------------")
for b in [1e4, 1e8, 1e12]:
    d = math.sqrt(b * b - 4 * a * c)
    x_bad = (-b + d) / (2 * a)
    x_good = 2 * c / (-b - d)

    B = mpmath.mpf(b)
    exact = 2 * c / (-B - mpmath.sqrt(B * B - 4 * a * c))
    print(f"{b:.0e}   | {rel_err(x_bad, exact):.3e}        | {rel_err(x_good, exact):.3e}")
