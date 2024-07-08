# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(fname, "r", encoding="utf-8") as values:
        for line in values:
            if line[0].isnumeric():
                value_list = line.split("\t")
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    return lst

    
# b) Crie a função notaFinal aqui...
def notafinal(reg):
    n1 = float(reg[-3])
    n2 = float(reg[-2])
    n3 = float(reg[-1])
    return (n1 + n2 + n3) / 3

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("Número{:^100}Nota".format("Nome"))
    for reg in lst:
        print("{:>6}{:^100}{:4.1f}".format(reg[0], reg[1], notafinal(reg)))
# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    
    lst.sort()
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


