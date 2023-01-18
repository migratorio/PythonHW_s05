# Напишите программу, удаляющую из текста все слова, содержащие "абв"

with open('file_text38.txt', 'r', encoding='UTF-8') as f:
    some_list = f.read().split()
    print(some_list)
new_list = []
# for i in range(len(some_list)):
#     presence = 1
#     for x in some_list[i]:
#         if x == 'а' or x == 'б' or x == 'в':
#             presence = 0
#             break
#     if presence == 1:
#         new_list.append(some_list[i])
# print(new_list)

for word in some_list:
    temp_list = list(filter(lambda x: x == 'а' or x == 'б' or x == 'в', word))
    if len(temp_list) == 0:
        new_list.append(word)
print(new_list)


