UPDATE customers SET city='Manchester' WHERE customer_id='8';

SELECT customers.name FROM customers WHERE city='Manchester' UNION SELECT agents.name FROM agents WHERE city='Manchester';

SELECT name FROM agents UNION SELECT city FROM customers;

SELECT name FROM agents UNION SELECT name FROM customers;

SELECT name FROM agents WHERE city='Manchester' UNION SELECT name FROM customers WHERE city='Manchester';

