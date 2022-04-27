# Задача 26
# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
#Т е для k = 8, список будет выглядеть так:  F−n = (−1)n+1Fn. 
#  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи
import random
k = 10
print(f'Коэфициент k = {k}')
def f(x):
    fib = 1
    if x >  2:
        fib = f(x - 1) + f(x - 2)
    return fib
def nef(x):
    fib = -1
    if x <  -2:
        fib = f(x - 1) - f(x - 2)
    return fib
for i in range(1,k):
    print(f(i))
k = k * (-1)
for i in range(k,-1):
    print(nef(i))
