# coding: utf-8
# This program finds the maximum of two numbers.
# It uses the built-in max function.
# Can you do it with a conditional statement (if / if-else) instead?

x1 = float(input("number? "))
x2 = float(input("number? "))

# Use a conditional statement instead of max function!
if  x1 > x2 :
    print("{} é o maior número" .format(x1))
elif x2 > x1 :
    print("{} é o maior número" .format(x2))
else :
    print("{} = {}, os numeros são iguais" .format(x1, x2))

