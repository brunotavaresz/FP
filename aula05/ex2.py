def inputFloatList():
    lista = []
    while True:
        n = input("nº? ")
        if n == "":
            break
        else:
            n = float(n)
        lista.append(n)
    return lista


def countLower(lst, v):
    count = 0
    for n in lst:
        if n < v:
            count += 1
        else:
            break
    return count

def minmax(lst):
    min = lst[0]
    max = lst [0]
    for n in lst:
        if n > max:
            n = max
        if n < min:
            n = min
    return max, min

def main():
    print(inputFloatList())
    lst = inputFloatList()
    vmedio = (minmax(lst)[0] + minmax(lst)[1]) / 2
    vinferior = countLower(lst, vmedio)
    print("A média entre o mínimo e o máximo é", vmedio)
    print("Há", vinferior)

main()
