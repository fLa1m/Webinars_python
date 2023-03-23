# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list = [
    {"V": "S001"},
    {"V": "S002"},
    {"VI": "S001"},
    {"VI": "S005"},
    {"VII": " S005 "},
    {" V ": " S009 "},
    {" VIII ": " S007 "},
]
text = set()
for i in range(len(list)):
    dictionary = list[i]
    for k, v in dictionary.items():
        text.add(v.strip())
print(text)
