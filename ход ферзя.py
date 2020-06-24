x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
distx=x2-x1
disty=y2-y1
if distx==disty or distx==0 and disty!=0 or distx!=0 and disty==0:
    print("YES")
else:
    print("NO")