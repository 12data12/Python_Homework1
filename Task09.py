# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quadrant = int(input('Enter the quadrant number (from 1 to 4): '))
if quadrant == 1:
    print('X and Y are greater than zero (X > 0, Y > 0)')
elif quadrant == 2:
    print('X is less than zero and Y is greater than zero (X < 0, Y > 0)')
elif quadrant == 3:
    print('X and Y are less than zero (X < 0, Y < 0)')
elif quadrant == 4:
    print('X is greater than zero and Y is less than zero (X > 0, Y < 0)')
    