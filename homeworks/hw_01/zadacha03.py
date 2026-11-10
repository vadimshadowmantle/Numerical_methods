import math


def relative_error(approx, exact):
    if exact == 0:
        return float('inf')
    return abs(approx - exact) / abs(exact)


pairs = [
    (3.14, math.pi),
    (2.718, math.e),
    (9.8, 9.81),
    (0.333, 1 / 3),
]

for approx, exact in pairs:
    print(f"relative_error({approx}, {exact:.6f}) = {relative_error(approx, exact):.6f}")

print()
print(f"relative_error(1, 0) = {relative_error(1, 0)}")
