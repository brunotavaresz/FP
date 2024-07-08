import bisect
lst = []
with open("wordlist.txt", "r") as words:
    for line in words:
        lst.append(line.strip())

def countwords(lst, exp):
    lst2 = [x[:len(exp)] for x in lst]
    primeiro = bisect.bisect_left(lst2, exp)
    ultimo = bisect.bisect_right(lst2, exp)
    if primeiro == ultimo:
        return lst2[ultimo][-1]
    return len(lst[primeiro:ultimo])
print(countwords(lst, "ea"))

