#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

#Решение 1

import cProfile
import random

N = 10
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
print()

#cProfile.run('N')

#timeit
#N = 100
#100 loops, best of 5: 25.6 nsec per loop
#N = 20
#100 loops, best of 5: 51.3 nsec per loop
#N = 4
#100 loops, best of 5: 30.8 nsec per loop


#3 function calls in 0.000 seconds

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

