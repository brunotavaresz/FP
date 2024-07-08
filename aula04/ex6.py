n = int(input("Número de termos:"))
def leibnizPi4(n):
    i = 0
    pi = 0
    for r in range(n):
        pi += ((-1)**i)/(2*i+1)
        i += 1
    return pi

print("A soma dos",n,"primeiros termos desta série é",leibnizPi4(n))