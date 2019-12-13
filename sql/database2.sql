CREATE DATABASE samplevideo_db;


SELECT * FROM `user_details`
SELECT COUNT(*) FROM `user_details`
SELECT DISTINCT first_name FROM `user_details`
SELECT * FROM `user_details` WHERE user_id=1
SELECT * FROM `user_details` WHERE user_id IN(1,2,3,4)
SELECT * FROM `user_details` WHERE first_name LIKE '%d%'
SELECT user_id AS id,username AS name FROM `user_details`