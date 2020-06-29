x=int(input())
y=int(input())
n=int(input()) #smaller
m=int(input()) #bigger
n,m=min(n,m), max(n,m)
if x >= n / 2:
    x = n - x
if y >= m / 2:
    y = m - y
print(min(x, y))
