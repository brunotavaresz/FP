from tkinter import filedialog
file = input("File name:")

def main():
    # 1) Pedir nome do ficheiro (experimente cada alternativa):                           #A
    #name = filedialog.askopenfilename(title="Choose File") #B
    
    # 2) Calcular soma dos números no ficheiro:
    total = fileSum(file)
    
    # 3) Mostrar a soma:
    print("Sum:", total)


def fileSum(filename):
    # Complete a função para ler números do ficheiro e devolver a sua soma.
    total = 0
    with open(file, "r") as nums:
        for line in nums:
            total += float(line)
    return total


if __name__ == "__main__":
    main()

