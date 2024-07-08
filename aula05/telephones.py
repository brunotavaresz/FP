n = str(input("nome? "))
def ispalindrome(n):
    if n == n[-1::-1]:
        return True
    else:
        return False

print(ispalindrome(n))







 