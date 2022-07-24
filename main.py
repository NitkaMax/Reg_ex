import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv


PATTERN_PHONE = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'

with open('phonebook_raw.csv', encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
def main(contacts_list: list):
    new_list = list()
    for item in contacts_list:
        full_name = ' '.join(item[:3]).split(' ')
        result = [full_name[0],full_name[1],full_name[2],item[3],item[4],
                 re.sub(PATTERN_PHONE,PHONE_SUB, item[5]),
                 item[6]]
        new_list.append(result)
    return union(new_list)
    

def union (contacts: list):
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    result_list = list()
    for x in contacts:
        if x not in result_list:
            result_list.append(x)
    return result_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w",encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(main(contacts_list))