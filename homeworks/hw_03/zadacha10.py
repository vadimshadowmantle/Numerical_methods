import numpy as np

M = np.arange(12).reshape(3, 4)
print(M)
print()
print("M.sum(axis=0)    =", M.sum(axis=0))
print("M.sum(axis=1)    =", M.sum(axis=1))
print("M.mean(axis=0)   =", M.mean(axis=0))
print("M.mean(axis=1)   =", M.mean(axis=1))
print("M.argmax(axis=0) =", M.argmax(axis=0))
print("M.argmax(axis=1) =", M.argmax(axis=1))

small = np.array([[1, 2],
                  [10, 20]])
print()
print(small)
print("small.sum(axis=0) =", small.sum(axis=0))
print("small.sum(axis=1) =", small.sum(axis=1))
