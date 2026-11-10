import math

s = 0.1 + 0.2
print(f"0.1 + 0.2 = {s}")
print(f"0.1 + 0.2 == 0.3:            {s == 0.3}")
print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(s, 0.3)}")

d_abs = abs(s - 0.3)
print()
print(f"Δ = {d_abs:.3e}")
print(f"δ = {d_abs / 0.3:.3e}")
