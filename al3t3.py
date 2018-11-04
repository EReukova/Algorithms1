import random

N = 4
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

a = row[mn]
row[mn] = row[mx]
row[mx] = a

for i in range(N):
    print(row[i], end = ',')

