import random

N = 150
row = []
for i in range(N):
        row.append(random.randint(0,N))
print(row)
 
n = row[0]
mx_fr = 1

for i in range(N-1):
    fr = 1
    for k in range(i+1,N):
        if row[i] == row[k]:
            fr += 1
    if fr > mx_fr:
        mx_fr = fr
        n = row[i]

    
   
if mx_fr > 1:
    print(f'Число {n} встречается {mx_fr} раз(а)')
    
else:
    print('Нет повторяющихся элементов')
