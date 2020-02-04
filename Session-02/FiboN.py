

def fibon(n):
    w = 0
    r = 1
    tot = 0
    for e in range(0, n):
        tot = (r+w)
        r = w
        w = tot
    return(tot)


print("5th Fibonacci term:", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term:", fibon(15))
