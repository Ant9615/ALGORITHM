n = int(input())
# a, b = map(int, input().split()) -> 먼저 a,b를 받으면 절차에 위배됨(개수 주워지고 개수만큼 input값을 계산)

for i in range(n):
    a, b = map(int, input().split())
    print(a+b)
