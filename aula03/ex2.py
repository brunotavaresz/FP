from re import A


def max(a, b):
    mx = a
    if b > mx:
        mx = b

    return mx





def main():
    a= float(input("nº? "))
    b = float(input("nº ?"))
    x = max(a,b)
    print("mx: {} ".format(x))