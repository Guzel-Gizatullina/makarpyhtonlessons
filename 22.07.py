'''Введите два списка с клавиатуры. Выведите на экран только те элементы, которые встречаются в обоих списках.'''
numbers=input().split()
numbers2=input().split()
for i in numbers:
    for j in numbers2:
        if i==j:
            print(i)
        