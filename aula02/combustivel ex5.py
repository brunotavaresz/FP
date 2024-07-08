x = float(input("Litros de combustível? "))
p1l = 1.4
ptotal = 1.4 * x
if x > 40:
    ptotal = (1.4 * x) * 0.9
print(ptotal)