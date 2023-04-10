# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# Вывод:
# same


def same_by(f, val):
    flag = True
    for x in val:
        if f(x) == 1:
            flag = False
    return flag


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")

# Решение с семинара


def same_by2(characteristic, objects):
    result = set([characteristic(obj) for obj in objects])
    return len(result) <= 1


values = [0, 2, 10, 6]
if same_by2(lambda x: x % 2, values):
    print("same")
else:
    print("different")
