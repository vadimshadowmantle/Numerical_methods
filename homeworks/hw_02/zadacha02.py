a = 1 + 1e-8
b = 1.0
f = a - b

cond_a = abs(a / f)
cond_b = abs(b / f)
print(f"cond по a = {cond_a:.3e}")
print(f"cond по b = {cond_b:.3e}")

da = 1e-9
a2 = a * (1 + da)
f2 = a2 - b
df = abs(f2 - f) / abs(f)

print()
print(f"f = {f:.6e},  f после возмущения = {f2:.6e}")
print(f"δf = {df:.3e}")
print(f"δf / δa = {df / da:.3e}   (предсказание cond = {cond_a:.3e})")