x = 47.3
delta = 0.001


a = x / (1 + delta)
b = x / (1 - delta)
print(f"точно:       [{a:.6f}, {b:.6f}]")


d = abs(x) * delta
print(f"Δx ≈ |x|·δx = {d:.4f}")
print(f"приближённо: [{x - d:.4f}, {x + d:.4f}]")
print(f"ответ:       [{x - d:.2f}, {x + d:.2f}]")
