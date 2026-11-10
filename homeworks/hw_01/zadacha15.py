from decimal import Decimal, getcontext

getcontext().prec = 28
n = 1000000

# (а) float
acc_float = 0.0
for _ in range(n):
    acc_float += 0.01

# (б) Decimal
acc_dec = Decimal("0")
for _ in range(n):
    acc_dec += Decimal("0.01")

# целые копейки
acc_kop = 0
for _ in range(n):
    acc_kop += 1

exact = Decimal("10000.00")
diff_float = abs(Decimal(acc_float) - exact)

print(f"float:    {acc_float:.10f} руб.")
print(f"Decimal:  {acc_dec} руб.")
print(f"копейки:  {acc_kop // 100}.{acc_kop % 100:02d} руб.  ({acc_kop} коп.)")
print()
print(f"расхождение float:   {diff_float:.10f} руб.  = {diff_float / exact * 100:.2e} %")
print(f"расхождение Decimal: {abs(acc_dec - exact)} руб.")
print(f"расхождение копеек:  {abs(acc_kop - 1000000)} коп.")
