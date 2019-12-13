SELECT year AS published_year, id AS bookId FROM `books`;

SELECT author_name, CONCAT(book_title,',',author_name,',',year)AS Description FROM `books`;

