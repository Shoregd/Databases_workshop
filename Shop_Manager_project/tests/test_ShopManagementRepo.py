from lib.Item import Item
from lib.Order import Order
from lib.ShopManagementRepo import ShopManagementRepository

def test_list_items_returns_item_list(db_connection):
    db_connection.seed('seeds/shop_manager_test.sql')
    repository = ShopManagementRepository(db_connection)
    result = repository.list_items()
    assert result == [
                'Item 1: Taco Unit Price: £1.25 In Stock: 75',
                'Item 2: Burrito Unit Price: £2.25 In Stock: 60',
                'Item 3: Enchilada Unit Price: £3.75 In Stock: 82',
                'Item 4: Tortilla Unit Price: £0.75 In Stock: 157',
                'Item 5: Cheese Unit Price: £1.90 In Stock: 286',
                'Item 6: Guacamole Unit Price: £1.60 In Stock: 184',
                'Item 7: Sour Cream Unit Price: £1.00 In Stock: 42'
    ]
def test_list_orders_returns_order_list(db_connection):
    db_connection.seed('seeds/shop_manager_test.sql')
    repository = ShopManagementRepository(db_connection)
    result = repository.list_orders()
    assert result == [
                    'Order Number 1 for: Greg Smith Order Date: 2023-11-02',
                    'Order Number 2 for: John Doe Order Date: 2023-11-17',
                    'Order Number 3 for: Terry Bloggs Order Date: 2023-11-12',
                    ]
def test_get_order_info_returns_information_about_correct_order_with_items(db_connection):
    db_connection.seed('seeds/shop_manager_test.sql')
    repository = ShopManagementRepository(db_connection)
    result = repository.get_order_info(1)
    assert result ==[
                    'Order Number 1 for: Greg Smith Order Date: 2023-11-02',
                    [
                        'Item 1: Taco',
                        'Item 5: Cheese',
                        'Item 6: Guacamole',
                        'Item 7: Sour Cream'
                    ]
    ]
def test_create_item_updates_database_and_returns_correctly(db_connection):
    db_connection.seed('seeds/shop_manager_test.sql')
    repository = ShopManagementRepository(db_connection)
    assert repository.create_item('Olives',0.45,300) == 'New Item added: Item 8: Olives Unit Price: £0.45 In Stock: 300'
    result = repository.list_items()
    assert result == [
                'Item 1: Taco Unit Price: £1.25 In Stock: 75',
                'Item 2: Burrito Unit Price: £2.25 In Stock: 60',
                'Item 3: Enchilada Unit Price: £3.75 In Stock: 82',
                'Item 4: Tortilla Unit Price: £0.75 In Stock: 157',
                'Item 5: Cheese Unit Price: £1.90 In Stock: 286',
                'Item 6: Guacamole Unit Price: £1.60 In Stock: 184',
                'Item 7: Sour Cream Unit Price: £1.00 In Stock: 42',
                'Item 8: Olives Unit Price: £0.45 In Stock: 300'
    ]

def test_create_order_adds_order_to_list_and_updates_join_table(db_connection):
    db_connection.seed('seeds/shop_manager_test.sql')
    repository = ShopManagementRepository(db_connection)
    assert repository.create_order('Karen Street','2023-12-01','4,5,6') ==[
        'New Order added: Order Number 4 for: Karen Street Order Date: 2023-12-01',
        [
            'Item 4: Tortilla',
            'Item 5: Cheese',
            'Item 6: Guacamole'
        ]
    ]




