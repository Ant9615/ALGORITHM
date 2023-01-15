import sys

sys.stdin = open('./test.txt', 'r')

def quick(li, cl: int, cr: int):
    pl = cl
    pr = cr
    x = li[(cl+cr)//2]
    
    while pl<=pr:
        while li[pl] < x: pl += 1
        while li[pr] > x: pr -= 1
        
        if pl <= pr:
            li[pl], li[pr] = li[pr], li[pl]
            pl += 1
            pr -= 1
    if cl<pr: quick(li, cl, pr)
    if cr>pl: quick(li, pl, cr)

def sort(li):
    quick(li, 0, len(li)-1) # given, left, right
    
    
# calculate mean 
def ave(li):
    ms = 0 
    for i in range(len(li)):
        ms += li[i]
    return ms//len(li)

# calculater median
# reference: https://m.blog.naver.com/hankrah/221877939533
def median(li):
    if len(li) % 2 == 0:
        return (li[(len(li)/2)-1] + li[int(len(li)/2)]) / 2  
    else:
        return li[int(len(li)/2)]
        
        

li = []

for i in range(5):
    n = sys.stdin.readline()
    li.append(n)

sort(li)

li = list(map(int, li))
# print(li) # for debugging

print(ave(li))
print(median(li))



