def rabin_karp(s,subs):
    len_sub = len(subs)
    h_subs = hash(subs)
    h_s  = hash(s) #Посчитаем хэш для строки S
    for i in range(len(s) - len_sub + 1):
        h_subs += pow[i] * h_subs[i];
        if h_subs == hash(s[i:i + len_sub])*pow[i]:
            return f'Обнаружено совпадение по позиции {i}'

    return -1

print (rabin_karp('alasdkfhlaskdjfh', 's'))




# проверяем все позиции


#Посчитаем хэш для строки S. Посчитаем значения хэшей для всех префиксов строки T.
#Теперь переберём все подстроки T длины |S| и каждую сравним с |S| за время O (1).

def getHash(h, L, R):
   result = h[R];
   if (L > 0): result -= h[L - 1];
   return result;

# считаем хеш строки t
ht = "ghghgh";
t=ht;
m=9
for i in range(m) :
   ht += pow[i] * t[i];


# проверяем все позиции
n=90
i=0
while(i + m <= n):
   if (getHash(h, i, i + m - 1) == ht * pow[i]) :
      print("обнаружено совпадение на позиции"+ i)
