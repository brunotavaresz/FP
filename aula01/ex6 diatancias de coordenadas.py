import math


x1 = float(input("x1? "))
y1 = float(input("y1? "))
x2 = float(input("x2? "))
y2 = float(input("y2? "))

d = math.sqrt(((y2 - y1)**2) + (x2 - x1)**2)

print ("A distância entre os pontos é de {}".format(d))