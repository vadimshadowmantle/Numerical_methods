import numpy as np

a = np.arange(24)

for shape in [(4, 6), (2, 3, 4), (2, 2, 6), (24,)]:
    current = a.reshape(shape)
    print(f"shape={current.shape}  данные не потерялись: {np.array_equal(a, current.ravel())}")

t = a.reshape(4, 6).T
print()
print("a.reshape(4, 6).T  C_CONTIGUOUS:", t.flags["C_CONTIGUOUS"])
