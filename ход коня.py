x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
distx=x2-x1
disty=y2-y1
if abs(distx)<=1 and abs(disty)<=2 or abs(distx)<=2 and abs(disty)<=1:
    print("YES")
else:
    print("NO")