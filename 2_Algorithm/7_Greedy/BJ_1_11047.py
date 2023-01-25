import sys

sys.stdin = open('./test.txt', 'r')

'''
내가 고안한 것
1. 누적합이 k 이하일때 동전 카운팅하고 누적합 갱신, 동시에 k는 해당 코인 갯수에 대한 넘버를 뺌
+ 하지만, 누적합이 k 이상일 때부터 카운팅x
2. 0 전까지 계산하도록 함
+ 하지만, 계속 틀린답으로 나옴
3. 다른 코드를 참고해서 k를 (코인 갯수 * 코인 넘버)에 대한 나눗셈으로 갱신하고
+ k가 0이하가 되면 루프를 탈출하는 식으로 바꿈
+ 2와 3에 대해 차이를 생각하고 2에 대한 문제점을 생각해볼 필요 있음 

'''

# -----------------first-----------------

    # li_len = len(a_li)
    # a_li = sorted(a_li, reverse=True) # order to descending, will change to using quick sort
    # cnt = 0
    # obj = 0 
    # for i in range(li_len-1):
    #     cnt_1 = k//a_li[i]
        
    #     # obj += cnt_1 * a_li[i]
    #     if obj <= k:
    #         cnt += cnt_1
    #         obj += cnt_1 * a_li[i]
    #         print(f'a_li[{i}]{a_li[i]}: cnt is {cnt}')
    #         print(f'a_li[{i}]{a_li[i]}: obj is {obj}')
    #         print(k)
    #         k -= obj
    #     else:
    #         return cnt

# -----------------------------------------

#  -----------------second-----------------
    # s_li = sorted(a_li, reverse=True)
    # # print(f'sorted: {s_li}')
    # # obj = 0
    # cnt = 0
    # k = k
    
    # for i in s_li:
    #     cal = k // i
    #     if i <= k:
    #         obj += (cal * i)
    #         cnt += cal
    #         k -= (cal * i)
    #         # print(f'obj: {obj}, cnt: {cnt}, k: {k}')
    #     elif 0<k<obj:
    #         obj += (cal * i)
    #         cnt += cal
    #         k -= (cal * i)
    #         # print(f'obj: {obj}, cnt: {cnt}, k: {k}')
    #     else: 
    #          return cnt
# -----------------------------------------
def coin_greedy(a_li:list, k: int):
    s_li = sorted(a_li, reverse=True)
    # print(f'sorted: {s_li}')
    # obj = 0
    cnt = 0
    k = k
    
    for i in s_li:
        cal = k // i
        if i <= k:
            # obj += (cal * i)
            cnt += cal
            k %= (cal * i)
            # print(f'obj: {obj}, cnt: {cnt}, k: {k}')
        # elif 0<k<obj:
        #     obj += (cal * i)
        #     cnt += cal
        #     k -= (cal * i)
            # print(f'obj: {obj}, cnt: {cnt}, k: {k}')
            if k<= 0:
                return cnt


n, k = map(int, sys.stdin.readline().split())
# print(f'n is {n}, k is {k}')

a_li = [None]*n
for i in range(n):
    a_li[i] = int(sys.stdin.readline())
    
# print(a_li)

# the ordering will change to quick sort with descending
# a_li = sorted(a_li, reverse=True)


print(coin_greedy(a_li, k))