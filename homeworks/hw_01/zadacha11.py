import math
from decimal import Decimal, getcontext


a = 1 + 1e-15
b = 1.0
r = a - b
print(f"a - b = {r}   (ожидали 1e-15)")
print(f"δ = {abs(r - 1e-15) / 1e-15:.2%}")


qa, qb, qc = 1.0, 1e8, 1.0
d = math.sqrt(qb * qb - 4 * qa * qc)
x_bad = (-qb + d) / (2 * qa)
x_good = 2 * qc / (-qb - d)


getcontext().prec = 50
D = Decimal
x_exact = 2 * D(qc) / (-D(qb) - (D(qb) ** 2 - 4 * D(qa) * D(qc)).sqrt())

err_bad = abs((D(x_bad) - x_exact) / x_exact)
err_good = abs((D(x_good) - x_exact) / x_exact)
print()
print(f"эталон:               x = {x_exact:.20e}")
print(f"обычная формула:      x = {x_bad:.20e}   δ = {float(err_bad):.2e}")
print(f"переписанная формула: x = {x_good:.20e}   δ = {float(err_good):.2e}")
