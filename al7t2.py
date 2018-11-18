#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
#заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
#и отсортированный массивы.


import random

N = 20
row = []
for i in range(N):
        row.append(random.randint(0,49))
print(f' Исходный массив: {row}')


def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst
 
def mergesort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst

print(f' Отсортированный массив: {mergesort(row)}')
