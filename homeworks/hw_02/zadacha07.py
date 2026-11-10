import math
import mpmath
import numpy as np

mpmath.mp.dps = 50

def f_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)

def f_good(x):
    return 1 / (math.sqrt(x + 1) + math.sqrt(x))

def f_exact(x):
    x = mpmath.mpf(x)
    return mpmath.sqrt(x + 1) - mpmath.sqrt(x)

def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))

xs = [1e4, 1e8, 1e12, 1e14, 1e16]
errs = []
print("   x    | ошибка плохого | ошибка хорошего")
print("-------------------------------------------")
for x in xs:
    ex = f_exact(x)
    eb = rel_err(f_bad(x), ex)
    eg = rel_err(f_good(x), ex)
    errs.append(eb)
    print(f"{x:.0e}  | {eb:.3e}      | {eg:.3e}")

pts = [(math.log10(x), math.log10(e)) for x, e in zip(xs, errs) if 0 < e < 1]
slope = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)[0]
print()
print(f"ошибка плохого ~ x^{slope:.2f}")