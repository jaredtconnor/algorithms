'''
Using recursion implement pow(x,n) function, which calculates x raised to the power of n (i.e. xn).

Example: 
input: x = 2,  n = 9
Output: 512
'''
def recursive_power(x, n): 

    # Base case
    if n == 1: 
        return x

    else: 
        return x * recursive_power(x, n-1)

test = recursive_power(2, 9)
print(test)