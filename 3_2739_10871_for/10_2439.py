n = int(input())

for i in range(1, n+1):
    b = n-i
    print('{0}{1}'.format(' '*b, '*'*i))
