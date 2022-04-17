# Задача 7
# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат





def logika(a,b,c):
    d = bool(not (a or b or c) == (not a and not b and not c))
    print(f"Истинность утверждения  для предикат X = {a}  Y = {b} Z = {c} : {d}")

logika(0,0,0)
logika(0,0,1)
logika(0,1,1)
logika(1,1,1)
logika(1,0,1)
logika(1,1,0)

