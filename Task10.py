# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xa = float(input('Enter the X coordinate for A: '))
ya = float(input('Enter the Y coordinate for A: '))
xb = float(input('Enter the X coordinate for B: '))
yb = float(input('Enter the Y coordinate for B: '))
from math import sqrt 
print('Distant between points A and B is ' ,round(sqrt((xa - xb)**2 + (ya - yb)**2), 3))
