delta_a = 0.3
delta_b = 0.005


t_max = delta_a / delta_b
print(f"датчик B не хуже A при |T| <= {t_max:.0f} °C")
print()

for t in [-30, 0, 20, 60, 100, 300]:
    err_b = abs(t) * delta_b
    better = "B" if err_b < delta_a else ("одинаково" if err_b == delta_a else "A")
    print(f"T = {t:>4} °C   ошибка A = {delta_a:.2f}   ошибка B = {err_b:.2f}   точнее: {better}")
