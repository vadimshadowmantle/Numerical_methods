import math
import numpy as np
import matplotlib.pyplot as plt


def bisection(f, a, b, eps=1e-9, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError(
            f"Нет смены знака на [{a}, {b}]: f(a)={fa}, f(b)={fb}"
        )

    journal = []

    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        length = b - a

        journal.append({
            "iter": k,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": fc,
            "length": length,
        })

        if fc == 0:
            return c, journal, "f_zero"
        if length < eps:
            return c, journal, "ok"

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return c, journal, "max_iter"


def print_journal(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'a':>12} | {'b':>12} | {'c':>12} | "
          f"{'f(c)':>14} | {'b-a':>10}")
    print("-" * 80)
    for row in journal:
        print(f"{row['iter']:>3} | {row['a']:>12.6f} | {row['b']:>12.6f} | "
              f"{row['c']:>12.6f} | {row['f(c)']:>14.3e} | "
              f"{row['length']:>10.2e}")


def f(x):
    return x**3 - 6 * x**2 + 11 * x - 6


xs = np.linspace(0, 4, 400)
plt.plot(xs, f(xs))
plt.axhline(0, color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = x³ − 6x² + 11x − 6")
plt.grid(True)

intervals = [(0.5, 1.2), (1.2, 2.5), (2.5, 4)]
exact = [1, 2, 3]
rows = []

for (a, b), x_true in zip(intervals, exact):
    root, j, s = bisection(f, a, b, eps=1e-9)
    print_journal(j, f"f(x) = x³ − 6x² + 11x − 6,  [{a}, {b}]")
    print(f"корень: {root:.12f},  статус: {s}")
    d = abs(root - x_true)
    rows.append((root, len(j), d, d / x_true, math.log2((b - a) / 1e-9)))

print()
print("     корень      | итераций |    Δ     |    δ     | log2(Δ0/ε)")
for root, n, d, rel, theory in rows:
    print(f"{root:.12f} |    {n}    | {d:.2e} | {rel:.2e} | {theory:.1f}")

plt.show()
