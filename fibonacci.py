def fibo_recursive(n):
        if n<=1: return n
        else: return fibo_recursive(n-1) + fibo_recursive(n-2)

print(fibo_recursive(5))


def fibo_loop(n):
        firstnum = 1
        nextnum = 1
        for i in range(0,n):
                fibo = firstnum
                firstnum = nextnum
                nextnum = fibo + firstnum
        return fibo


print(fibo_loop(5))

def fibo_list(n):
        fibo_list = [1, 1]
        for i in range(2,n+1):
                fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
        return fibo_list[n-1]
print(fibo_list(5))
        
