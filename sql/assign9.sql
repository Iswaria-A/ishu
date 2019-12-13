SELECT MAX(price) AS LargestPrice FROM books WHERE author_country='England';

SELECT MIN(price) AS SmallestPrice FROM `books` WHERE author_name='Mark Twain';

SELECT COUNT(id) FROM `books` WHERE author_name='William Faulkner';

SELECT book_title FROM `books` ORDER BY year DESC LIMIT 7;

SELECT book_title FROM `books` ORDER BY year;

SELECT AVG(price) FROM `books`;

SELECT AVG(price) FROM `books` WHERE author_name='Mark Twain';