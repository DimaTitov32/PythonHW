# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите X: '))
y = int(input('Введите y: '))
if x>0 and y>0:
    print('Точка находится в 1-ой чертверти')
if x<0 and y>0:
    print('Точнка находится во 2-ой четверти')
if x<0 and y<0:
    print('Точка находится в 3-ей четверти')
if x>0 and y<0:
    print('Точка находится в 4-ой четверти')