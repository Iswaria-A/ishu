-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2019 at 09:23 AM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `office`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Id` int(10) DEFAULT NULL,
  `FirstName` varchar(100) DEFAULT NULL,
  `LastName` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `Balance_amount` float(7,2) DEFAULT NULL,
  `Status_id` tinyint(1) DEFAULT NULL,
  `Notes` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Id`, `FirstName`, `LastName`, `Password`, `Balance_amount`, `Status_id`, `Notes`) VALUES
(8, 'Jack', 'Rich', 'abcd', 7.25, 1, 'coding '),
(9, 'Tim', 'Roy', 'defg', 7.15, 0, 'learning'),
(9, 'Tim', 'Roy', 'defg', 7.15, 0, 'learning'),
(NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Jack', 'Henry', 'abc', 7.26, 1, 'hello'),
(NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Jack', 'Henry', 'abc', 7.26, 1, 'hello'),
(7, 'tim', 'henry', 'abc', 7.23, 0, 'hello'),
(7, 'tim', 'henry', 'abc', 7.23, 0, 'hello'),
(8, 'tim', 'jack', 'def', 7.16, 1, 'hai'),
(1, 'Jim', 'Roy', 'abc', 7.20, 1, 'Coding'),
(2, 'Jack', 'Th', 'def', 7.21, 0, 'Hello'),
(3, 'Tim', 'Hey', 'ghi', 7.22, 1, 'Haii'),
(4, 'Jacob', 'null', 'jkl', 7.23, 0, 'Learning'),
(5, 'Ted', 'Nm', 'mno', 7.24, 1, 'Css'),
(6, 'Tom', 'b', 'pqr', 7.25, 0, 'Java'),
(7, 'Timmy', 'Jon', 'stu', 7.26, 1, 'Languages'),
(8, 'Geogrge', 'Luck', 'vwx', 7.27, 0, 'html'),
(9, 'Luke', 'he', 'xy', 7.28, 1, 'bootstrap');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
