x1=int(input())
y1=int(input())
x2=int(input())
y2= int(input())
colour1= 0 #black
colour2= 1 #white
if x1!=y1:
    colour1=1
if x2==y2:
    colour2=0
if colour1==colour2: 
    print("YES")
else:
    print("NO")
    
