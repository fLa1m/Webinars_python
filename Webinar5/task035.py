# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def easy_num(num):
    if num in (1, 2):
        return "yes"
    for i in range(2, num // 2):
        if num % i == 0:
            return "no"
        else:
            return "yes"


print(easy_num(18014398241046527))

# Решения с семинара


# def is_prime(n, i=2):
#     if n == 2 or i > int(n**0.5):
#         return True
#     if n % i == 0:
#         return False
#     return is_prime(n, i + 1)


# n = int(input("Введите число: "))
# if is_prime(n):
#     print(n, "является простым числом")
# else:
#     print(n, "не является простым числом")
