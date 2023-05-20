from Utils import operations


def test_mask_Account():
    assert operations.mask_Account("Счет 75106830613657916952")=="Счет **6952"
    assert operations.mask_Account("Visa Classic 6831982476737658")=="Visa Classic 6831 98** **** 7658"

def test_Open_operations():
    assert operations.Open_operations("oper_test.josn") ==    [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',      'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},      'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',      'to': 'Счет 74489636417521191160'}, {}]


def test_Select_operations():
    assert operations.Select_operations('EXECUTED',"oper_test.josn") ==    [{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',      'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},      'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',      'to': 'Счет 74489636417521191160'}]

def test_Sprint_top_operations():
    assert operations.print_top_operations("oper_test.josn") == '2019-03-23 Перевод со счета на счет \nСчет **4719 -> Счет **1160 \n43318.34 руб. \n\n'