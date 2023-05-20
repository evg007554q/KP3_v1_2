import json
import datetime
from operator import itemgetter

File_operations = '../operations.json'
def Open_operations(File_name = File_operations):
    "возращаем список операций из файла"
    with open(File_name,'r',encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data

def Select_operations(orders_type, File_name= File_operations):
    "Возращает список операций по типу сортировка по дате"
    operations= Open_operations()
    oper_filtered = []
    for item in operations:
        if 'state' in item:
            if item['state'] == orders_type:
                oper_filtered.append(item)

    return sorted(oper_filtered, key = itemgetter('date'))

def mask_Account(acc):
    """Возращает серытый номер
    Счет return '**XXXX'
    Карта return 'XXXX XX** **** XXXX'
    """
    #определи счет это или карта
    if acc.find("Счет") == 0:
        itAcc = True
    else:
        itAcc = False

    acc_num = ""
    for c in acc:
        if c.isdigit():
           acc_num += c

    if itAcc:
        return '**' + acc_num[len(acc_num)-4:]
    else:
        return acc_num[:4] + ' ' + acc_num[4:6] + '** **** ' + acc_num[12:]

def print_top_operations(operations_count=5,orders_type="EXECUTED"):
    "Выводит заданое количество последних операций по указаному типу"
    operations = Select_operations(orders_type)
    message_operations=""
    for item in range(min(len(operations),operations_count)):
        oper=operations[item]
        #пример
        #14.10.2018 Перевод  организации
        #Visa Platinum 7000 79** **** 6361 -> Счет **9638
        #82771.72  руб.
        #print(
        #    f'{ datetime.datetime.strptime(oper["date"],"%Y-%m-%dT%H:%M:%S.%f").date() } {oper["description"]}'
        #)
        message_operations +=f'{ datetime.datetime.strptime(oper["date"],"%Y-%m-%dT%H:%M:%S.%f").date() } {oper["description"]} \n'
        if 'from' in oper:
            message_operations +=f'{ mask_Account(oper["from"]) } -> Счет {mask_Account(oper["to"])} \n'
        else:
            message_operations += f'Счет {mask_Account(oper["to"])} \n'
        message_operations +=f'{ oper["operationAmount"]["amount"] } {oper["operationAmount"]["currency"]["name"]} \n'

        message_operations += f'\n'

    return message_operations

