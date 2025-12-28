from hotel import *

def test_discount():
    price = 100       
    discount = 10     
    quantity = 2       
    assert (price * quantity) - ((price * quantity) * discount / 100) == 180
