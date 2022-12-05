'''
use bubble sort
'''

# def bubble(x):
#     for i in range(len(x)-1,0,-1):
#         for j in range(i):
#             if x[j] > x[j+1]:
#                 temp = x[j+1]
#                 x[j+1] = x[j]
#                 x[j] = temp
                
#             '''
#             if x[j]>x[j+1]:
#                 x[j], x[j+1] = x[j+1], x[i]
#             '''
#     return x

# x = []
# n = int(input())

# for i in range(n):
#     num = int(input())
#     x.append(num)

# x = bubble(x)    
# for i in range(n):
#     print(x[i])

'''
use insert sort
'''

# def insert_sort(x):
#     for i in range(len(x)):
#         loc = i-1
#         item = x[i]
        
#         while(loc>= 0 and item < x[loc]):
#             x[loc+1] = x[loc]
#             loc = loc-1
        
#         x[loc+1] = item
#     return x

# x = []
# n = int(input())

# for i in range(n):
#     num = int(input())
#     x.append(num)

# x = insert_sort(x)    
# for i in range(n):
#     # print(x)
#     print(x[i])

            
            
            