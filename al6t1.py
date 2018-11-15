#Исходная задача - ввести 3 числа и найти среднее
#ДЗ 6 урока - найти объем памяти, занимаемый переменными

import sys

print('Введите три числа: ')
a = int(input())
b = int(input())
c = int(input())
 
if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)

print(f'Объем памяти a,b,c: {sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)}b')

#Результат работы программы:

#Введите три числа:
#8
#6
#7
#Среднее: 7
#Объем памяти a,b,c: 42b
