import numpy as np
from decimal import Decimal

err32 = float(np.float32(0.1)) - 0.1
err64 = float(np.float64(0.1)) - 0.1

print("float32:", repr(err32), f"{err32:.20e}")
print("float64:", repr(err64), f"{err64:.20e}")

true32 = Decimal(float(np.float32(0.1))) - Decimal("0.1")
true64 = Decimal(float(np.float64(0.1))) - Decimal("0.1")

print()
print("ошибка float32 относительно точного 0.1:", f"{float(true32):.20e}")
print("ошибка float64 относительно точного 0.1:", f"{float(true64):.20e}")
print("ошибка float32 больше в", f"{float(true32 / true64):.3e}", "раз")


