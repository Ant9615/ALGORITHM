# @functool.lru_cahe()
# 모든 함수를 자동으로 메모이징하는 내장형 decorator
# 어떤 인자와 fib가 실행될 때마다 데커레이터는 계산된 반환값을 메모리에 저장(캐싱)함


from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:  # 기저조건
        return n
    return fib(n-1)+fib(n-2)


print(fib(10))
