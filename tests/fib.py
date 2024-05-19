
m = {}

def fib(n):
    if n in m:
        return m[n]
    
    if n <= 2:
        result = 1
    
    else:
        result = fib(n-1) + fib(n-2)
    
    m[n]=result
    return result

print(fib(50))