-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 17, 2021 at 04:38 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banking_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Name` varchar(25) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `Age` int(11) NOT NULL,
  `Phone_no` varchar(10) NOT NULL,
  `Account_No` int(11) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Balance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`Name`, `Gender`, `Age`, `Phone_no`, `Account_No`, `Email`, `Balance`) VALUES
('Naresh', 'Male', 20, '987654321', 1001, 'naresh123@gmail.com', 48100),
('Prasath', 'Male', 20, '987654322', 1002, 'prasath123@gmail.com', 41600),
('Muthu', 'Male', 21, '987654323', 1003, 'muthu123@gmail.com', 58000),
('Kumar', 'Male', 23, '987654324', 1004, 'kumar123@gmail.com', 38200),
('Kumaran', 'Male', 34, '987654325', 1005, 'kumar123@gmail.com', 23800),
('Naveen', 'Male', 30, '987654326', 1006, 'naveen123@gmail.com', 92798),
('Praveen', 'Male', 25, '987654327', 1007, 'praveen123@gmail.com', 58268),
('Krishnan', 'Male', 20, '987654318', 1008, 'krishnan123@gmail.com', 59300),
('Kaviya', 'Female', 24, '987654319', 1009, 'kaviya123@gmail.com', 80000),
('Swathi', 'Female', 20, '987654330', 1010, 'swathi123@gmail.com', 70000),
('Kavin', 'Male', 30, '987654331', 1011, 'kavin123@gmail.com', 100200),
('Prakash', 'Male', 35, '987654332', 1012, 'prakash123@gmail.com', 50000),
('Surash', 'Male', 30, '9898848848', 1039, 'surash123@gmail.com', 50000),
('Santhi', 'Female', 40, '9884878755', 1041, 'santhi123@gmil.com', 40000),
('Swatha', 'Female', 25, '9388383833', 1044, 'swatha123@gmail.com', 30000),
('Jeeva', 'Male', 23, '8987878748', 1046, 'jeeva123@gmail.com', 60000);

-- --------------------------------------------------------

--
-- Table structure for table `history`
--

CREATE TABLE `history` (
  `Sender_Name` varchar(25) NOT NULL,
  `Sender_NO` int(11) NOT NULL,
  `Receiver_Name` varchar(25) NOT NULL,
  `Receiver_no` int(11) NOT NULL,
  `Date` date DEFAULT current_timestamp(),
  `Amount` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `history`
--

INSERT INTO `history` (`Sender_Name`, `Sender_NO`, `Receiver_Name`, `Receiver_no`, `Date`, `Amount`) VALUES
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 400),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Naresh', 1001, 'Prasath', 1002, '2021-09-15', 200),
('Kumar', 1004, 'Naresh', 1001, '2021-09-15', 200),
('Kumar', 1004, 'Naresh', 1001, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Naveen', 1006, 'Kumaran', 1005, '2021-09-15', 200),
('Prasath', 1002, 'Naresh', 1001, '2021-09-15', 200),
('Krishnan', 1008, 'Naresh', 1001, '2021-09-16', 200),
('Krishnan', 1008, 'Naresh', 1001, '2021-09-16', 200),
('Muthu', 1003, 'Kumaran', 1005, '2021-09-16', 200),
('Praveen', 1007, 'Kavin', 1011, '2021-09-16', 200),
('Krishnan', 1008, 'Naveen', 1006, '2021-09-16', 500),
('Kumaran', 1005, 'Krishnan', 1008, '2021-09-16', 200),
('Naresh', 1001, 'Praveen', 1007, '2021-09-16', 500),
('Naresh', 1001, 'Praveen', 1007, '2021-09-16', 500),
('Kumar', 1004, 'Praveen', 1007, '2021-09-16', 200);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`Account_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `Account_No` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1047;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
