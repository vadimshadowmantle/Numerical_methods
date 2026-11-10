def significant(s):

    digits = s.replace(".", "").lstrip("0")
    if "." in s:
        return len(digits), len(digits)
    return len(digits.rstrip("0")), len(digits)


numbers = ["0.004520", "1200", "1.200", "10.03", "0.03050", "250000"]

for s in numbers:
    lo, hi = significant(s)
    if lo == hi:
        print(f"{s:>9}: {lo} знач. цифр   →  {float(s):.{lo - 1}e}")
    else:
        print(f"{s:>9}: от {lo} до {hi} знач. цифр (неоднозначно)   →  "
              f"{float(s):.{lo - 1}e} ... {float(s):.{hi - 1}e}")
