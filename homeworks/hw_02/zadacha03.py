import math

print("   ε    |    корень x1     | сдвиг корня | сдвиг / ε")
print("-----------------------------------------------------")
for eps in [1e-2, 1e-4, 1e-6]:
    a, b, c = 1.0, -2.0, 1 - eps
    d = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + d) / (2 * a)
    shift = abs(x1 - 1)
    print(f"{eps:.0e}  | {x1:.14f} | {shift:.3e}   | {shift / eps:.0f}")
