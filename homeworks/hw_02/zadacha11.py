import math
import mpmath

mpmath.mp.dps = 50

a, b, c = 1.0, 1e8, 1.0
d = math.sqrt(b * b - 4 * a * c)

x1 = (-b + d) / (2 * a)
x2 = -(b - d) / (2 * a)

B = mpmath.mpf(b)
exact = 2 * c / (-B - mpmath.sqrt(B * B - 4 * a * c))

print(f"алгоритм 1: {x1!r}")
print(f"алгоритм 2: {x2!r}")
print(f"x1 == x2:   {x1 == x2}")
print()
print(f"эталон:     {mpmath.nstr(exact, 20)}")
print(f"ошибка 1:   {float(abs((x1 - exact) / exact)):.2%}")
print(f"ошибка 2:   {float(abs((x2 - exact) / exact)):.2%}")
