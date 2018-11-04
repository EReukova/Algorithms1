import random

N = 65
row = []
for i in range(N):
        row.append(random.randint(0,N))
print(row)

if row[0] > row[1]:
    mn1 = 0
    mn2 = 1
else:
    mn1 = 1
    mn2 = 0
    
for i in range(2,N):
    if row[i] < row[mn1]:
        a = mn1
        mn1 = i
        if row[a] < row[mn2]:
            mn2 = a
    elif row[i] < row[mn2]:
        mn2 = i
        
print(f'\n Первый наименьший элемент: Индекс {mn1+1} Значение {row[mn1]}')
print(f' Второй наименьший элемент: Индекс {mn2+1} Значение {row[mn2]}')
