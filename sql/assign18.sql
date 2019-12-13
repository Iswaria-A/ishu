CREATE TABLE `products`(product_id int(50), name varchar(100),price int(50),agent_id int(50));

INSERT INTO `products`(`product_id`, `name`, `price`, `agent_id`) 
VALUES ('5','Tv','5000','2'), 
('10','Chair','7000','4'), 
('15','Fan','2000','5'), 
('20','Laptop','9000','7'), 
('25','Charger','150','8'), 
('30','Bag','100','9'), 
('35','Dress','700','10'), 
('40','Sandal','200','11'), 
('45','Chocolate','90','16'), 
('50','Mobile phone','8000','17'), 
('55','Watch','1000','13');


SELECT name FROM agents WHERE EXISTS (SELECT name FROM Products WHERE Products.agent_id = agents.agent_id AND Price >150);


SELECT name FROM Products WHERE Product_id = ANY (SELECT Product_id FROM orders WHERE no_of_items > 10);

SELECT name FROM Products WHERE Product_id = ALL (SELECT Product_id FROM orders WHERE no_of_items > 10);

UPDATE orders SET order_date ='2018-3-10' WHERE order_id='9';

SELECT * FROM `orders` WHERE order_date='2018-3-10';