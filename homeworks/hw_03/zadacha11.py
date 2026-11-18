import numpy as np

X = np.random.default_rng(42).normal(size=(5, 3))

m = X.mean(axis=0)
mk = X.mean(axis=0, keepdims=True)
print("X.mean(axis=0):", m.shape)
print("X.mean(axis=0, keepdims=True):", mk.shape)
print("X - X.mean(axis=0):", (X - m).shape)
print("X - X.mean(axis=0, keepdims=True):", (X - mk).shape)

print()
print("X.std(axis=1):", X.std(axis=1).shape)
print("X.std(axis=1, keepdims=True):", X.std(axis=1, keepdims=True).shape)

Z = (X - X.mean(axis=1, keepdims=True)) / X.std(axis=1, keepdims=True)
print()
print("средние по строкам:", Z.mean(axis=1))
print("std по строкам:    ", Z.std(axis=1))

print()
try:
    X - X.mean(axis=1)
except ValueError as e:
    print("X - X.mean(axis=1) без keepdims — ошибка:", e)
