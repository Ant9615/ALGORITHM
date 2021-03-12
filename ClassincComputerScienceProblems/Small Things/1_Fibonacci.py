# Fibonacci
# : 첫 번째와 두 번째 숫자르 제외한 모든 숫자가 이전 두 숫자를 합안 숫자를 나열한 수열

# def fib1(n: int) -> int:
#     return fib1(n-1)+fib1(n-2)


# if __name__ == "__main__":
#     print(fib1(5))
# 무한 재귀

# 재귀 함주의 기저조건
# 기저조건: 재귀함수를 빠져나오는 탈출 조건이다.

def fib(n: int) -> int:
    if n < 2:  # 기저조건
        return n
    return fib(n-1)+fib(n-2)  # 재귀 조건


if __name__ == "__main__":
    print(fib(5))
    print(fib(10))
