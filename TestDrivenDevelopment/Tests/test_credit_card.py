from TestDrivenDevelopment.credit_class import CreditCard
import pytest

def test_charge_credit_card():
    card = CreditCard('Alex', 100, 1000)

    # charge cannot exceed limit 
    assert card.charge(1000) == False

def test_balance_correct():
    # check if balance is correct after charged
    card = CreditCard('Alex', 100, 1000)
    card.charge(100)
    assert card.balance == 200




@pytest.mark.parametrize("balance", [5, 10, 15, 20])
@pytest.mark.parametrize("limit", [1_000, 2_000, 3_000, 4_000])
def test_charge_credit_card(balance, limit):
    card = CreditCard('Alex', balance, limit)

    # charge cannot exceed limit 
    assert card.charge(limit) == False
