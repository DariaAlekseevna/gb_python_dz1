""" Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21 """

a_x = int(input("Enter the coordinate of the point A by X: "))
a_y = int(input("Enter the coordinate of the point A by Y: "))
b_x = int(input("Enter the coordinate of the point B by X: "))
b_y = int(input("Enter the coordinate of the point B by Y: "))

distance = ((b_x - a_x)**2 + (b_y - a_y)**2)**0.5
print(round(distance, 3))