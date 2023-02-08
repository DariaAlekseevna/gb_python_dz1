""" Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y). """

num_quarter = int(input("Enter number of quarter of plane (from 1 to 4): "))
if num_quarter == 1:
    print("x >= 0, y >= 0")
elif num_quarter == 2:
    print("x <= 0, y >= 0")
elif num_quarter == 3:
    print("x <= 0, y <= 0")
else:
    print("x >= 0, y <= 0")