'''Введите с клавиатуры список чисел. Выведите на экран только нечетные элементы списка.'''
number=input().split()
for i in number:
    if int(i)%2==0:
        continue
    print(i)

