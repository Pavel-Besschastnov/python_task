# 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. 
# Пример: 
# На сжатие: 
# Входные данные: 
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW 
# Входные данные:  
# 12W1B12W3B24W1B14W

import os
strok = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
print(strok)
count = 0
newstrok = ''
for i in range(0,len(strok)):
    if strok[i] == strok[i+1]:
        count+=1

print(count)
