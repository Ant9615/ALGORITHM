import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    i = a+b
    print(i)
# input 대신 sys.stdin.readline()
# 개행문자 포함하려면 sys.stdin.readline().rstrit()
# 시간 단축으루 위해 사용함
# sys.stdin.readline() > row_input()>input()
# sys.stdin: 여러 줄 입력 받을 때
# sys.stdin.readline(): 한 라인 입력 받을 때
