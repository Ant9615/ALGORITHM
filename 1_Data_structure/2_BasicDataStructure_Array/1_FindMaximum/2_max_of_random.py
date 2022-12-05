import random
from max import max_of

print('find maximum in random numbers')
num = int(input('put number of random: '))
lo = int(input('put minimum in random numbers: '))
hi = int(input('put maximum in random numbers: '))

x = [None]*num # generate list of size of numbers

for i in range(num):
    x[i] = random.randint(lo,hi)
    
print(f'{x}')
print(f'maximum in random numbers is {max_of(x)}')