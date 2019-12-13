CREATE DATABASE office;

CREATE TABLE customers( Id int(10), FirstName varchar(100), LastName varchar(100), Password varchar(100), Balance_amount float(7,2), Status_id TINYINT(1), Notes varchar(100) );

INSERT INTO `customers`(`Id`,`FirstName`,`LastName`,`Password`,`Balance_amount`,`Status_id`,`Notes`)
VALUES('1','Jim','Roy','abc','7.20','1','coding'),
VALUES('2','Jim','Roy','abc','7.21','1','coding'),
VALUES('3','Jim','Roy','abc','7.22','1','coding'),
VALUES('4','Jim','Roy','abc','7.23','1','coding'),
VALUES('5','Jim','Roy','abc','7.24','1','coding'),
VALUES('6','Jim','Roy','abc','7.25','1','coding'),
VALUES('7','Jim','Roy','abc','7.26','1','coding'),
VALUES('8','Jim','Roy','abc','7.27','1','coding'),
VALUES('9','Jim','Roy','abc','7.28','1','coding');

SELECT * FROM `customers`
SELECT COUNT(*) FROM `customers`
SELECT * FROM `customers` WHERE Id=1
SELECT * FROM `customers` WHERE Id IN(1,2,3)
SELECT * FROM `customers` WHERE Id NOT IN(1,2,3)
SELECT * FROM `customers` WHERE Id>4
SELECT * FROM `customers` WHERE LastName IS null
SELECT COUNT(*) FROM `customers` WHERE LastName IS NULL
SELECT DISTINCT(FirstName) FROM `customers`
SELECT * FROM `customers` WHERE FirstName LIKE "%a%"