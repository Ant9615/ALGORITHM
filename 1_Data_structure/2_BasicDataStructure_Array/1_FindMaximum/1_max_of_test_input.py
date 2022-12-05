from max import max_of

print("find maximum in array \n when input the 'End' it is ending")

num = 0
x = [] # empty list

while True:
    s = input(f'put in the x[{num}]: ')
    if s == 'End':
        break
    x.append(int(s))
    num += 1
    
print(f'your put {num} components')
print(f'maximum is {max_of(x)}')
    