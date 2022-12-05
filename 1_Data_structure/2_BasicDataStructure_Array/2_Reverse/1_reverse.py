from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

if __name__ == '__main__':
    print('order to reverse about input')
    nx = int(input('put in your number of components: '))
    x = [None]*nx
    
    for i in range(nx):
        x[i] = int(input(f'put x[{i}]: '))
        
    # sort to reverse
    reverse_array(x)
    
    print('sorted to reverse')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
    