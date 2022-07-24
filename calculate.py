# ### Завдання 1

# Файл: `calculate.py`
# Оцінка: 50

# Покращити програму `calculate` (файл [calculate_raw.py](https://github.com/vaiol/python/blob/main/L3/src/calculate_raw.py)) яка була створена на лекції функцією виконання арифметичної операції в одній строчці. А також розширена новими арифметичними операціями.  
# Можна використовувати вихідний код вашої програми виконання відповідного ДЗ, але попередньо повинні бути виправлені помилки.  
# Програма має задовольняти наступні потреби:  
# 1. Створити файл `calculate.py` 
# 1. Программа повина зчитувати аргументи командної строки (за допомогою модуля `sys`) і виконувати арифметичні операції.
# 1. Необхідна підтримка 5 базових арифметичних операцій: `+`, `-`, `*`, `/`, `%` (додавання, віднімання, множення, ділення, остача від ділення). Додано нову операцію - %.
# 1. Результат виконання арифметичної операції потрібно виводити у консоль.
# 1. Программа повинна адекватно оброблювати помилки.
# 1. Программа повинна запускатись наступним чином: `python calculate.py 2 + 2` або `python calculate.py 2+2`
# 1. Приклади:
#     1. `python calculate.py 2 + 2` -> 4
#     1. `python calculate.py 2 - 200` -> -198
#     1.  `python calculate.py 2 * 8` -> 16
#     1.  `python calculate.py 200 / 2` -> 100 
#     1. `python calculate.py 3+3` -> 6
#     1. `python calculate.py 100-20` -> 80
#     1.  `python calculate.py 4*4` -> 16
#     1.  `python calculate.py 25/2` -> 12.5 
# 1. Заборонено використовувати `eval` для обчислення результату.
# 1. Повинна бути створена і використана функція обчислення `def calc(left_operand, right_operand, operation)` яка повертає результат арифметичного обчислення.



# Додав ще цілочисельне ділення.
# python calculate.py 2+2  - цей варіант коли (лів.операнд,оператор, прав.операнд - розміщені за 1 індексом) не має пропуску між лівим операндом,оператором і правим операндом у мене не працює, поки що(((((
#  Як розділити, у мене поки що є ідея "2+2" наприклад розбити на три частини по індексу, тоді буде працювати, але якщо чисел буде більше і відповідно індесів, тоді помилка(((


import sys
left_operand = sys.argv[1]
right_operand = sys.argv[3]
operation = sys.argv[2]
def calculate(left_operand, right_operand, operation):
    left_operand = int(left_operand)
    right_operand = int(right_operand)
    allowed_operations = ['+', '-', '/', '*', '%', '//' ]
    if len(sys.argv) != 4:
        print('Arg len should be 4')
        sys.exit()
    if operation not in allowed_operations:
        print('Operation is not allowed')
        sys.exit()
    if operation == '/' and right_operand == 0:
        print('Division by zero is not allowed')
        sys.exit()
    elif operation == '+':
        addition = '{} + {} = '.format(left_operand, right_operand)
        print(left_operand + right_operand)
        sys.exit()
    elif operation == '-':
        subtraction = '{} - {} = '.format(left_operand, right_operand)
        print(left_operand - right_operand)
        sys.exit()
    elif operation == '*':
        multiplication = '{} * {} = '.format(left_operand, right_operand)
        print(left_operand * right_operand)
        sys.exit()
    elif operation == '/':
        division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand / right_operand)
        sys.exit()
    elif operation == '%':
        remainder_from_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand / right_operand)
        sys.exit()
    elif operation == '//':
        integer_division = '{} / {} = '.format(left_operand, right_operand)
        print(left_operand // right_operand)
        sys.exit()
calculate(left_operand, right_operand, operation)
# Додав ще цілочисельне ділення












# import sys



# if len(sys.argv) != 4:
#     print('Arg len should be 4')
#     sys.exit()
# left_operand = sys.argv[1]
# right_operand = sys.argv[3]
# operation = sys.argv[2]
# allowed_operations = ['+', '-', '/', '*', '%']
# if operation not in allowed_operations:
#     print('Operation is not allowed')
#     sys.exit()
# try:
#     left_operand = int(left_operand)
#     right_operand = int(right_operand)
# except ValueError:
#     print('Left and Right operands must be int')
#     sys.exit()
# if operation == '/' and right_operand == 0:
#     print('Division by zero is not allowed')
#     sys.exit()

## Option 1
# if operation == '*':
#     print(left_operand * right_operand)
# elif operation == '+':
#     print(left_operand + right_operand)

## Option 2
# match operation:
#     case '*':
#         print(left_operand * right_operand)
#     case '+':
#         print(left_operand + right_operand)


## Option 3
# print(eval(f'{left_operand}{operation}{right_operand}'))


# def perform_operation(left, right, operation)
#     return ()



# # import sys
# # left_operand1 = sys.argv[1:]
# left_operand1 = input()
# # right_operand1 = sys.argv[3:]
# # left_operand1 = input()
# # operation = sys.argv[2:]
# # operation = input()
# left_ope = left_operand1[0]
# oper = left_operand1[1]
# right_ope = left_operand1[2]
# left_operand = int(left_ope)
# right_operand = int(right_ope)
# operation = str(oper)
# def calc(left_oper, right_ope, oper):
#     if len(sys.argv) != 4:
#         print('Arg len should be 4')
#         sys.exit()
#     allowed_operations = ['+', '-', '/', '*', '%' ]
#     if operation not in allowed_operations:
#         print('Operation is not allowed')
#         sys.exit()
#     if operation == '/' and right_operand == 0:
#         print('Division by zero is not allowed')
#         sys.exit()
#     elif operation == '+':
#         print(left_operand + right_operand)
#         sys.exit()
#     elif operation == '-':
#         print(left_operand - right_operand)
#         sys.exit()
#     elif operation == '/':
#         print(left_operand - right_operand)
#         sys.exit()
#     elif operation == '*':
#         print(left_operand * right_operand)
#         sys.exit()
#     elif operation == '%':
#         print(left_operand % right_operand)
#         sys.exit()
# calc(left_oper, right_ope, oper)


# except ValueError:
#     print('Left and Right operands must be int')
#     sys.exit()

# if operation == '/' and right_operand == 0:
#     print('Division by zero is not allowed')
#     sys.exit()

# # Option 1
# if operation == '*':
#     print(left_operand * right_operand)
# elif operation == '+':
#     print(left_operand + right_operand)

# # Option 2
# match operation:
#     case '*':
#         print(left_operand * right_operand)
#     case '+':
#         print(left_operand + right_operand)


# # Option 3
# print(eval(f'{left_operand}{operation}{right_operand}'))


# def perform_operation(left, right, operation)
#     return ()




# import sys
# left_operand = int(sys.argv[1])
# right_operand = int(sys.argv[3])
# operation = sys.argv[2]
# def calc(left_operand, right_operand, operation):
#     if len(sys.argv) != 4:
#         print('Arg len should be 4')
#         sys.exit()
#     allowed_operations = ['+', '-', '/', '*', '%', '//' ]
#     if operation not in allowed_operations:
#         print('Operation is not allowed')
#         sys.exit()
#     if operation == '/' and right_operand == 0:
#         print('Division by zero is not allowed')
#         sys.exit()
#     elif operation == '+':
#         print(left_operand + right_operand)
#         sys.exit()
#     elif operation == '-':
#         print(left_operand - right_operand)
#         sys.exit()
#     elif operation == '/':
#         print(left_operand - right_operand)
#         sys.exit()
#     elif operation == '*':
#         print(left_operand * right_operand)
#         sys.exit()
#     elif operation == '%':
#         print(left_operand % right_operand)
#         sys.exit()
#     elif operation == '//':
#         print(left_operand // right_operand)
#         sys.exit()
#     def again():
#         print('Do you want to calculate again? Please type Y for YES or N for NO.')
#         if calc_again.upper() == 'Y':
#             calculate()
#         elif calc_again.upper() == 'N':
#             print('See you later.')
#         else:
#             again()
# calc(left_operand, right_operand, operation)