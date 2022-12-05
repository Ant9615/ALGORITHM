import sys
sys.stdin = open('11720.txt', 'r')

string = list(input())
ans = 0
s = False

for k in range(len(string)):
    if string[k] != ' ' and s == False:
        ans += 1
        s = True

    if string[k] == ' ' and s == True:
        s = False

print(ans)


# print('{}'.format())
