n = new = int(input())
l = 0

while True:
    sh = n//10
    re = n % 10
    p = sh + re
    l += 1
    new = int(str(n%10) + str(p%10)) 

    if (n == new):
        break
print(l)
