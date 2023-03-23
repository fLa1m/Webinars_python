# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

n = [1, 2, 3, 4, 5]
k = int(input())
print(n)
list = []
length = len(n)
if length < k:
    k = k % length
for i in range(k, len(n)):
    list.append(n[i])
for i in range(k):
    list.append(n[i])
print(list)

# Вариант с семинара

k = int(input())
values = [1, 2, 3, 4, 5]
length = len(values)
if length < k:
    k = k % length
print(values)
print(values[k:] + values[:k])
