import re
from pprint import pprint


def change_lastname(id, elem, index, tmp, change_contacts):
    if not elem:
        pass
    else:
        if len(elem.split(' ')) != 1:
            tmp = elem.split(' ')
        if tmp:
            change_contacts[index].append(tmp[id])
        else:
            pattern = re.compile("\w+")
            result = pattern.findall(elem)
            change_contacts[index].append(*result)
    return tmp, change_contacts


def change_firstname(id, elem, index, tmp, change_contacts):
    if tmp:
        change_contacts[index].append(tmp[id])
    elif len(elem.split(' ')) != 1:
        tmp = elem.split(' ')
    else:
        pattern = re.compile('\w+')
        result = pattern.findall(elem)
        change_contacts[index].extend(result)
    return tmp, change_contacts


def change_surname(id, elem, index, tmp, change_contacts):
    if tmp and len(tmp)-1 >= id:
        change_contacts[index].append(tmp[id])
    elif len(elem.split(' ')) != 1:
        tmp = elem.split(' ')
    else:
        pattern = re.compile('\w+')
        result = pattern.findall(elem)
        change_contacts[index].extend(result)
    return tmp, change_contacts


def change_phone(id, elem, index, change_contacts):
    if elem:
        pattern_add = re.compile('[\(]?([доб]+)[\.]?\s+(\d+)[\)]?')
        if re.findall(pattern_add, elem):
            subst_pattern_add = r" \1. \2"
            result = re.sub(pattern_add, subst_pattern_add, elem)
            change_contacts[index].append(result)
        pattern = re.compile('(\+7|7|8)?\s*[(]?(\d{3})[)]?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})')
        subst_pattern = r"+7(\2)\3-\4-\5"
        result = re.sub(pattern, subst_pattern, elem)
        change_contacts[index].append(result)
    else:
        pass


def correction2(contacts_list):
    for id, item in enumerate(contacts_list):
        contacts_list[id] = ', '.join(item)

    pattern_ln = re.compile('^\w+')
    print(contacts_list)


def correction_of_contacts(contacts_list):
    changed_contacts = []
    for index, data in enumerate(contacts_list):
        changed_contacts.append([])
        tmp = []
        for id, elem in enumerate(data):
            if id == 0:  # фамилия
                tmp, changed_contacts = change_lastname(id, elem, index, tmp, changed_contacts)
            elif id == 1:  # имя
                tmp, changed_contacts = change_firstname(id, elem, index, tmp, changed_contacts)
            elif id == 2:  # отчество
                tmp, changed_contacts = change_surname(id, elem, index, tmp, changed_contacts)
            elif id == 3:  # организация
                if elem:
                    changed_contacts[index].append(elem)
            elif id == 4:  # должность
                if elem:
                    changed_contacts[index].append(elem)
                else:
                    changed_contacts[index].append('-')
            elif id == 5:  # телефон
                change_phone(id, elem, index, changed_contacts)
            elif id == 6:  # емейл
                if elem:
                    changed_contacts[index].append(elem)
                else:
                    changed_contacts[index].append('-')
    return changed_contacts


def elimination_of_duplicates(contacts_list):
    count = 1
    changed_data = contacts_list.copy()
    result = []
    for i in range(len(contacts_list)-2):
        tmp = contacts_list[count].copy()
        for i in range(2, len(contacts_list)):
            if count != i and tmp[0] == contacts_list[i][0] and tmp[1] == contacts_list[i][1]:
                # if
                find_duplicates = list(zip(tmp, contacts_list[i]))
                for id, elem in enumerate(find_duplicates):
                    if elem[0] == elem[1]:
                        find_duplicates[id] = elem[0]
                    else:
                        if elem[0] == '-':
                            find_duplicates[id] = elem[1]
                        else:
                            find_duplicates[id] = elem[0]
                if find_duplicates in result:
                    continue
                else:
                    result.append(find_duplicates)
        count += 1

    for item in result:
        for id, (ln, fn, *args) in enumerate(contacts_list):
            if ln == item[0] and fn == item[1]:
                contacts_list[id] = item
            if item in contacts_list:
                pass
    pprint(contacts_list)
    # return contacts_list

