

def sumofn(n):

    sumn = 0
    for e in range(1, n+1):
        sumn += e
    return(sumn)


print("Sum from 1-100 is:", sumofn(100))
