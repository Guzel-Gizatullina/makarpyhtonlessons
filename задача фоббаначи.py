n=int(input())
fib=1
fib1=1
for i in range(2, n):
    fib, fib1 = fib, fib + fib1
print(fib1)


