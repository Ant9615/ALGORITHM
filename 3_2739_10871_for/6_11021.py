import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print('Case #{0}: {1}'.format(i+1, a+b))

# i+1을 한 이유는 case #1부터 출력하기 위함임 반복 입력값을 받으면 첫 번째 숫자 1부터 출력
# formating 순서: {0} 첫 번째 인덱스 {1} 두 번째 인덱스
