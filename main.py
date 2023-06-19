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
    # print(*changed_list, sep='\n')

    # 2. Сохраните получившиеся данные в другой файл.
    # Код для записи файла в формате CSV:
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')

        # Вместо contacts_list подставьте свой список:
        datawriter.writerows(changed_list)


if __name__ == '__main__':
    main()
