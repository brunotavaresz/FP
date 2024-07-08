CTP = float(input("Nota CTP: "))
CP = float(input("Nota CP: "))
nota_int = (CTP + CP) / 2
if nota_int < 10 : 
    ATPR = float(input("Nota ATPR: "))
    APR = float(input("Nota APR: "))
    nova_nota_final= (ATPR + APR) / 2
if CP < 9.5 or CTP < 9.5 :
    nota_x = 66
print("Nota final normal: {} " .format(nota_int))
print("Nota final recurso: {} " .format(nova_nota_final))
print("Chumbou a alguma disciplina (66 sim): {} " .format(nota_x))



    