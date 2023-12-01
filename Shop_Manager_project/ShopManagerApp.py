from lib.database_connection import DatabaseConnection
from lib.ShopManagementRepo import ShopManagementRepository
import datetime

connection = DatabaseConnection()
connection.connect()

connection.seed('seeds/shop_manager_test.sql')

repository = ShopManagementRepository(connection)

def update_list_lengths():
    rows = connection.execute('SELECT * FROM items')
    itemlength = len(rows)
    rows = connection.execute('SELECT * FROM orders')
    orderlength = len(rows)
    return itemlength,orderlength
itemlength, orderlength = update_list_lengths()


print('---Welcome to the ShopManager Programme.---\n\n')
choice = input('Type "help" for a list of corresponding commands: ')

def print_item_list():
    result = repository.list_items()
    print('Current Item list:\n')
    for item in result:
        print(f'    {item}')
    print('\n\n')
def get_item_info():
    itemname = None
    unit_price = None
    instock = None
    itemname = input('Please enter the name of the item: ')
    while unit_price == None or unit_price<= 0:
        try:
            unit_price = float(input('Please enter the price of the item(format £X.XX): £'))
            if unit_price <= 0:
                print('Price cannot be zero or below. please try again.')
        except:
            print('Invalid input please try again.') 
    while instock == None or instock <0:
        try:
            instock = int(input('Please enter the current stock level of the item: '))
            if instock < 0:
                print('Stock cannot be negative please try again.')
        except:
             print('Please enter a valid number for the stock level.')
    return repository.create_item(itemname,unit_price,instock)
def print_orders():
    result = repository.list_orders()
    print('Current Order list:\n')
    for item in result:
        print(f'    {item}')
    print('\n\n')
def print_order_info(orderinfo):
    result = orderinfo
    print('\n')
    for item in result:
        if type(item) != list:
            print(f'{item}\n')
        else:
            for data in item:
                print(f'    {data}')
    print('\n\n')

def get_new_order_info():
    print('\n')
    orderdate = None
    itemsordered = None
    customername = input('Please enter the customers name: ')
    while orderdate == None:
        try:
                orderdate = input('Please enter the order date (format YYYY-MM-DD): ')
                checkdate = orderdate.split('-')
                
        except:
                print('Invalid date entered. Please try again.')
                orderdate = None
    while itemsordered == None:
        print_item_list()
        try:
            itemsordered = input('Please enter the items to be ordered seperated by a comma(I.e 3,4,5): ')
            itemsordered.strip()
            checkitems = itemsordered.split(',')
            for item in checkitems:
                if int(item) <1 or int(item) > itemlength:
                    print('Please only choose valid item numbers from the list.')
                    itemsordered = None
        except:
            print('Invalid data entered. Please try again ensuring ONLY commas(,) seperate values.' )
            itemsordered = None
    print('\n\n')
    result = repository.create_order(customername,orderdate,itemsordered)
    print_order_info(result)

while True:
    match choice:
        case 'help'|'h':
            print('''
                  List of commands and corresponding function: \n
                    "help": Shows this list of commands.\n
                    "1" - Lists all available items.\n
                    "2" - Create a new item.\n
                    "3" - List all orders\n
                    "4" - Get order info. (Shows items included with the order)\n
                    "5" - Create new order\n
                    "quit or exit" - Exits the programme.\n
                  ''')
        case 'exit'|'quit'|'escape'|'q'|'esc':
            break

        case '1':
            print_item_list()
        case '2':
            result = get_item_info()
            print('\n',result,'\n\n')
            itemlength, orderlength = update_list_lengths()
        case '3':
            print_orders()
        case '4':
            ordernumber = None
            print('\n\n')
            print_orders()
            while ordernumber ==None:
                try:
                    ordernumber = input('Which order number would you like more info about? ')
                    result = repository.get_order_info(ordernumber)
                except:
                    print('Please enter a valid order number from the list.')
                    ordernumber = None
            
            print_order_info(result)
        case '5':
            get_new_order_info()
            itemlength, orderlength = update_list_lengths()
        case _:
            print('\nUnknown command. Please type "help" for a list of commands.\n')
    choice = input('What would you like to do? ')
