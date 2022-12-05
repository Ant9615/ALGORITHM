# find maximum using array

from typing import Any, Sequence
# in the Sequence have list, bytearray, str, tuple and bytes


# type of parameter 'a' is sequence type 
def max_of(a) -> Any: # '-> Any': the return is structure randomly
    # return maximum component of sequence 'a'
    maximum = a[0]
    
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
            
    return maximum

if __name__ == "__main__":
    num = int(input('put in number of components:'))
    
    x = [None] * num # array
    
    for i in range(num): # run about 0 to number of components 
        x[i] = int(input(f'put in x[{i}]:'))
        
    print(f'the maxumum value is {max_of(x)}')