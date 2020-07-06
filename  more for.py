n=int(input())
ans=0 
factor=1
for i in range (1, n + 1):
    for j in range (1, i):
        factor*=j
    ans+=factor 
print(ans)
