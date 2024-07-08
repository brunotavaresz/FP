def shorten(n):
    a = ""
    for x in n:
        if x.isupper() == True:
            a += x
    return a

def main():
    n = (input("nome? "))
    print(shorten(n))
main()
