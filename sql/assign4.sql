ALTER TABLE `books` ADD city varchar(100) AFTER author_country;

ALTER TABLE `books` DROP COLUMN city;

ALTER TABLE `books` MODIFY book_name varchar(100) NOT NULL;


ALTER TABLE `books` MODIFY price float(5,2);