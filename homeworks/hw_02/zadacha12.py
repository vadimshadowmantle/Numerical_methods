import math
import mpmath
import numpy as np

mpmath.mp.dps = 50
eps = 2.2e-16


def f_bad(x):
    return math.sqrt(x + 1) - math.sqrt(x)


def f_exact(x):
    x = mpmath.mpf(x)
    return mpmath.sqrt(x + 1) - mpmath.sqrt(x)


xs = [10.0**k for k in range(2, 17)]
errs = []
print("   x    | lg x | ошибка плохого | lg ошибки |  ε·x")
print("--------------------------------------------------------")
for x in xs:
    e = float(abs((mpmath.mpf(f_bad(x)) - f_exact(x)) / f_exact(x)))
    errs.append(e)
    le = f"{math.log10(e):6.1f}" if e > 0 else "  -inf"
    print(f"{x:.0e}  | {math.log10(x):4.0f} | {e:.3e}      | {le}    | {eps * x:.1e}")

# наклон по точкам, где ошибка ещё не насытилась (< 1)
pts = [(math.log10(x), math.log10(e)) for x, e in zip(xs, errs) if 0 < e < 1]
slope = np.polyfit([p[0] for p in pts], [p[1] for p in pts], 1)[0]
print()
print(f"наклон lg(ошибки) от lg(x): {slope:.2f}   (предсказание ε·x даёт наклон 1)")
