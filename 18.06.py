#Шахматный слон ходит по диагонали. Даны две различные клетки шахматной доски,
#  определите, может ли слон попасть с первой клетки на вторую одним ходом.
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x2-x1==y2-y1:
    print("YES")
else:
    print("NO")