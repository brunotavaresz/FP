livros = int(input("Quantos Livros são: "))

PF = 20 
PC = 24.95 
IMP =1.23
SPA= 0.20
Lucro = (PC - SPA / (IMP - PF)) * livros
IMP_f = 1.23 * livros
print("Os lucros são {} euros e os impostas têm o valor de {} euros." .format(Lucro, IMP_f))
