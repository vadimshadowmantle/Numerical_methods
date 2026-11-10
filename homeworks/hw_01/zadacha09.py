import math

terms = [1 / k for k in range(1, 101)]

s_a = 0.0
for t in terms:
    s_a += t

s_b = 0.0
for t in terms:
    s_b += round(t, 3)

exact = math.fsum(terms)

d_a = abs(s_a - exact)
d_b = abs(s_b - exact)
print(f"эталон fsum:          S = {exact:.15f}")
print(f"(а) без округлений:   S = {s_a:.15f}   ΔS = {d_a:.2e}   δS = {d_a / exact:.2e}")
print(f"(б) округление до 3:  S = {s_b:.15f}   ΔS = {d_b:.2e}   δS = {d_b / exact:.2e}")
if d_a == 0:
    print("ошибка (а) равна 0, поэтому (б) хуже «бесконечно»")
else:
    print(f"ошибка (б) больше в {d_b / d_a:.0f} раз")
