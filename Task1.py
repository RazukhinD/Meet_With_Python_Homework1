#Напишите программу для. проверки истинности утверждения
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input('Введи логическое(0 или 1) значение для Х: '))
Y = int(input('Введи логическое(0 или 1) значение для Y: '))
Z = int(input('Введи логическое(0 или 1) значение для Z: '))
if 0<=X<=1 and 0<=Y<=1 and 0<=Z<=1:
    if (not (X or Y or Z)) == (not X and not Y and not Z):
        print ('таблица истинности работает')
    else:
        print('Как ты это сделал?')
else:
    print('Ну по русски же написал или 0 или 1')