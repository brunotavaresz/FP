import math


ca = float(input("comprimento do cateto a: "))
cb = float(input("comprimento do cateto b: "))
h = ((cb**2)+(ca**2))**0.5
x = math.asin(ca/h)
x = math.degrees(x)
z = 180 - 90 - x

print("A hipotenusa tem um valor de {} e o ângulo de cateto A com a hipotenusa é de {}".format(h,z))