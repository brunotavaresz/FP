def ispalindrome(s):
    if s[:] == s[::-1]:
        return True
    else:
        return False 

def main():
    s = input("string? ")
    print(ispalindrome(s))

main()