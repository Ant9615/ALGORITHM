def fib(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):  # 하향식 반복문(단순재귀는 상향식으로 계산함)
        last, next = next, last+next
    return next


if __name__ == '__main__':
    print(fib(10))

# 언더스코어 _
# 인터프리터에서 마지막 값을 저장할 때
# 값을 무시하고 싶을 때
# 변수나 함수명에 특별한 의미 또는 기능을 부여하고자 할 때
# 국제화 또는 지역화 함수로써 사용할 때
# 숫자 리터럴 값의 자릿수 구분을 위한 구분자로써 사용할 때

# 위의 for _ range는 특정값을 무시하고 싶을 때 사용
