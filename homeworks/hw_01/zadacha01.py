import math

pairs = [
    ("3.14 и π", 3.14, math.pi),
    ("2.718 и e", 2.718, math.e),
    ("9.8 и 9.81", 9.8, 9.81),
    ("0.333 и 1/3", 0.333, 1 / 3),
]

results = []
for name, x, exact in pairs:
    d_abs = abs(x - exact)
    d_rel = d_abs / abs(exact) * 100
    results.append((name, d_abs, d_rel))
    print(f"{name:<12}  Δx = {d_abs:.6f}   δx = {d_rel:.4f} %")

print()
print("по Δx (лучше → хуже):", [r[0] for r in sorted(results, key=lambda r: r[1])])
print("по δx (лучше → хуже):", [r[0] for r in sorted(results, key=lambda r: r[2])])
