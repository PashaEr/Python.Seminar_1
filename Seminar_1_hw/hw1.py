# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# num1 = int(input("Введите день недели: "))

# if num1 > 7 or num1 < 1:
#     quit('Такого дня недели не существует, попробуйте ещё раз  ') 
    
# if (num1 == 7 or num1 == 6 ):
#         print('Ура, выходные!')
    
# else:
#     print("Этот день рабочий( ")

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.


# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             result = not (x or y or z) == (not x and not y and not z)
#             if result:
#                 print(x, y, z, 'Утверждение истинно')
#             else:
#                 print(x, y, z, '"Утверждение ложно')

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
#  номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# import os
# os.system('cls')

# x = float(input('Ввведите координаты х: '))
# y = float(input('Ввведите координаты y: '))

# if x == 0 or y == 0:
#     print('Введённые данные не соответствуют условию задачи! \n')

# elif x > 0 and y > 0:
#     print('Заданная точка находится в I четверти \n')
# elif x < 0 and y > 0:
#     print('Заданная точка находится в II четверти \n')
# elif x < 0 and y < 0:
#     print('Заданная точка находится в III четверти \n')
# else:
#     print('Заданная точка находится в IV четверти \n')

# 4.Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y)

import os
os.system('cls')

coord = [0,'x > 0; y > 0','x < 0; y > 0','x < 0; y < 0','x > 0; y < 0']
number_q = int(input('Input numbers qwater:'))
if number_q < 1 or number_q > 4:
    print('number qwater incorrect!')
else:
    print(f'diapazon cord {number_q} qwater {coord[number_q]}')













                                                                          





    
