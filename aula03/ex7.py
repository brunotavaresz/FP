


def tax(r):
    if r <= 1000:
        x= 0.1 * r
    elif r > 1000 and r <= 2000:
        x = 0.2 * r - 100
    elif 2000 < r:
        x = 0.3 * r - 300
    else:
        exit(1)

    return x


def main():
    r = int(input("r? "))

    print("... {} ".format(tax(r)))
main()