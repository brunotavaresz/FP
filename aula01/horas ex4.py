seg = int(input("segundos? "))
h = seg // 3600
x = seg % 3600
m = x // 60
s = x % 60

print("{:02d}:{:02d}:{:02d}".format(h, m, s))