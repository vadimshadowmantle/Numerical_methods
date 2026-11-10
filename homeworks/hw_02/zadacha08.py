import math
import mpmath

mpmath.mp.dps = 50


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


print("   x    |  math.log(1 + x)  |  math.log1p(x)    | ошибка log | ошибка log1p")
print("------------------------------------------------------------------------------")
for x in [1e-2, 1e-8, 1e-12, 1e-16]:
    exact = mpmath.log(1 + mpmath.mpf(x))
    bad = math.log(1 + x)
    good = math.log1p(x)
    print(f"{x:.0e}  | {bad:.10e} | {good:.10e} | {rel_err(bad, exact):.2e}   | {rel_err(good, exact):.2e}")

print()
print(math.log1p.__doc__)
