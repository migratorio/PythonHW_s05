# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

f = open('task39fail_source.txt', 'r', encoding='UTF-8')
source_line = f.read()
print('Исходная строка:', source_line)
source_line = source_line + ' '

"""Кодируем:"""
"""Вариант 1"""
# count = 1
# compress = ''
#
# for i in range(1, len(source_line)):
#     if source_line[i - 1] == source_line[i]:
#         count += 1
#     else:
#         compress = compress + str(count) + source_line[i - 1]
#         count = 1

"""Вариант 2"""
compress = ''
item0 = ''
id0 = 1
for id, item in enumerate(source_line, 1):
    if item != item0:
        if id - id0 == 0:
            item0 = item
            continue
        compress = compress + str(id - id0) + item0
        item0 = item
        id0 = id


f = open('task39fail_compress.txt', 'w')
f.write(compress)
f.close()


"""Декодируем"""
f = open('task39fail_compress.txt', 'r', encoding='UTF-8')
compress = f.read()
print('сжатый список:  ', compress)
source_line = ''
str_count = ''

for el in compress:
    if el.isdigit():
        str_count = str_count + el
    else:
        source_line = source_line + el * int(str_count)
        str_count = ''
print('Декодировано:   ', source_line)
f = open('task39fail_dec.txt', 'w')
f.write(compress)


