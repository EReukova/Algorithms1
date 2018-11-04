M = 5
N = 4
row = []

for i in range(N):
    a = []
    s = 0
    print(f'\n Введите {i}-ю строку: ')
    
    for j in range(M-1):
        n = int(input(f'Введите {j+1}-й элемент {i}-й строки: '))
        s += n
        a.append(n)
    a.append(s)
    row.append(a)
 
for i in row:
    print(f'\n {i}')
