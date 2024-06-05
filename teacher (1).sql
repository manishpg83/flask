-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 01:33 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `teacher`
--

CREATE TABLE `teacher` (
  `id` int(11) NOT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `mobile_number` varchar(20) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `is_teacher` tinyint(1) DEFAULT NULL,
  `can_work_with_ous` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `city_type` varchar(50) DEFAULT NULL,
  `is_married` tinyint(1) DEFAULT NULL,
  `has_kids` tinyint(1) DEFAULT NULL,
  `kids_age_range` varchar(20) DEFAULT NULL,
  `teacher_type` varchar(50) DEFAULT NULL,
  `can_teach_personal_student` tinyint(1) DEFAULT NULL,
  `can_teach_iit` tinyint(1) DEFAULT NULL,
  `_iit_options` text DEFAULT NULL,
  `can_teach_neet` tinyint(1) DEFAULT NULL,
  `_neet_options` text DEFAULT NULL,
  `can_teach_upsc` tinyint(1) DEFAULT NULL,
  `_upsc_options` text DEFAULT NULL,
  `can_teach_banking` tinyint(1) DEFAULT NULL,
  `_banking_options` text DEFAULT NULL,
  `can_teach_personally` tinyint(1) DEFAULT NULL,
  `_personally_options` text DEFAULT NULL,
  `can_teach_cat` tinyint(1) DEFAULT NULL,
  `_cat_options` text DEFAULT NULL,
  `can_teach_gmat` tinyint(1) DEFAULT NULL,
  `_gmat_options` text DEFAULT NULL,
  `laptop` tinyint(1) DEFAULT NULL,
  `connected_with_ous` tinyint(1) DEFAULT NULL,
  `batch_capacity` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teacher`
--

INSERT INTO `teacher` (`id`, `teacher_id`, `mobile_number`, `first_name`, `last_name`, `date`, `age`, `is_teacher`, `can_work_with_ous`, `gender`, `city`, `city_type`, `is_married`, `has_kids`, `kids_age_range`, `teacher_type`, `can_teach_personal_student`, `can_teach_iit`, `_iit_options`, `can_teach_neet`, `_neet_options`, `can_teach_upsc`, `_upsc_options`, `can_teach_banking`, `_banking_options`, `can_teach_personally`, `_personally_options`, `can_teach_cat`, `_cat_options`, `can_teach_gmat`, `_gmat_options`, `laptop`, `connected_with_ous`, `batch_capacity`, `updated_by`) VALUES
(1, 1, '545345455', 'fsdfsdfs', 'sds', '2024-06-04', 22, 1, 'yes', 'M', '2', 'Tier1', 0, 1, '0-5 years', 'School', 1, 0, '[\"Option 1\", \"Option 2\", \"Option 3\"]', 1, '[\"Option 1\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 3\"]', 1, '[\"Option 1\", \"Option 2\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 4\"]', 1, NULL, 1, '[\"Option 1\", \"Option 2\"]', 1, 1, 112, 1),
(2, 2, '545345455', 'fsdfsdfsss', 'sdsss', '0000-00-00', 17, 1, NULL, 'F', NULL, NULL, 0, 0, '0-5 years', 'Kindergarten', 1, 1, '[\"Option 1\"]', 0, '[\"Option 1\"]', 1, '[\"Option 1\"]', 1, '[\"Option 1\"]', 1, '[\"Option 1\", \"Option 5\"]', 1, '[\"Option 1\"]', 1, '[\"Option 1\"]', 1, 1, 22, 0),
(3, 3, '545345455', 'fsdfsdfs', 'sds', '2024-06-04', 22, 1, 'yes', 'M', '2', 'Tier2', 1, 1, '0-5 years', 'School', 1, 1, '[\"Option 1\", \"Option 2\", \"Option 3\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 5\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 3\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 3\", \"Option 4\", \"Option 5\"]', 1, '[\"Option 1\", \"Option 2\", \"Option 4\"]', 1, NULL, 1, '[\"Option 1\", \"Option 2\"]', 0, 1, 11, 0),
(4, 4, '43434343', 'sdfsdff', 'fdsfdsf', '2024-06-02', 22, 0, 'yes', 'M', NULL, 'Tier2', 0, 0, NULL, 'School', 0, 1, '[\"Option 1\"]', 1, '[\"Option 1\"]', 0, NULL, 0, NULL, 0, NULL, 0, NULL, 0, NULL, 1, 1, 22, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
