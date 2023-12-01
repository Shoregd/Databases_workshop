from lib.Order import Order

def test_init_correct():
    test_Order = Order(1,'Taco','2023-11-30')
    assert test_Order.id == 1
    assert test_Order.customer_name == 'Taco'
    assert test_Order.order_date== '2023-11-30'

def test_format_correctly():
    test_Order = Order(1,'Taco','2023-11-30')
    assert str(test_Order) == 'Order Number 1 for: Taco Order Date: 2023-11-30'

def test_object_testing():
    test_Order = Order(1,'Taco','2023-11-30')
    assert test_Order == Order(1,'Taco','2023-11-30')
    