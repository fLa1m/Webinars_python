# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10^5. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:     Вывод:
# 300       220 284


# def friendly_digits(num: int):
#     array = [_ for _ in range(num + 1)]
#     friend_numbers = set()
#     div_n = 0
#     div_m = 0
#     # print(array)
#     for n in range(len(array)):
#         # print(f"n={array[n]}")
#         for i in range(1, n):
#             # print(f"i={array[i]}")
#             if array[n] % array[i] == 0:
#                 div_n += array[i]
#                 # print(f"div_n={div_n}")
#         # print(f"-div_n={div_n}-")
#         m = div_n
#         for j in range(1, div_n):
#             # print(f"j={j}")
#             if div_n % j == 0:
#                 div_m += j
#                 # print(f"div_m={div_m}")
#             if div_m == n and m != n:
#                 friend_numbers.add(n)
#                 friend_numbers.add(div_n)
#         div_n = 0
#         div_m = 0
#         # print(f"div_n={div_n},div_m={div_m}")
#     print(friend_numbers)


# k = int(input())
# friendly_digits(k)


def sum_dividers(n):
    return sum(x for x in range(1, n // 2 + 1) if n % x == 0)


k = int(input())

for i in range(1, k + 1):
    potentially_friendly = sum_dividers(i)
    if i < potentially_friendly and i == sum_dividers(potentially_friendly):
        print(i, potentially_friendly)
