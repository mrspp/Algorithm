def fibo_rescusive(n):
    if n<=1: return n
    else: return fibo_rescusive(n-1) + fibo_rescusive(n-2)

#print(fibo_rescusive(40))


def fibo_loop(n):
    a = 0
    b = 1
    for i in range(1,n):
        print(b)
        tg = a
        a =  b
        b = tg + a
fibo_loop(10)

