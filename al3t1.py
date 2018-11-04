row = [0] * 8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            row[j-2] += 1

i = 0
while i < len(row):
        print(f'{i+2}  -  {row[i]}')
        i += 1

