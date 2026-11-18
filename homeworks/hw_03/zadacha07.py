import numpy as np

v = np.arange(5)

print("v[:, None]:", v[:, None].shape)
print("v[None, :]:", v[None, :].shape)
print("np.squeeze(v[:, None]):", np.squeeze(v[:, None]).shape)

t = np.arange(6).reshape(2, 3).T
print("np.arange(6).reshape(2, 3).T:", t.shape)
print(t)

s = v[:, None] + v[None, :]
print()
print("v[:, None] + v[None, :]:", s.shape)
print(s)

p = v[:, None] * v[None, :]
print()
print("v[:, None] * v[None, :]:", p.shape)
print(p)
