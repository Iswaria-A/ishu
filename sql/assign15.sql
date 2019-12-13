CREATE TABLE `agents`(agent_id int(50),name varchar(100), city varchar(100), commission varchar(100));

INSERT INTO `agents`(`agent_id`, `name`, `city`, `commission`) 
VALUES ('1','Ram','Berlin','50'), 
('2','Rim','Mexico','70'), 
('3','Tom','France','20'), 
('4','Raj','Manchester','55'), 
('5','Ran','Shimla','60'), 
('6','Roy','Srinagar','90'), 
('7','Ted','Sweden','100'), 
('8','Timm','Ranchi','59'), 
('9','Rana','Jammu','38'), 
('10','Tena','Delhi','75');

CREATE TABLE `customers`(customer_id int(50),name varchar(100),city varchar(100),agent_id int(50));

INSERT INTO `customers`(`customer_id`, `name`, `city`, `agent_id`) 
VALUES ('2','Abc','Berlin','1'), 
('4','Def','Mexico','2'), 
('6','Rakee','France','3'), 
('8','Jisha','Singapore','4'), 
('10','Tiljo','Dubai','5'), 
('12','Thomas','Finland','10'), 
('14','Maddy','Ladak','15'), 
('16','Madhav','Lake','17'), 
('18','Jacky','Bhutan','20');

CREATE TABLE `orders`(order_id int(50),customer_id int(50),agent_id int(50),purchase_amount int(50),order_date varchar(100),no_of_items int(50));

INSERT INTO `orders`(`order_id`, `customer_id`, `agent_id`, `purchase_amount`, `order_date`, `no_of_items`) 
VALUES ('3','2','1','100','1/2/2001','22'), 
('6','4','2','150','6/1/2003','27'), 
('9','6','3','120','1/3/2004','26'), 
('12','8','4','190','7/2/2005','40'), 
('15','10','5','200','10/2/2007','23'), 
('18','12','11','230','12/2/2011','35'), 
('21','16','15','290','3/2/2012','45'), 
('24','20','17','300','16/8/2016','37'), 
('27','22','19','360','18/9/2014','60'), 
('30','28','14','400','5/7/2004','80');

SELECT customers.name,orders.order_id FROM customers LEFT JOIN orders ON customers.customer_id=orders.customer_id ORDER BY customers.name;

SELECT orders.order_id,customers.name FROM orders RIGHT JOIN customers ON customers.agent_id=orders.agent_id ORDER BY customers.customer_id;

SELECT customers.name,orders.order_id FROM customers FULL OUTER JOIN orders ON customers.customer_id=orders.customer_id ORDER BY customers.name;
