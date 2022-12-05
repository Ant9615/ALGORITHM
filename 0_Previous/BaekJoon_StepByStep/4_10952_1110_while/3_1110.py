n = m = int(input())
l = 0

while True:
    new = (n//10) + (n % 10)  # 몫과 나머지 합치고
    l += 1  # new의 과정 횟수 count
    n = int(str(n % 10)+str(new % 10))  # 새로운 수 조합

    if n == m:  # 변수확인 잘해야함
        break

print(l)
