# memoization
# : 계산 작업이 완료되면 결과를 저장하는 기술
# : 이전에 실행된 계산을 수행할 때 다시 계산하지 않고 저장된 값을 사용할 수 있다.

# Memoization Fibonacci
from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}  # 기저조건


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1)+fib(n-2)  # memoization
    return memo[n]


if __name__ == '__main__':
    print(fib(5))
