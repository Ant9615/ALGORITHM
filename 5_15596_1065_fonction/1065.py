import sys
sys.stdin = open('1065.txt', 'r')


def confirm(s):
    global ans

    length = len(str(s))  # 123 - 3
    s_str = str(s)  # '123'
    minus = 1000000

    if length > 2:  # 1 2 3 4
        cnt = 0  # cnt는 등차의 개수
        for k in range(length-1):  # 0,1  // 3 2
            if minus == 1000000:
                minus = int(s_str[k+1]) - int(s_str[k])
                cnt += 1
                continue
            elif minus != 1000000 and minus == int(s_str[k+1]) - int(s_str[k]):
                cnt += 1
            # minus = 1000000

        if cnt == length - 1:
            ans += 1
            # print(s, cnt)

    elif length <= 2:
        ans += 1

    return


n = int(input())
ans = 0
for k in range(1, n+1):
    confirm(k)

print(ans)
