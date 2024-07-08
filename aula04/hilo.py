n = int(input("nº ? "))
divtotal = 0
for i in range(1, n):
    if n % i == 0:
        print(i)
        divtotal = divtotal + i
        