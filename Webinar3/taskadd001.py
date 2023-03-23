# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Пример ввода:
# a a a b c a a d c d d
# Пример вывода:
# a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# 0 1 2 3 4 5 6 7 8 9 10
string = "a a a b c a a d c d d"
chars = string.replace(" ", "")
for i in range(len(chars)):
    if chars.count(chars[i], 0, i) == 0:
        print(chars[i], end=" ")
    else:
        print(f"{chars[i]}_{chars.count(chars[i], 0, i)}", end=" ")
print()
print()

# Мое первое решение

string = "Я хочу стать программистом"
chars = set()
for i in string:
    chars.add(i.lower())
count = 0
for i in chars:
    for j in string:
        if i == j.lower():
            count += 1
    print(f"'{i}'_{count}", end=" ")
    count = 0
print()
print()

# Решение через словари с семинара

sourse = "a a a b c a a d c d d".split()
count_dict = {}


def transfer(source_list: list):
    for el in source_list:
        if el not in count_dict:
            count_dict[el] = 0
            yield el
            continue
        count_dict[el] += 1
        yield f"{el}_{count_dict[el]}"


[print(_, end=" ") for _ in transfer(sourse)]
