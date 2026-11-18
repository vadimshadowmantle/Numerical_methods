import numpy as np

A = np.arange(6).reshape(2, 3)
B = A.T

print("B.base is not None:", B.base is not None)
print("A.strides:", A.strides)
print("B.strides:", B.strides)

B[0, 1] = 999
print()
print("после B[0, 1] = 999, A:")
print(A)
