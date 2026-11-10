items = [
    ("мост, м", 1247, 1250),
    ("болт, мм", 9.7, 10.0),
]

for name, x, exact in items:
    d_abs = abs(x - exact)
    d_rel = d_abs / abs(exact) * 100
    print(f"{name:<9}  Δx = {d_abs:.1f}   δx = {d_rel:.2f} %")
