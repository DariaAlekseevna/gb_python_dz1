""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет """

day = int(input("Input integer number from 1 to 7: "))
if day > 5:
    print("congratulations, it's a holiday!") 
else: 
    print("it's weekday, go to work")