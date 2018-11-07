#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
#Решение 2
import random
import cProfile

N = 100
row = []
for i in range(N):
        row.append(random.randint(0,N))
print(row)

mn = min(row)
mx = max(row)
imn = row.index(mn)
imx = row.index(mx)
print(f' {mn}  {mx}')
row[imn],row[imx] = row[imx],row[imn]

for i in range(N):
    print(row[i],end=' ')
print()
cProfile.run(' ')

#N  = 1000
#100 loops, best of 5: 25.7 nsec per loop
#N = 10
#100 loops, best of 5: 25.7 nsec per loop
# N = 100
#100 loops, best of 5: 25.7 nsec per loop

#Вывод: по моим замерам второе решение с исп функций минимум и максимум получилось более оптимальным и стабильным

#4 function calls in 0.000 seconds

#  Ordered by: standard name

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
