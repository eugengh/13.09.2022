n=int(input('Introdu n '))
m=int(input('Introdu m '))
def factorial(x):
    p = 1
    for i in range(1, x+1):
        p*=i
    return(p)

dif = n-m
C = factorial(n)/factorial(m)*factorial(dif)
print(C)