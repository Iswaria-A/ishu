SELECT * FROM `books` WHERE author_name='Mark Twain';

SELECT * FROM `books` WHERE author_name='Mark Twain' AND author_country='Brazil';

SELECT * FROM `books` WHERE author_country='America' OR author_country='India';

SELECT * FROM `books` WHERE NOT author_country='China';


SELECT LAST_INSERT_ID();

SELECT * FROM `books` ORDER BY year;

SELECT * FROM books LIMIT 7;
