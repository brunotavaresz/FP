


def inputFloatList():

    lista = []

    linha = input("nº")

    while linha != "":
        numero = float(linha)
        lista.append(numero)   
        linha = input("nº")

    return lista

def countLower(lst, v):
    count = 0
    for item in lst:
        if item < v:
            count +=1
    return count

def minamax(lst):
    minimo = [0]
    maximo =[0]

    for item in lst:
        if item < minimo:
            item = minimo
        if item > maximo:
            item = maximo

    return(minimo, maximo)

def main():
    lista_de_numeros = inputFloatList()
    print(lista_de_numeros)
    print(countLower(lista_de_numeros, 3))
    print(minamax(lista_de_numeros))
main()