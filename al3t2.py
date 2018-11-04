import random
N = 20
row1 = [0]*N
row2 = []
for i in range(N):
    row1[i] = random.randint(0,N)
    if row1[i] % 2 == 0:
     row2.append(i)
print(row1)
print(f'Индексы четных чисел: {row2}')
