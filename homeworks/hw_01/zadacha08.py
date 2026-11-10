import math
import numpy as np

print(round(0.5), round(1.5), round(2.5), round(3.5),
      round(-0.5), round(-1.5), round(-2.5))

rng = np.random.default_rng(42)
vals = [k + 0.5 for k in rng.integers(0, 10, size=1000000)]

exact = math.fsum(vals)
up = math.fsum(math.floor(v + 0.5) for v in vals)
banker = math.fsum(round(v) for v in vals)

print()
print(f"точная сумма:       {exact:.1f}")
print(f"«0.5 вверх»:        {up:.1f}   сдвиг = {up - exact:+.1f}")
print(f"banker's rounding:  {banker:.1f}   сдвиг = {banker - exact:+.1f}")
