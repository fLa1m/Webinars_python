# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while.
# Input: 5
# Output: 120

n = int(input("Введите число: "))
factorial = 1
if n == 0:
    print(f"0! = {factorial}")
elif n > 0:
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"{n}! = {factorial}")
else:
    print("Введите число >= 0")
