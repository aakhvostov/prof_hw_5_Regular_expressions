import re
import csv
from itertools import groupby


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
name_pattern = re.compile(r'(\b[А-Яa-z][а-яa-z]+)[ ,](\b[А-Яa-z][а-яa-z]+)?[ ,]?(\b[А-Яa-z][а-яa-z]+)?')
tel_pattern = re.compile(r'(\+7|8)[- ]?\(?(\d+)\)?[ -]?(\d+)?[ -]?(\d+)?[ -]?(\d+)?(\s+)?\(?(доб\. )?(\d+)?\)?')

for elem in contacts_list:
    full_name = ",".join(elem[:3])
    name = name_pattern.findall(full_name)
    tel = tel_pattern.sub(r"+7(\2)\3\4\5\6\7\8", elem[5])
    # print(f'{elem[0]} меняем на {name[0][0]}\n{elem[1]} меняем на {name[0][1]}\n'
    #       f'{elem[2]} меняем на {name[0][2]}\n{elem[5]} меняем на {tel}\n')
    elem[0], elem[1], elem[2] = name[0][0], name[0][1], name[0][2]
    elem[5] = tel
# print(contacts_list)
remove_index = set()
for i in range(len(contacts_list)):
    # print(f'i = {i}')
    for j in range(i, len(contacts_list)):
        Flag = False
        # print(f'j = {j}')
        if i != j:
            for nums in zip(contacts_list[i][:2], contacts_list[j][:2]):
                Flag = len(list(groupby(nums))) == 1
                if Flag:
                    for k in range(len(contacts_list[i])):
                        # print('k = ',k)
                        # print(contacts_list[i][k])
                        if not contacts_list[i][k]:
                            # print('if not')
                            # print(contacts_list[j][k])
                            contacts_list[i][k] = contacts_list[j][k]
                            remove_index.add(j)

for i in remove_index:
    contacts_list.remove(contacts_list[i])

# print(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding='utf-8') as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(contacts_list)
