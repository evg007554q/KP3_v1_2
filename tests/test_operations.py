from Utils import operations


def test_mask_Account():
    assert operations.mask_Account("Счет 75106830613657916952")=="**6952"
    assert operations.mask_Account("Visa Classic 6831982476737658")=="6831 98** **** 7658"

def test_Open_operations():
    ...