'''Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.'''
numbers=input().split()
for i in range (len(numbers)):
    numbers[i]=int(numbers[i])
m=max(list)
print(m)
for i in range (len(numbers)):
    if numbers[i]==m:
        print(i)
        

