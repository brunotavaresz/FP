from re import A


def max(a, b, c):
    mx = a
    if b > mx:
        mx = b
    if c > mx:
        mx = c

    return mx





def main():
    a= float(input("nº? "))
    b = float(input("nº ?"))
    c = float(input("nº ?"))
    x = max(a,b, c)
    print("mx: {} ".format(x))
main()