import math


def naive(arr):
    s = 0.0
    for x in arr:
        s += x
    return s


def run(fn, arr):
    try:
        return repr(fn(arr))
    except Exception as e:
        return f"{type(e).__name__}"


cases = [
    ("большие 1e300 + 1e300", [1e300, 1e300]),
    ("переполнение 1e308·2 - 1e308", [1e308, 1e308, -1e308]),
    ("маленькие 1e-300 + 1e-300", [1e-300, 1e-300]),
    ("ноль", [0.0, 0.0]),
    ("денормализованные 1e-320", [1e-320, 1e-320]),
    ("1 + inf", [1.0, float('inf')]),
    ("inf + (-inf)", [float('inf'), float('-inf')]),
    ("1 + nan + 2", [1.0, float('nan'), 2.0]),
    ("всё вместе", [1e300, 1e-300, 0.0, 1e-320, float('inf'), float('nan')]),
]

print("          массив              |     наивная сумма      |        fsum")
print("--------------------------------------------------------------------------")
for name, arr in cases:
    print(f"{name:<29} | {run(naive, arr):<22} | {run(math.fsum, arr)}")
