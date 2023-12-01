from lib.Item import Item

def test_init_correct():
    test_item = Item(1,'Taco',1.75,89)
    assert test_item.id == 1
    assert test_item.name == 'Taco'
    assert test_item.unit_price == 1.75
    assert test_item.quantity == 89

def test_format_correctly():
    test_item = Item(1,'Taco',1.75,89)
    assert str(test_item) == 'Item 1: Taco Unit Price: £1.75 In Stock: 89'
def test_format_correct_with_zeros():
    test_item = Item(1,'Taco',1.00,89)
    assert str(test_item) == 'Item 1: Taco Unit Price: £1.00 In Stock: 89'

def test_object_testing():
    test_item = Item(1,'Taco',1.75,89)
    assert test_item == Item(1,'Taco',1.75,89)
    