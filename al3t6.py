import random

N = 100
row = []
for i in range(N):
        row.append(random.randint(0,N))
print(row)
    
mn = 0
mx = 0

for i in range(N):
    if row[i] < row[mn]:
        mn = i
    elif row[i] > row[mx]:
        mx = i
print(f'\n Минимальное значение: Индекс {mn+1}, Значение {row[mn]} \n Максимальное значение: Индекс {mx+1}, Значение {row[mx]}')

s = 0

for i in range(mn+1, mx):
    s += row[i]
print(f'Сумма элементов между минимальным и максимальным значением: {s}')
