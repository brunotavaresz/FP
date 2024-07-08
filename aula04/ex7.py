def seq():
    tot = 0
    tot_f = 0
    p= 0
    while True:
        n = input("Número:")
        p += 1
        if n == "":
            break
        else:
            n1 = float(n)
            tot += n1
            tot_f = tot / p
    return tot_f
    
print(seq())