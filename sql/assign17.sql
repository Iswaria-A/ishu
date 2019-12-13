SELECT COUNT(agent_id),city FROM agents GROUP BY City;

SELECT COUNT(agent_id), City FROM Customers GROUP BY City ORDER BY COUNT(agent_id) DESC;

SELECT COUNT(Customer_id), City FROM Customers GROUP BY City HAVING COUNT(Customer_id) > 3;