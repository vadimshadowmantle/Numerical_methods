import math
import mpmath

mpmath.mp.dps = 50


def rel_err(approx, exact):
    return float(abs((mpmath.mpf(approx) - exact) / exact))


def lg(e):
    return f"{math.log10(e):6.1f}" if e > 0 else "  -inf"


print("   n    | lg n |  цикл     | lg  |   sum     | lg  |   fsum    | lg")
print("---------------------------------------------------------------------------")
for n in [10**5, 10**6, 10**7]:
    arr = [1 / k for k in range(1, n + 1)]
    exact = mpmath.harmonic(n)          # эталон H_n с 50 знаками

    total = 0.0
    for x in arr:
        total += x

    e1 = rel_err(total, exact)
    e2 = rel_err(sum(arr), exact)
    e3 = rel_err(math.fsum(arr), exact)
    print(f"{n:>8} | {math.log10(n):4.0f} | {e1:.2e} |{lg(e1)} | {e2:.2e} |{lg(e2)} | {e3:.2e} |{lg(e3)}")
