SELECT books.book_name,books.author_name,books.price,user_books.user_name FROM books INNER JOIN user_books ON books.id=user_books.id;


INSERT INTO `user_books`(`id`, `user_name`, `book_id`, `user_country`) 
VALUES ('1','abc','5','Japan'), 
('2','hai','10','Uk'), 
('3','hello','15','England'), 
('4','world','20','Russia'), 
('5','star','25','Kenya'), 
('6','coding','30','Koria'), 
('7','view','35','Netherlands'), 
('8','bagg','40','Newzealand'), 
('9','class','45','Sweden');


UPDATE user_books SET user_name = 'David John'WHERE id='3';

SELECT books.book_name,books.author_name,books.price FROM books INNER JOIN user_books ON books.id=user_books.id WHERE user_name='David John';
