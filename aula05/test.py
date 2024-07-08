def inputFloatList():
    lst = []
    while True:
        n = input('Número:')
        if n == '':
            break
        else:
            n1 = float(n)
            lst.append(n1)
    return lst

def countLower(lst,v):
    inf = []
    for n in lst:
        if n < v:
            inf.append(n)
    return inf, len(inf)

def minmax(lst):
    min = lst[0]
    max = lst[0]
    for n in lst:
        if n > max:
            max = n
        if n < min:
            min = n
    return min, max

def main():
    lst = inputFloatList()
    medio = (minmax(lst)[0] + minmax(lst)[1])/2
    baixos = countLower(lst,medio)
    
    print(lst)
    print("A média entre o mínimo e máximo é", medio)
    print("Os {} números {} são inferiores à média".format(baixos[1], baixos[0]))

main()