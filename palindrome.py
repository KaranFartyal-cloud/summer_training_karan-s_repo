def checkPalin(temp , i , n):
    while i != n :
        if temp[i] != temp[n]:
            return False
        i += 1
        n -= 1
    return True

temp = input("Enter your string : ")

i = 0
n = len(temp)

if checkPalin(temp, i , n - 1):
    print(f"{temp} is palindrome")
else :
    print(f"{temp} is not palindrome")


