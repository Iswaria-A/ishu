CREATE DATABASE library;
CREATE TABLE `books`(id int(50) UNIQUE AUTO_INCREMENT PRIMARY KEY, book_name varchar(100), book_title varchar(100), author_name varchar(100), author_country varchar(100), year varchar(100) NULL,price float(50));

CREATE TABLE duplicate_books SELECT * FROM books;
SELECT * FROM `duplicate_books`;
INSERT INTO `books`(`id`,`book_name`,`book_title`,`author_name`,`author_country`,`year`,`price`) 
VALUES('1','Harry Potter','Fiction','JK Rowling','America','1990','600.25'), 
('2','Famous Five','Fiction','Jim','Brazil','1988','800.35'), 
('3','Famous Seven','Novel','Mark Twain','China','1994','950.15'), 
('4','Law of Averages','Adventures','Teddy','India','1993','1000.25'), 
('5','Queen land','Fiction','John','Uk','1999','700.75'), 
('6','Abc','Drama','Jack','London','1998','680.55'), 
('7','Hangwomen','Novel','Meera','India','2017','550.25'), 
('8','Def','Love story','Jay','Japan','2011','6000.25'), 
('9','Jaa','Fiction','Ted','Europe','2013','5000.25'), 
('10','Reason is you','Novel','Roy','canada','1995','720.25'), 
('11','This is not your story','Adventure','Ram','Dubai','1991','400.30');


CREATE TABLE `user_books`(id int(50), user_name varchar(100),book_id int (50),user_country varchar(100));