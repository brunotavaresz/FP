# Complete the code to make the HiLo game...

import random

def main():

    secret = random.randrange(1, 101);
    print("Can you guess my secret?")

    num = int(input("nº? "))
    count = 0
    while num > 0:
        if num > secret:
            print("High")
            num = int(input("nº? "))
            count +=1
        elif num < secret:
            print("Low")
            num = int(input("nº? "))
            count +=1
        else:
            print("Acertou")
            count +=1
            break
    print(count)

     

main()
