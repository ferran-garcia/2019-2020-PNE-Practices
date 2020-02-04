




def fibosum(n):
    w = 0
    r = 1
    tot = 0
    res = 0
    for e in range(0, n):
        tot = (r + w)
        res = res + tot
        r = w
        w = tot
    return(res)

print("Sum of the first 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the first 10 terms of the Fibonacci series:", fibosum(10))