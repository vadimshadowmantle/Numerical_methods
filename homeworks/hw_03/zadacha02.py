import numpy as np

a = np.array([1, 2, 3, 4])

print("a / 2   =", a / 2)
print("a // 2  =", a // 2)
print("a / 2.0 =", a / 2.0)
print("a.dtype        =", a.dtype)
print("(a / 2).dtype  =", (a / 2).dtype)
print("(a // 2).dtype =", (a // 2).dtype)
print("a после операций:", a)

b = np.array([1, 2, 3], dtype=np.int8)
c = b + 127
print()
print("b + 127 =", c)
print("dtype:", c.dtype)
