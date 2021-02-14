# import sys
# sys.stdin = open('11720.txt', 'r')

a = int(input())  # 11
b = input()      # 10987654321

ans = 0

for k in range(a):
    ans += int(b[k])

print(ans)
