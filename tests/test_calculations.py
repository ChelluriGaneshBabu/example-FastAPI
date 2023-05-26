from app.calculations import add,sub,mul,div,BankAccount,Insufficient_amount
import pytest


# def test_add():
#     print("testing successfully")
#     assert add(5,3) == 8

# def test_sub():
#     assert sub(5,3) == 2

# def test_mul():
#     assert mul(5,3) == 15

# def test_div():
#     assert div(6,3) == 2

# @pytest.mark.parametrize("num1,num2,expected",[
#     (3,2,5),
#     (7,1,8),
#     (12,3,15)
# ])

# def test_add2(num1,num2,expected):
#     assert add(num1,num2) == expected


# def test_bank_set_amount():
#     bank_account = BankAccount(50)
#     assert bank_account.balance == 50

# def test_bank_default_amount():
#     bank_account = BankAccount()
#     assert  bank_account.balance == 0

# def test_withdraw():
#      bank_account =BankAccount(100)
#      bank_account.withdraw(40)
#      assert  bank_account.balance == 60

# def test_deposit():
#     bank_account = BankAccount(200)
#     bank_account.deposit(50)
#     assert bank_account.balance == 250

# def test_collect_interest():
#     bank_account = BankAccount(50)
#     bank_account.collect_interest()
#     assert round(bank_account.balance,6) == 55

@pytest.fixture
def zero_bank_account():
    print("default amount is empty")
    return BankAccount()


def test_bank_default_amount(zero_bank_account):
    assert  zero_bank_account.balance == 0

@pytest.fixture
def bank_account():
    return BankAccount(50)

def test_bank_set_amount(bank_account):
    assert bank_account.balance == 50

def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 100

def test_withdraw(bank_account):
    bank_account.withdraw(25)
    assert bank_account.balance == 25

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55
    
@pytest.mark.parametrize("deposited,withdrew,expected",[
    (2000,500,1500),
    (100,25,75),
    
])
def test_bank_transaction(zero_bank_account,deposited,withdrew,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(Insufficient_amount):
        bank_account.withdraw(200)