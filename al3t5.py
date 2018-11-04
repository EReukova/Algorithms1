import random
N = 100
row = []
for i in range(N):
        row.append(random.randint(-100,10))
print(row)
 
i = 0
a = -1
while i < N:
        if row[i] < 0 and a == -1:
                a = i
        elif row[i] < 0 and row[i] > row[a]:
                a = i
        i += 1
 
print(f'Наибольшее отрицательное значение: Индекс {a+1}, Значение {row[a]}')
