# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Enter X: '))
y = int(input('Enter Y: '))
z = int(input('Enter Z: '))
A = not (x or y or z)
B = not x and not y and not z
if A == B:
    print('Statement is true')