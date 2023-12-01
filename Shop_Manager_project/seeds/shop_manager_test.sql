DROP TABLE IF EXISTS items_orders;
DROP SEQUENCE IF EXISTS order_id_seq;
DROP SEQUENCE IF EXISTS item_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;
DROP TABLE IF EXISTS items;
DROP SEQUENCE IF EXISTS items_id_seq;

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name text,
    unit_price float,
    quantity int
);
CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date date
    );

CREATE TABLE items_orders(
    order_id int,
    item_id int,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade

);

INSERT INTO items(name,unit_price,quantity) VALUES
('Taco',1.25,75),
('Burrito',2.25,60),
('Enchilada',3.75,82),
('Tortilla',0.75,157),
('Cheese',1.90,286),
('Guacamole',1.60,184),
('Sour Cream',1.00,42);

INSERT INTO orders(customer_name,order_date) VALUES
('Greg Smith','2023-11-02'),
('John Doe','2023-11-17'),
('Terry Bloggs','2023-11-12');

INSERT INTO items_orders(order_id,item_id) VALUES
(1,1),
(1,5),
(1,6),
(1,7),
(2,2),
(2,4),
(2,5),
(2,6),
(3,3),
(3,4),
(3,5),
(3,7);