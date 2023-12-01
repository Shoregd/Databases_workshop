from lib.Item import Item
from lib.Order import Order

class ShopManagementRepository:
    def __init__(self,connection):
        self._connection = connection
    def list_items(self):
        rows = self._connection.execute('SELECT * FROM items')
        items_list = []
        for row in rows:
            data = str(Item(row['id'],row['name'],row['unit_price'],row['quantity']))
            items_list.append(data)
        return items_list
    def list_orders(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders_list = []
        for row in rows:
            data = str(Order(row['id'],row['customer_name'],row['order_date']))
            orders_list.append(data)
        return orders_list
    
    def get_order_info(self,order_number):
        rows = self._connection.execute(
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
        )
        return_data = []
        items_list = []
        row = rows[0]
        data = str(Order(row['orders_id'],row['customer_name'],row['order_date']))
        return_data.append(data)
        for row in rows:
            data = f'Item {row["items_id"]}: {row["item_name"]}'
            items_list.append(data)
        return_data.append(items_list)
        return return_data
    def create_item(self,itemname,unitprice,item_quantity):
        self._connection.execute(
            'INSERT INTO items(name,unit_price,quantity) VALUES(%s,%s,%s)',[itemname,unitprice,item_quantity]
        )
        rows = self._connection.execute('SELECT * FROM items')
        row = rows[-1]
        return f'New Item added: {str(Item(row["id"],row["name"],row["unit_price"],row["quantity"]))}'
    def create_order(self,customername,orderdate,items):
        self._connection.execute(
            '''
            INSERT INTO orders (customer_name,order_date) VALUES(%s,%s)
            ''', [customername,orderdate]
        )
        rows = self._connection.execute('SELECT * FROM orders')
        orderid = rows[-1]['id']
        items = items.split(',')
        for item in items:
            self._connection.execute('INSERT INTO items_orders (order_id,item_id) VALUES(%s,%s)',[orderid,item])
        
        return_data = ['New Order added: ']
        order_info = self.get_order_info(orderid)
        return_data[0] += order_info[0]
        return_data.append(order_info[1])
        return return_data