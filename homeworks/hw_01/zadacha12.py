import math
import sys

arr = [0.1] * 1000000
exact = 1e5

total = 0.0
for x in arr:
    total += x

results = [
    ("цикл for", total),
    ("sum(arr)", sum(arr)),
    ("math.fsum(arr)", math.fsum(arr)),
]

print(f"Python {sys.version.split()[0]}")
print()
print("    способ      |       результат       |     Δ     |     δ")
print("----------------------------------------------------------------")
for name, s in results:
    d = abs(s - exact)
    print(f"{name:<15} | {s:<21.12f} | {d:.3e} | {d / exact:.3e}")
