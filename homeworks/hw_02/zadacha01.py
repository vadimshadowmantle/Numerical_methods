import math

# cond = |x · f'(x) / f(x)|
tasks = [
    ("√x,     x = 1e-8",     1e-8,        math.sqrt,          lambda x: 1 / (2 * math.sqrt(x))),
    ("ln x,   x = 1.001",    1.001,       math.log,           lambda x: 1 / x),
    ("x - 1,  x = 1.000001", 1.000001,    lambda x: x - 1,    lambda x: 1.0),
    ("sin x,  x = π/2",      math.pi / 2, math.sin,           math.cos),
]

results = []
for name, x, f, df in tasks:
    cond = abs(x * df(x) / f(x))
    verdict = "хорошо" if cond < 10 else "плохо"
    results.append((name, cond))
    print(f"{name:<22} cond = {cond:.3e}   обусловлена {verdict}")

print()
print("по возрастанию cond:")
for name, cond in sorted(results, key=lambda r: r[1]):
    print(f"  {name:<22} {cond:.3e}")
