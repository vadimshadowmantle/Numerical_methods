import numpy as np
import matplotlib.pyplot as plt


def newton(f, df, x0, eps=1e-12, max_iter=100):
    journal = []
    x = x0
    for k in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            return x, journal, "zero_derivative"
        x_new = x - fx / dfx
        journal.append({
            "iter": k,
            "x": x,
            "f(x)": fx,
            "f'(x)": dfx,
            "x_new": x_new,
            "step": abs(x_new - x),
        })
        if abs(x_new - x) < eps or abs(fx) < eps:
            return x_new, journal, "ok"
        x = x_new
    return x, journal, "max_iter"


def secant(f, x0, x1, eps=1e-12, max_iter=100):
    journal = []
    x_prev, x_curr = x0, x1
    f_prev, f_curr = f(x_prev), f(x_curr)

    for k in range(1, max_iter + 1):
        if f_curr - f_prev == 0:
            return x_curr, journal, "zero_denominator"
        x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        journal.append({
            "iter": k,
            "x_prev": x_prev,
            "x_curr": x_curr,
            "f_curr": f_curr,
            "x_new": x_new,
            "step": abs(x_new - x_curr),
        })
        if abs(x_new - x_curr) < eps or abs(f_curr) < eps:
            return x_new, journal, "ok"
        x_prev, f_prev = x_curr, f_curr
        x_curr = x_new
        f_curr = f(x_curr)
    return x_curr, journal, "max_iter"


def bisection(f, a, b, eps=1e-12, max_iter=200):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Нет смены знака")
    for k in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) < eps:
            return c, k
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
    return c, k


def print_journal_newton(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x':>14} | {'f(x)':>14} | {'f\'(x)':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x']:>14.10f} | {row['f(x)']:>14.3e} | "
              f"{row['f\'(x)']:>14.3e} | {row['step']:>10.2e}")


def print_journal_secant(journal, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"{'k':>3} | {'x_prev':>14} | {'x_curr':>14} | {'f_curr':>14} | {'шаг':>10}")
    print("-" * 70)
    for row in journal:
        print(f"{row['iter']:>3} | {row['x_prev']:>14.10f} | {row['x_curr']:>14.10f} | "
              f"{row['f_curr']:>14.3e} | {row['step']:>10.2e}")


f = lambda x: x**3 - 2*x + 2
df = lambda x: 3*x**2 - 2

xs = np.linspace(-3, 3, 400)
plt.plot(xs, f(xs))
plt.axhline(0, color="black")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = x³ − 2x + 2")
plt.grid(True)

root_n0, jn0, s_n0 = newton(f, df, x0=0, max_iter=10)
print_journal_newton(jn0, "Ньютон: f(x) = x³ − 2x + 2,  x₀ = 0")
print(f"корень = {root_n0:.12f},  итераций: {len(jn0)},  статус: {s_n0}")

root_n, jn, s_n = newton(f, df, x0=-2)
print_journal_newton(jn, "Ньютон: f(x) = x³ − 2x + 2,  x₀ = −2")
print(f"корень = {root_n:.12f},  итераций: {len(jn)},  статус: {s_n}")

root_s, js, s_s = secant(f, x0=-2, x1=-1)
print_journal_secant(js, "Секущие: f(x) = x³ − 2x + 2,  x₀ = −2, x₁ = −1")
print(f"корень = {root_s:.12f},  итераций: {len(js)},  статус: {s_s}")

root_b, n_b = bisection(f, -2, -1)

print(f"\n{'Метод':<12} | {'Старт':<14} | {'Корень':<20} | {'Итераций':>10}")
print("-" * 64)
print(f"{'Ньютон':<12} | {'x₀ = 0':<14} | {root_n0:<20.12f} | {len(jn0):>10}")
print(f"{'Ньютон':<12} | {'x₀ = −2':<14} | {root_n:<20.12f} | {len(jn):>10}")
print(f"{'Секущие':<12} | {'−2, −1':<14} | {root_s:<20.12f} | {len(js):>10}")
print(f"{'Бисекция':<12} | {'[−2, −1]':<14} | {root_b:<20.12f} | {n_b:>10}")

plt.show()
