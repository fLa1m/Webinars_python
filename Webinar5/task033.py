# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n = int(input())
array = sorted([randint(1, 5) for _ in range(n)])
print(array)
max_num = max(array)
min_num = min(array)
i = -1
while array[i] == max_num:
    array[i] = min_num
    i -= 1
print(array)
