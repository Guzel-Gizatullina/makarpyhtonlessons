'''Определите среднее значение всех элементов последовательности, завершающейся числом 0.'''
summ=0
length=0
while True:
    i=int(input())
    if i==0:
        break
    summ+=i
    length+=1
print(summ/length)
