

# https://www.daleseo.com/sort-merge/
# https://bblackscene21.tistory.com/8

import sys

# def merge_sort(arr):
#     a_s = len(arr)
#     if a_s <= 1:
#         return arr
    
#     a_m = len(arr) // 2
    
#     lef = merge_sort(arr[:a_m])
#     rig = merge_sort(arr[a_m:])
#     mer = merging(lef,rig)
#     return mer
    
# def merging(arr1, arr2):
#     merged = []
#     while len(arr1) > 0 and len(arr2) > 0:
#         if arr1[0] <= arr2[0]:
#             merged.append(arr1.pop(0))
#         else:
#             merged.append(arr2.pop(0))
    
#     if len(arr1)>0:
#         merged += arr1
#     if len(arr2)>0:
#         merged += arr2
        
#     return merged



# def merge_sort(arr, p, q):    
#     if p>=q: 
#         return 
#     m_p = (p+q) // 2 # for index(e.g., 7 half is 3.5)
#     merge_sort(arr,p, m_p)
#     merge_sort(arr, m_p+1, q)
#     merge(arr, p, m_p+1, q)

# def merge(arr, lef, rig, end):
#     mer = []
#     l, r = lef,rig
#     while l < rig and r <= end:
#         if arr[l] <= arr[r]:
#             mer.append(arr[l])
#             l += 1
#         else: 
#             mer.append(arr[r])
#             r += 1
    
#     while l < rig:
#         mer.append(arr[l])
#         r += 1
    
#     while r <= end:
#         mer.append(arr[r])
#         r += 1
        
#     l = lef
#     for n in mer:
#         arr[l] = n 
#         l += 1

# def mergeSort(list,p,q): #q= inclusive
# 	if p>= q: return
# 	mid = (p + q) // 2
# 	mergeSort(list, p, mid)
# 	mergeSort(list, mid+ 1, q)
# 	merge(list, p, mid + 1, q)


# def merge(list, left, right, end):
# 	merged = []
# 	l, r = left, right
# 	while l < right and r <= end:
# 		if list[l] <= list[r]:
# 			merged.append(list[l])
# 			l +=1
# 		else:
# 			merged.append(list[r])
# 			r +=1
# 	while l < right:
# 		merged.append(list[l])
# 		l +=1
# 	while r <= end:
# 		merged.append(list[r])
# 		r+=1

# 	l = left
# 	for n in merged:
# 		list[l] = n	
# 		l +=1



# def merge_sort(arr):
#     if len(arr) < 2: return arr
    
#     mid = len(arr) // 2
    
#     lef = merge_sort(arr[:mid])
#     rig = merge_sort(arr[mid:])
    
#     return merging(lef,rig)

# def merging(lef,rig):
#     tmp = []
#     i = 0 
#     j = 0
    
#     while i < len(lef) and j < len(rig):
#         if lef[i] > rig[j]:
#             tmp.append(rig[j])
#             j += 1
#         else: 
#             tmp.append(lef[i])
#             i += 1
            
#     while j < len(rig):
#         tmp.append(rig[j])
#         j += 1
        
#     while i < len(lef):
#         tmp.append(lef[i])
#         i += 1
#     return tmp

# https://leunco.tistory.com/71

def merge_sort(arr):
    if len(arr) <= 1: return arr
    
    mid = len(arr) // 2
    
    lef = merge_sort(arr[:mid])
    rig = merge_sort(arr[mid:])
    
    i,j,k=0,0,0
    
    while i < len(lef) and j < len(rig):
        if lef[i] < rig[j]:
            arr[k] = lef[i]
            i+=1
        else:
            arr[k] = rig[j]
            j+=1
        k += 1 
        
    if i == len(lef):
        while j < len(rig):
            arr[k] = rig[j]
            j += 1
            k += 1 
    elif j == len(rig):
        while i < len(lef):
            arr[k] = lef[i]
            i += 1
            k += 1
    return arr 


n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
# print(arr)
arr = merge_sort(arr) 
# print('\n')

for i in range(n):
    print(arr[i])




