import numpy as np

A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)

print("A @ B:", (A @ B).shape)
print(A @ B)
print()
print("A.T @ B.T:", (A.T @ B.T).shape)
print(A.T @ B.T)
print()
print("A * A:", (A * A).shape)
print(A * A)

print()
try:
    print(A * B)
except ValueError as e:
    print("A * B — ошибка:", e)

D1 = np.array([[2, 0], [0, 3]])
D2 = np.array([[4, 0], [0, 5]])
print()
print("D1 * D2:")
print(D1 * D2)
print("D1 @ D2:")
print(D1 @ D2)
print("одинаково:", np.array_equal(D1 * D2, D1 @ D2))
