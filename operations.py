import re
from pprint import pprint

def change_phone(id, id1, change_contacts_list, pattern, contacts_list):
    if change_contacts_list[id1][5]:  # полный телефон (группа 6, в списке индекс 5)
        if change_contacts_list[id1][12]:  # добавочный номер
            subst_pattern = r"+7(\8)\9-\10-\11 \12.\13"
            change_contacts_list[id1][5] = pattern.sub(subst_pattern, contacts_list[id])
        # elif change_contacts_list[id][12] == '':
        else:
            subst_pattern = r"+7(\8)\9-\10-\11"
            change_contacts_list[id1][5] = pattern.sub(subst_pattern, contacts_list[id])


def correction2(contacts_list):
    change_contacts_list = []
    for id, item in enumerate(contacts_list):  # корректируем каждую строку по очереди
        contacts_list[id] = ','.join(item)
        pattern = re.compile(
            '^(\w+)?[\s,]+(\w+)?[\s,]+(\w+)?[\s,]+(\w+)?[s,]*([a-zA-Zа-яА-Я\s]*[–]?[a-zA-Zа-яА-Я\s]*)[\s*,](([+]?\d*)[\s(]*(\d{3})[\s)-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})[\s+(]*([\w+]+)?[\s.]*(\d+)?)?[)]?[\s,]([a-zA-Zа-яА-Я.@0-9]+)?')
        match = pattern.search(contacts_list[id])
        # Добавляем в виде списка в уже отсортированном, по группам, виде (Ф,И,О, и т.д.)
        # 1. ищем индекс возможных совпадений в конечном списке
        id1 = [change_contacts_list.index(change_contacts_list[i]) for i in range(len(change_contacts_list))
               if match.group(1) in change_contacts_list[i][0]]
        count = 0
        if id1:
            count += 1
            for elem in change_contacts_list[id1[0]]:
                if elem != '':
                    continue
                else:
                    position = change_contacts_list[id1[0]].index(elem)
                    change_contacts_list[id1[0]][position] = match.group(position + 1)
            change_phone(id, id1[0], change_contacts_list, pattern, contacts_list)
        # if match.group(1) in [change_contacts_list[i][0] for i in range(len(change_contacts_list))]:
        #     index = change_contacts_list.index(match.group(1))
        #     print(index)
        # else:
        # 2. добавляем, если совпадений нет
        else:
            change_contacts_list.append([*match.groups()])
            change_phone(id - count, id, change_contacts_list, pattern, contacts_list)
    pprint(change_contacts_list)
