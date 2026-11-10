import math

small = [1e-10] * 500000
big = [1e6] * 500000

s_a = 0.0
for x in small + big:
    s_a += x

s_b = 0.0
for x in big + small:
    s_b += x

exact = math.fsum(small + big)

print(f"fsum:                  {exact:.10f}")
print(f"(а) маленькие → большие: {s_a:.10f}   Δ = {abs(s_a - exact):.2e}")
print(f"(б) большие → маленькие: {s_b:.10f}   Δ = {abs(s_b - exact):.2e}")
print()
print(f"сумма маленьких отдельно: {math.fsum(small):.10f}")
