from pprint import pprint
import re
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv
from operations import correction_of_contacts

def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)

    # 1. Выполните пункты 1-3 задания.
    changed_list = correction_of_contacts(contacts_list[1:])  # исключаем первую строку, т.к. она статична
    print(*changed_list, sep='\n')

    # print(f'''{contacts_list[0][0]:^20} | {contacts_list[0][1]:^20} | {contacts_list[0][2]:^20} | {contacts_list[0][3]:^10}\
    #  | {contacts_list[0][4]:^143} | {contacts_list[0][5]:^27}| {contacts_list[0][6]:^21}''')
    # print('+' + '-'*20 + '+' + '-'*22 + '+' + '-'*22 + '+' + '-'*18 + '+' + '-'*145 + '+' + '-'*28 + '+' + '-'*21)
    # for l, f, s, o, p, ph, e in changed_list:
    #     print(f'{l:^20} | {f:^20} | {s:^20} | {o:^16} | {p:^143} | {ph:^26} | {e:^21}')

    # 2. Сохраните получившиеся данные в другой файл.
    # Код для записи файла в формате CSV:
    # with open("phonebook.csv", "w") as f:
    #     datawriter = csv.writer(f, delimiter=',')
    #
    #     # Вместо contacts_list подставьте свой список:
    #     datawriter.writerows(contacts_list)


if __name__ == '__main__':
    main()
