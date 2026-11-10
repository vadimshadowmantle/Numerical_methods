import math
import mpmath

mpmath.mp.dps = 50


def f_bad(x):
    return (1 - math.cos(x)) / x**2


def f_good(x):
    return 2 * math.sin(x / 2)**2 / x**2


def f_exact(x):
    x = mpmath.mpf(x)
    return (1 - mpmath.cos(x)) / x**2


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


print("   x    | lg x | ошибка плохого | lg ошибки | ошибка хорошего | lg ошибки")
print("--------------------------------------------------------------------------")
for x in [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]:
    ex = f_exact(x)
    eb = rel_err(f_bad(x), ex)
    eg = rel_err(f_good(x), ex)
    lb = f"{math.log10(eb):6.1f}" if eb > 0 else "  -inf"
    lg = f"{math.log10(eg):6.1f}" if eg > 0 else "  -inf"
    flag = "  > 1%" if eb > 0.01 else ""
    print(f"{x:.0e} | {math.log10(x):4.0f} | {eb:.3e}      | {lb}    | {eg:.3e}       | {lg}{flag}")
