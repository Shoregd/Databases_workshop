class Order:
    def __init__(self,id,customer_name,order_date):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
    def __repr__(self):
        return f'Order Number {self.id} for: {self.customer_name} Order Date: {self.order_date}'
    def __eq__(self,other):
        return self.__dict__ == other.__dict__