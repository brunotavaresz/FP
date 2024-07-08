import sys

def countLowers(ficheiro):

    letras = {}

    with open(ficheiro, encoding="utf8") as f:
        for linha in f:
            for caracter in linha:
                if letras.get(caracter.lower()) == None and caracter.isalpha():
                    letras[caracter.lower()] = 1
                elif caracter.isalpha():
                    letras[caracter.lower()] +=1
        return letras


def main():
    ficheiro = sys.argv[1]
    a = countLowers(ficheiro)
    b = dict(sorted(a.items()))
    for key, value in b.items():
        print(key, value)
main()
