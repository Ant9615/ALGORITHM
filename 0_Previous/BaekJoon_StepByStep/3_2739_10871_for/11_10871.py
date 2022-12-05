n, x = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    if x > l[i]:
        print("{}".format(l[i], end=""))
