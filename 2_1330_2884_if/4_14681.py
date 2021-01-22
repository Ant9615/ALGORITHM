# x, y = map(input().split(), int)
# map함수는 첫 줄 동시에 받아 리스트로 변환하기에 줄마다 따로 input값을 넣는 문제에 안맞음
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
