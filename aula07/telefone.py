# Complete este programa como pedido no guião da aula.

def addcontacts(contactos):
    num = input('número? ')
    if num in contactos:
        print('Já tem este contacto')
    else:
        nome = input('nome? ')
        contactos[num] = nome

def remcontacts(contactos):
    num = input('número? ')
    if num not in contactos:
        print("O número que escolheu não está nos contactos! ")
    else:
        contactos.pop(num)

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    ...


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("add contactos...")
            addcontacts(contactos)
        elif op == "R":
            print("remove contactos...")
            remcontacts(contactos)
        else:
            print("Não implementado!")
    

# O programa começa aqui
main()

