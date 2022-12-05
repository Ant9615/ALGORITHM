'''
references
https://ulwunr.tistory.com/11


'''


import sys 


def cal_budget(budgets):
    
    
    return 


n = int(sys.stdin.readline())
budgets = list(map(int,sys.stdin.readline().split()))
tot = int(sys.stdin.readline())

sum_bud = sum(budgets)

if sum_bud <= tot:
    print(max(budgets))

else:
    print(cal_budget(budgets))