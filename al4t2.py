#Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования Решета Эратосфена;
#Использовать алгоритм решето Эратосфена

#1. C использованием алгоритма

import cProfile

n = int(input("Вывод простых чисел до числа   "))
a = [0] * n  
for i in range(n):  
    a[i] = i  

a[1] = 0

m = 2  
while m < n:  
    if a[m] != 0:  
        j = m * 2  
        while j < n:
            a[j] = 0  
            j = j + m 
    m += 1


b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])

del a
print(b)
cProfile.run(' ')

#timeit
#Вывод простых чисел до числа   8
#100 loops, best of 5: 61.6 nsec per loop
#Вывод простых чисел до числа   100
#100 loops, best of 5: 66.7 nsec per loop
#Вывод простых чисел до числа   50
#100 loops, best of 5: 66.7 nsec per loop

#cProfile
#3 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
