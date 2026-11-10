import math
import mpmath
import numpy as np

mpmath.mp.dps = 50

def f_bad(x):
    return (1 - math.cos(x)) / x**2


def f_bad32(x):
    x = np.float32(x)
    return (np.float32(1) - np.cos(x)) / (x * x)

def f_good(x):
    return 2 * math.sin(x / 2)**2 / x**2

def f_exact(x):
    x = mpmath.mpf(x)
    return (1 - mpmath.cos(x)) / x**2

def rel_err(approx, exact):
    return float(abs((mpmath.mpf(float(approx)) - exact) / exact))

print("(а) меняем x, алгоритм плохой, float64")
for x in [1e-2, 1e-4, 1e-6, 1e-8]:
    print(f"   x = {x:.0e}   ошибка = {rel_err(f_bad(x), f_exact(x)):.2e}")

x = 1e-2
print()
print(f"(б) x = {x:.0e}, алгоритм плохой")
print(f"   float64   ошибка = {rel_err(f_bad(x), f_exact(x)):.2e}")
print(f"   float32   ошибка = {rel_err(f_bad32(x), f_exact(x)):.2e}")

x = 1e-6
print()
print(f"(в) x = {x:.0e}, float64")
print(f"   плохой    ошибка = {rel_err(f_bad(x), f_exact(x)):.2e}")
print(f"   хороший   ошибка = {rel_err(f_good(x), f_exact(x)):.2e}")