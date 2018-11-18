#Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
#заданный случайными числами на промежутке [-100; 100). Выведите на экран
#исходный и отсортированный массивы. Сортировка должна быть реализована
#в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random

N = 15
row = []
for i in range(N):
        row.append(random.randint(-100,99))
print(f' Исходный массив: {row}')

def swap(row, i, j):
    row[i], row[j] = row[j], row[i]
 
def bubble_sort(row):
    i = len(row)
    while i > 1:
       for j in range(i - 1):
           if row[j] > row[j + 1]:
               swap(row, j, j + 1)
       i -= 1
    return row
print(f' Реализация с функцией: {bubble_sort(row)}')


n = 1
while n < len(row):
     for i in range(len(row)-n):
          if row[i] > row[i+1]:
               row[i],row[i+1] = row[i+1],row[i]
     n += 1
print(f' Проверка циклом: {row}')

