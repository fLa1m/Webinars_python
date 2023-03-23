# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

from random import randint

list = [1, 1, 2, 0, -1, 3, 4, 4]
uniq_list = []
print(list)
for i in range(len(list)):
    if list[i] not in uniq_list:
        uniq_list.append(list[i])
print(len(uniq_list))

# Вариант с семинара

l = [1, 1, 2, 0, -1, 3, 4, 4]
list = set(l)
print(len(list))
