#Пользователь вводит данные о количестве предприятий,
#их наименования и прибыль за 4 квартала для каждого предприятия.
#Программа должна определить среднюю прибыль (за год для всех предприятий)
#и вывести наименования предприятий, чья прибыль выше среднего
#и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
#Примечание: 4 квартала - это 4 разных прибыли ;-)

import collections

M = 5
N = int(input('Введите количество предприятий = '))
name = []

for i in range(N):
    a = []
    av_inc = 0
    print(f'\n Введите данные {i+1}- го предприятия: ')
    name1 = input('Введите название предприятия: ')
    name.append(name1) 
    
    for j in range(M-1):
        inc = int(input(f'Введите прибыль за {j+1}-й квартал: '))
        av_inc += inc/4
        a.append(inc)
    a.append(av_inc)
    name.append(a)
    print(f' Средняя прибыль предприятия {name1} за год {av_inc:.2f}')

total_av_inc = av_inc/N
print(f'Средняя прибыль за год для всех предприятий {total_av_inc}')

for i in range(N):
     if av_inc > total_av_inc:
         MaxIncome = collections.namedtuple('MaxIncome', ['name', 'av_inc'])
         Income1 = MaxIncome(name1, av_inc)
         print(Income1)
     else av_inc < total_av_inc:
         MinIncome = collections.namedtuple('MinIncome', ['name', 'av_inc'])
         Income2 = MinIncome(name1, av_inc)
         print(Income2)
             
    
          



        
    
                     

                     
                     
        


