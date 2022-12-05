# https://www.daleseo.com/quick-select/
# https://blog.naver.com/PostView.nhn?blogId=tndus4243&logNo=222228260717
# https://stackoverflow.com/questions/10806303/python-implementation-of-median-of-medians-algorithm 

import sys

def selection_sort(arr, k):
    global cnt, ans
    
    # down to 0(decreasing index)
    for i in range(n-1,0,-1):
        # initialize location of maximum and index to first element
        max_it, idx = arr[0], 0
        
        # compare to next element and change to maximum
        for j in range(1, i+1):
            if arr[j] > max_it:
                max_it, idx = arr[j], j
        # swap last element and current element 
        if arr[i] != arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            cnt += 1
        # if counting number of swap, finish this loop and print the result
        if cnt == k:
            ans = f'{arr[idx]} {arr[i]}'
    
    return ans
    
n, k = map(int,sys.stdin.readline().split()) # (delete it) readline과 readlins 주의
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0
ans = -1 
# print(arr)

arr = selection_sort(arr,k)

print(arr)

















# def find_max(a):
#     s =len(a)
#     # print(a)
#     max_c = a[0]
    
#     for i in range(s):
#         if a[i] > max_c:
#             max_c = a[i]
    
#     return max_c

# def selection(n, k, a):
#     cnt = 0
    
#     for i in range(n-1, 0, -1):
#         max_a = find_max(a)
#         # print(max_a)
#         max_idx = a.index(max_a)
#         print(max_idx)
#         # tmp = 05
#         # print(max_a)
#         if max_a > a[i]:
#             a[i], a[max_idx] = a[max_idx], a[i]
#             cnt += 1
#             # tmp = a[-1]
#             # a[-1] = a[max_idx]
#             # a[max_idx] = tmp
#             # print(a[i], a[max_idx])  
#         if cnt == k:
#             ans =  
            
#     return ans
    

# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))
# ans = -1 
# # print(a)
# # print(a[0:5])
# sl = selection(n, k, a)
# # print(sl)

# # print(f'{sl[0]} {sl[1]}')

        
