PROBLEM OUTLINE

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding items.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.

--- NOUNS ---

items, name, unit_price, quantity, orders, customer_name, order_date

--- TABLE LAYOUT ---

RECORD | PROPERTIES

Items | id,name,unit_price,quantity

Orders | id,customer_name,order_date

--- DATA TYPES ---

Items:
    * id: SERIAL
    * name: text
    * unit_price: float
    * quantity: int

Orders:
    * id: SERIAL
    * customer_name: text
    * order_date: date

--- RELATIONSHIPS ---

Items can have MANY orders. Orders can have MANY Items. Join table needed.

--- JOIN TABLE LAYOUT ---

Join table tables: items,orders
Join table name: items_orders
Columns: item_id,order_id

SQL file can be found in seeds/shop_manager_project.sql
Test data sql found in seeds/shop_manager_test.sql

--- CLASS BREAKDOWN ---

Item - Model Class
    * __init__: id,name,unit_price,quantity
    * __repr__: 'Item {id}: {name} Unit Price: £{unit_price} In Stock: {quantity}'
    * __eq__: Allows testing.

Order - Model Class
    * __init__: id,customer_name,order_date
    * __repr__: 'Order Number {id} for: {customer_name} Order Date: {order_date}'

ShopManagementRepository - Repository Class for manipulation of Item class
    * __init__: connection to database using db_connection

    * list_items(): Will return a list of Item objects by their __repr__. No 
       inputs. Returns a list of strings. No other side effects.
        executes
        '''
        SELECT * from items
        '''

    * create_item(): Will create a new item and add it to the database. Inputs: 
       item_name: string, unitprice: float, item_quantity: int. Returns 
       confimation string 'New Item added: {new item __repl__}' Side effects: Adds data to items table in database.
       executes 
        '''INSERT INTO items(name,unit_price,quantity) VALUES(%s,%s,%s)''',[item_name,unitprice,item_quantity]
        I.E create_item('Olives',0.45,300) --v 
            'New Item added: Item 8: Olives Unit Price: £0.45 In Stock: 300' 

    * list_orders(): Will return a list of Order objects __repr__. No inputs taken.
        Returns list of strings. No side effects.
        executes
        ''' SELECT * from orders'''
        I.E list_orders() --> ['Order Number 1 for: Greg Smith Order Date: 2023-11-02'...]

    * get_order_info(): Will return the associated information about the specified
        order. Inputs order_number: int. Returns list of string information about the specified order and a list of associated items as strings. No side effects.

        I.E get_order_info(1) --v
        ['Order Number 1 for: Greg Smith Order Date: 2023-11-02',['Item Number 1: Taco','Item Number 5: Cheese','Item Number 6: Guacamole','Item Number 7: Sour Cream']] this can then be printed to the end user.
        executes
        '''
        SELECT
            orders.id as orders_id,
            orders.customer_name,
            orders.order_date,
            items.id as items_id,
            items.name as item_name
        FROM orders
        JOIN items_orders ON items_orders.order_id = orders.id
        JOIN items ON items.id = items_orders.item_id
        WHERE orders.id = %s
        ''',[order_number]
    * create_order(): Will create a new order in the database and update the 
       associations within the items_orders table. Inputs: customername:string,orderdate: string, items_ordered: string of numbers seperated by commas. Returns 'New order added:' then calls get_order_info for the new order id appending each item to the list it will return to be printed.
       I.E create_order('Karen Street','2023-11-30','2,4,5') --v
       ['New order added:','Order Number 4 for: Karen Street Order Date: 2023-11-30',[{ITEMS}]]
       executing 
       '''
       INSERT INTO orders(customer_name,order_date) VALUES(%s,%s)
       ''',[customername,orderdate]
       '''
       SELECT * from orders (get new ID)
       '''
       new_id = len(returned_list)
       '''
       INSERT INTO items_orders(order_id,item_id) VALUES(%s,%s) (will loop through list of item ids supplied from items_ordered)
       ''',[new_id,current_item_id]

