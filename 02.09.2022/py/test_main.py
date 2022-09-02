from xmlrpc.client import Boolean
import main


test_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
test_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
test_4 = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
test_5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_create_phone_number_1():
    assert main.create_phone_number_1(test_1) == "(123) 456-7890"
    assert main.create_phone_number_1(test_2) == "(111) 111-1111"
    assert main.create_phone_number_1(test_3) == "(123) 456-7890"
    assert main.create_phone_number_1(test_4) == "(023) 056-0890"
    assert main.create_phone_number_1(test_5) == "(000) 000-0000"


def test_create_phone_number_2():
    assert main.create_phone_number_2(test_1) == "(123) 456-7890"
    assert main.create_phone_number_2(test_2) == "(111) 111-1111"
    assert main.create_phone_number_2(test_3) == "(123) 456-7890"
    assert main.create_phone_number_2(test_4) == "(023) 056-0890"
    assert main.create_phone_number_2(test_5) == "(000) 000-0000"


def test_create_phone_number_3():
    assert main.create_phone_number_3(test_1) == "(123) 456-7890"
    assert main.create_phone_number_3(test_2) == "(111) 111-1111"
    assert main.create_phone_number_3(test_3) == "(123) 456-7890"
    assert main.create_phone_number_3(test_4) == "(023) 056-0890"
    assert main.create_phone_number_3(test_5) == "(000) 000-0000"

test_create_phone_number_1()
test_create_phone_number_2()
test_create_phone_number_3()
