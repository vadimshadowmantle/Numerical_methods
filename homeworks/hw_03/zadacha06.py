import numpy as np

M = np.arange(12).reshape(3, 4)
f = M.flatten()
r = M.ravel()

print("f.base is None:", f.base is None)
print("r.base is not None:", r.base is not None)

f[0] = 999
print()
print("после f[0] = 999, M:")
print(M)

r[1] = 888
print()
print("после r[1] = 888, M:")
print(M)
