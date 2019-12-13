CREATE DATABASE My_students;
CREATE TABLE `student`(StudentId int(50),First_name varchar(100),Last_name varchar(100),Subjects varchar(100),Marks int(50));
INSERT INTO `student`(`StudentId`, `First_name`, `Last_name`) 
VALUES ('1','Tim','H'), ('2','Tom','L'), 
('3','Timmy','K'), 
('4','Jack','N'), 
('5','Ted','P'), 
('6','Thomas','B'),
 ('7','Jim','C');
CREATE TABLE `s1`(StudentId int(50),Subjects varchar(100),Marks int(50),Attendance varchar(100));
INSERT INTO `s1`(`StudentId`, `Subjects`, `Marks`, `Attendance`) 
VALUES ('2','Science','25','P'), 
('1','Social','35','A'),
 ('4','English','50','P'), 
 ('3','Maths','70','A'), 
 ('5','English','84','P'), 
 ('7','English','90','A'), 
 ('6','English','87','A'), 
 ('8','Sanskit','95','P'),
  ('10','English','89','P'),
   ('9','Science','79','A'),
    ('11','English','99','A'),
     ('13','Social','80','P'), 
     ('12','English','96','P'), 
     ('14','Malayalam','69','A'), 
     ('16','Science','91','P'), 
     ('15','English','93','P');
INSERT INTO `student`(`StudentId`, `First_name`, `Last_name`) 
VALUES ('','Teddy','G'), 
('','Roy','R'), 
('','Rim','M'), 
('','Yan','H'), 
('','Jerry','D'), 
('','Ben','I'), 
('','Ced','P'), 
('','Rok','E');
SELECT student.First_name, student.Last_name , s1.Marks FROM s1 INNER JOIN student ON student.StudentId=s1.StudentId;
SELECT student.First_name, student.Last_name , s1.Marks,s1.Subjects FROM s1 INNER JOIN student ON student.StudentId=s1.StudentId WHERE marks>=80 AND Subjects='English';
SELECT student.First_name, student.Last_name , s1.Subjects FROM s1 INNER JOIN student ON student.StudentId=s1.StudentId WHERE Attendance='A' AND Subjects='English';
