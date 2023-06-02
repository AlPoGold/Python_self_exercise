# 1. Игра Fizz-Buzz
# Есть детская игра FizzBuzz, где нужно называть числа подряд, соблюдая всего три правила:
# Если число делится на 3, вместо него надо сказать «Fizz».
# Если число делится на 5, вместо него надо сказать «Buzz».
# А если число делится одновременно на 3 и на 5, то надо вместо него сказать «FizzBuzz».
# На вход подается число num, нужно вывести числа или слова по порядку от 1 до num (включительно) согласно правилам игры
#
# num = int(input())
#
# numbers = [i for i in range(1, num+1)]
# for n in numbers:
#     if n%(3*5)==0:
#         print('FizzBazz')
#     elif n%3==0:
#         print('Fizz')
#     elif n%5==0:
#         print('Buzz')
#     else:
#         print(n)

# 2. Какого цвета клетка
# На вход подается обозначение шахматной клетки, необходимо вывести ее цвет
# dict_cell = {
#     'a': 0,
#     'b' : 1,
#     'c' : 2,
#     'd' : 3,
#     'e' : 4,
#     'f' : 5,
#     'g' : 6,
#     'h' : 7
#
# }
# board = [[0]*8 for _ in range(8)]
# cell = input()

#0 - white
#1 - black
# for i in range(8): #rows - nums
#     for j in range(8): #cols - letters
#         if j%2==1 and (7-i)%2==1:
#             board[i][j] = 1
#         elif j%2==0 and (7-i)%2==0:
#             board[i][j] = 1
#
# print(*board, sep='\n')
#
# x, y = [char for char in cell]
# letter = dict_cell[x]
# number = 8-int(y)
#
# if board[number][letter]==1:
#     print('black')
# else:
#     print('white')


#
# 3. Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка
# import random as r
# numbers = [r.randint(1, 10) for _ in range(100)]
# print(*numbers)
#
# uniq_list = list(set(numbers))
#
# print(*uniq_list)

#
# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи (можно прочитать в wiki что это)
#числа негафибоначчи — отрицательно индексированные элементы последовательности чисел Фибоначчи
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    fib = [1] * (n)
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

print(fibonacci(8))

def negafibonacci(n):
    arr = [1] * n
    arr[1] = -1

    for i in range(2, n):
        arr[i] = arr[i-2] - arr[i-1]
    arr.reverse()
    return arr

print(negafibonacci(8)+[0]+fibonacci(8))