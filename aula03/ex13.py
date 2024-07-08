
a = float(input("nº "))
b = float(input("nº "))


def mdc(a,b):
    r = a % b
    if r == 0:
        return b
    else:
        x = mdc(b,r)
        return x

print(mdc(a, b))