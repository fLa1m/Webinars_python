# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

import input_num


def rev(size_n: int):
    if size_n == 1:
        return [input_num("and last number: ")]
    return [input_num("input number: ")] + rev(size_n - 1)


def rev2(n: int):
    i = input("Введите число: ")
    if n == 1:
        print(i, end=" ")
    else:
        rev2(n - 1)
        print(i, end=" ")


n = int(input("Please input number: "))

print(*rev(n)[::-1])

rev2(n)
