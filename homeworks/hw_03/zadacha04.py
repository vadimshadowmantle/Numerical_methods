import numpy as np

arrays = [
    ("zeros float64", np.zeros((2, 3), dtype=np.float64)),
    ("zeros float32", np.zeros((2, 3), dtype=np.float32)),
    ("ones int16",    np.ones((2, 3), dtype=np.int16)),
    ("full 7 uint8",  np.full((2, 3), 7, dtype=np.uint8)),
]

for name, arr in arrays:
    print(f"{name:14s} dtype={arr.dtype}  nbytes={arr.nbytes}")

big64 = np.zeros((1000, 1000), dtype=np.float64)
big32 = np.zeros((1000, 1000), dtype=np.float32)

print()
print("(1000, 1000) float64:", big64.nbytes, "байт")
print("(1000, 1000) float32:", big32.nbytes, "байт")
print("экономия:", big64.nbytes - big32.nbytes, "байт")
