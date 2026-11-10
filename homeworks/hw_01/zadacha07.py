x = 4.738291
delta = 0.02

x_round = round(x, 2)
print(f"неверно: {x} ± {delta}")
print(f"верно:   {x_round} ± {delta}")
print(f"значащих цифр осталось: {len(str(x_round).replace('.', ''))}")
