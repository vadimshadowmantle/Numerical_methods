import math

x = 1.0
first = {1e-9: None, 1e-6: None, 1e-3: None}

print(" шаг  |        x         |   δx")
print("-------------------------------------")
for n in range(1, 10001):
    x *= 1.0001
    exact = math.exp(n * math.log(1.0001))
    d = abs(x - exact) / exact
    for level in first:
        if first[level] is None and d > level:
            first[level] = n
    if n % 1000 == 0:
        print(f"{n:>5} | {x:.14f} | {d:.2e}")

print()
for level, n in first.items():
    print(f"δx > {level:.0e}: {'на шаге ' + str(n) if n else 'не превысила за 10000 шагов'}")
