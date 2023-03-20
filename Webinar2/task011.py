# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

a = int(input("Введите число: "))
count = 2
first_digit = 0
second_digit = 1
fibonachi_number = 0
if a > 1:
    while fibonachi_number < a:
        fibonachi_number = first_digit + second_digit
        first_digit = second_digit
        second_digit = fibonachi_number
        count += 1
    if fibonachi_number == a:
        print(count)
    else:
        print(-1)
else:
    print("Введите число > 1")
