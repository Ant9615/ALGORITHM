from typing import Generator
# iterater는 여러 요소를 가지는 컨테이너에서 각 요소를 하나씩 꺼내 어떤 처리를 수행하는 객체
# generator는 iterator를 생성해주는 함수다.
# 일반적인 함수처럼 작성되지만 데이터를 반환하기 위해 return이 아니라 yield를 사용함


def fib(n: int) -> Generator[int, None, None]:
    yield 0  # 특수조건
    if n > 0:
        yield 1  # 특수조건
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next  # 반환문


if __name__ == '__main__':
    for i in fib(10):
        print(fib(i))
