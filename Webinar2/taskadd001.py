# даны натуральные числа от 35 до 87. Найти и напечатать те из них,
# которые при делении на 7 дают остаток 1, 2 или 5.
numbers = []
for i in range(35, 88):
    if i % 7 == 1 or i % 7 == 2 or i % 7 == 5:  # if i % 7 in (1, 2, 5)
        numbers.append(i)
print(*numbers)