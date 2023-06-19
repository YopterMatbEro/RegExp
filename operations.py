import re
from pprint import pprint

def change_phone(id, id1, change_contacts_list, pattern, contacts_list, match):
    if change_contacts_list[id1][5]:  # полный телефон (группа 6, в списке индекс 5)
        if change_contacts_list[id1][12]:  # добавочный номер
            subst_pattern = r"+7(\8)\9-\10-\11 \12.\13"
            change_contacts_list[id1][5] = pattern.sub(subst_pattern, contacts_list[id])
            [change_contacts_list[id1].remove(match.group(i)) for i in [7, 8, 9, 10, 11, 12, 13]]
        else:
            subst_pattern = r"+7(\8)\9-\10-\11"
            change_contacts_list[id1][5] = pattern.sub(subst_pattern, contacts_list[id])
            [change_contacts_list[id1].remove(match.group(i)) for i in [7, 8, 9, 10, 11, 12, 13]]


def correction_of_contacts(contacts_list):
    change_contacts_list = []
    count = 0  # кол-во объединённых контактов в итоговом списке
    for id, item in enumerate(contacts_list):  # корректируем каждую строку по очереди
        contacts_list[id] = ','.join(item)
        pattern = re.compile(
            '^(\w+)?[\s,]+(\w+)?[\s,]+(\w+)?[\s,]+(\w+)?[s,]*([a-zA-Zа-яА-Я\s]*[–]?[a-zA-Zа-яА-Я\s]*)[\s*,](([+]?\d*)[\s(]*(\d{3})[\s)-]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})[\s+(]*([\w+]+)?[\s.]*(\d+)?)?[)]?[\s,]([a-zA-Zа-яА-Я.@0-9]+)?')
        match = pattern.search(contacts_list[id])

        # Добавляем в виде списка в уже отсортированном, по группам, виде (Ф,И,О, и т.д.)
        # 1. ищем индекс возможных совпадений в конечном списке
        id1 = [change_contacts_list.index(change_contacts_list[i]) for i in range(len(change_contacts_list))
               if match.group(1) in change_contacts_list[i][0]]

        if id1:  # [n] - index уже имеющегося контакта с этой фамилией
            count += 1  # + объединённый контакт, для вычитания из id и попадания по верному индексу в новом списке
            # поиск и заполнение новых данных, отсутствующих у первичного контакта
            for elem in change_contacts_list[id1[0]]:
                if elem:
                    continue
                else:
                    # определяем позицию недостающих данных
                    position = change_contacts_list[id1[0]].index(elem)
                    change_contacts_list[id1[0]][position] = match.group(position + 1)  # добавляем из группы
            # подгоняем номер телефона под установленный шаблон, в случае, если он не прописан
            if change_contacts_list[id1[0]][5]:
                continue
            else:
                change_phone(id, id1[0], change_contacts_list, pattern, contacts_list, match)
        # 2. добавляем, если совпадений нет
        else:  # [] - not id1
            change_contacts_list.append([*match.groups()])
            change_phone(id, id - count, change_contacts_list, pattern, contacts_list, match)
    change_contacts_list.insert(0, ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'])

    return change_contacts_list
