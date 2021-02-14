def confirm(s, n):
    result = s  # 972

    temp = str(s)  # '33'
    # print(temp)
    for m in range(len(temp)):
        result += int(temp[m])

    if result == n:
        return True
    else:
        return False


def fnt(n):
    global con   # 현재 39가 들어옴

    k = len(str(n)) # k = '39' , n =39
    start = (9*k)   # start

    if n>100:
        for s in range(n-start, n):  # 1 ~ 999 => 1026 /// 972 , 999
            ans = confirm(s, n)  # (1,39) , (2,39) , (33,39) ~ (38,39) /// (972,999) ~ (998,999)

            if ans == True:
                if con[n] == 0:
                    con[n] = 1
                break

    else:
        for s in range(1, 101):  # 1 ~ 999 => 1026
            ans = confirm(s, n)  # (1,39) , (2,39) , (33,39) ~ (38,39)

            if ans == True:
                if con[n] == 0:
                    con[n] = 1
                break

    # for s in range(1, n):  # 1 ~ 99 / 100 ~ 10000 / n -> x + 첫번째 자릿수 + 두번째 자릿수  + 세번째 자릿수 100 / 999 -> 70/969 
    #     # 999 = x + (9+9+9) / 972 / 1~971 971 111 ->84 ~ 110
    #     ans = confirm(s, n)  

    #     if ans == True:
    #         if con[n] == 0:
    #             con[n] = 1
    #         break
    return


con = [0]*10001 # step1 [0,0,0,0,0,........0]
for k in range(1, 10001):
    fnt(k)  


for s in range(1, 10001):
    if con[s] == 0:
        print(s)
