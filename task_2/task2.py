def fib(n, a=0, b=1):
    if n == 0:
        return a
    return fib(n - 1, b, a + b)


print(fib(int(input())))