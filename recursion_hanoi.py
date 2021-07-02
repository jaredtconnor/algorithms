''' 

'''
def recursive_hanoi(n, source, temp, target): 
    if n > 0: 
        recursive_hanoi(n-1, source, target, temp)

        if source:  
            target.append(source.pop())

        recursive_hanoi(n-1, temp, source, target)


# Examples
source = [5, 4, 3, 2, 1]
target = [] 
temp = []
n = len(source)

recursive_hanoi(n, source, temp, target) 
print(source, temp, target)
