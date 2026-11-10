import math
import random
import sys
import numpy as np


def experiment(seed):
    random.seed(seed)
    a = [random.random() for _ in range(100000)]
    b = np.random.default_rng(seed).random(100000)
    ref_a = math.fsum(a)
    ref_b = math.fsum(b)
    return {
        "random: sum - fsum": sum(a) - ref_a,
        "random: np.sum - fsum": float(np.sum(a)) - ref_a,
        "numpy:  sum - fsum": sum(b) - ref_b,
        "numpy:  np.sum - fsum": float(np.sum(b)) - ref_b,
    }, (ref_a, ref_b)


print(f"Python {sys.version.split()[0]}, numpy {np.__version__}")
print()

r1, s1 = experiment(42)
r2, s2 = experiment(42)
print(f"seed 42, запуск 1: fsum = {s1}")
print(f"seed 42, запуск 2: fsum = {s2}")
print(f"запуски совпадают: {r1 == r2 and s1 == s2}")
print()

print("        разница с fsum      |  seed 42   |  seed 43   |  seed 44")
print("-------------------------------------------------------------------")
r3, _ = experiment(43)
r4, _ = experiment(44)
for key in r1:
    print(f"{key:<27} | {r1[key]:+.2e} | {r3[key]:+.2e} | {r4[key]:+.2e}")
