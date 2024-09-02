-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2024 at 11:20 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rit_e_approval`
--

-- --------------------------------------------------------

--
-- Table structure for table `application_allotment`
--

CREATE TABLE `application_allotment` (
  `id` bigint(20) NOT NULL,
  `Department` varchar(100) DEFAULT NULL,
  `acyear` varchar(100) DEFAULT NULL,
  `capitalGoods` int(11) DEFAULT NULL,
  `academic` int(11) DEFAULT NULL,
  `rnd` int(11) DEFAULT NULL,
  `recurringItems` int(11) DEFAULT NULL,
  `coCurricular` int(11) DEFAULT NULL,
  `facultyCompetency` int(11) DEFAULT NULL,
  `trainingPlacement` int(11) DEFAULT NULL,
  `extraCurricular` int(11) DEFAULT NULL,
  `governanceAdmin` int(11) DEFAULT NULL,
  `generalAmenities` int(11) DEFAULT NULL,
  `others` int(11) DEFAULT NULL,
  `transport` int(11) DEFAULT NULL,
  `expenditure` int(11) DEFAULT NULL,
  `total_amount` int(11) DEFAULT NULL,
  `balance_amount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `application_allotment`
--

INSERT INTO `application_allotment` (`id`, `Department`, `acyear`, `capitalGoods`, `academic`, `rnd`, `recurringItems`, `coCurricular`, `facultyCompetency`, `trainingPlacement`, `extraCurricular`, `governanceAdmin`, `generalAmenities`, `others`, `transport`, `expenditure`, `total_amount`, `balance_amount`) VALUES
(1, 'AD', '2024', 10000, 5134, 9766, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 130000, 129766),
(2, 'TRANSPORT', '2024', 10000, 10000, 9768, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 130000, 129768);

-- --------------------------------------------------------

--
-- Table structure for table `application_auth_list`
--

CREATE TABLE `application_auth_list` (
  `Document_no` varchar(200) NOT NULL,
  `hod` varchar(100) DEFAULT NULL,
  `hod_date` varchar(100) DEFAULT NULL,
  `hod_remarks` varchar(100) DEFAULT NULL,
  `hod_reason` varchar(100) DEFAULT NULL,
  `hod_clarification` varchar(100) DEFAULT NULL,
  `gm` varchar(100) DEFAULT NULL,
  `gm_date` varchar(100) DEFAULT NULL,
  `gm_remarks` varchar(100) DEFAULT NULL,
  `gm_reason` varchar(100) DEFAULT NULL,
  `gm_clarification` varchar(100) DEFAULT NULL,
  `Vice_Principal` varchar(100) DEFAULT NULL,
  `Vice_Principal_date` varchar(100) DEFAULT NULL,
  `Vice_Principal_remarks` varchar(100) DEFAULT NULL,
  `Vice_Principal_reason` varchar(100) DEFAULT NULL,
  `Vice_Principal_clarification` varchar(100) DEFAULT NULL,
  `Principal` varchar(100) DEFAULT NULL,
  `Principal_date` varchar(100) DEFAULT NULL,
  `Principal_remarks` varchar(100) DEFAULT NULL,
  `Principal_reason` varchar(100) DEFAULT NULL,
  `Principal_clarification` varchar(100) DEFAULT NULL,
  `staff` varchar(100) DEFAULT NULL,
  `staff_clarification` varchar(100) DEFAULT NULL,
  `staff_date` varchar(100) DEFAULT NULL,
  `staff_reason` varchar(100) DEFAULT NULL,
  `staff_remarks` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `application_auth_remarks`
--

CREATE TABLE `application_auth_remarks` (
  `Document_no` varchar(200) NOT NULL,
  `auth_approval` varchar(100) DEFAULT NULL,
  `auth_remarks` varchar(100) DEFAULT NULL,
  `auth_reason` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `application_clarification`
--

CREATE TABLE `application_clarification` (
  `Document_no` varchar(200) NOT NULL,
  `clarification_approval` varchar(500) DEFAULT NULL,
  `clarification_date_and_time` date NOT NULL,
  `clarification_remarks` varchar(500) DEFAULT NULL,
  `clarification_reroute_comments` varchar(500) DEFAULT NULL,
  `clarification_reroute_clarification` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `application_doc_remarks`
--

CREATE TABLE `application_doc_remarks` (
  `Document_no` varchar(200) NOT NULL,
  `doc_date_and_time` date NOT NULL,
  `doc_approval_id` varchar(20) DEFAULT NULL,
  `doc_applied_staff_id` varchar(20) DEFAULT NULL,
  `doc_subject` varchar(100) DEFAULT NULL,
  `doc_remarks` varchar(100) DEFAULT NULL,
  `doc_attachment` varchar(100) DEFAULT NULL,
  `doc_clarification_status` varchar(100) DEFAULT NULL,
  `doc_clarifictaions_reason` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `application_doc_remarks`
--

INSERT INTO `application_doc_remarks` (`Document_no`, `doc_date_and_time`, `doc_approval_id`, `doc_applied_staff_id`, `doc_subject`, `doc_remarks`, `doc_attachment`, `doc_clarification_status`, `doc_clarifictaions_reason`) VALUES
('RIT/AC/2024/AD/Research and Development/00003@2008241443', '2024-08-20', '3333', '1111', NULL, 'gdsfdsfgdsfg', NULL, 'Pending', NULL),
('RIT/AC/2024/AD/Research and Development/00003@2008241444', '2024-08-20', '3333', '1111', NULL, 'gdfgdsgfdsg', NULL, 'Pending', NULL),
('RIT/AC/2024/AD/Research and Development/00003@2008241445', '0000-00-00', '3333', '1111', NULL, 'gsdgdsfgdsfg', NULL, 'Pending', NULL),
('RIT/AC/2024/AD/Research and Development/00003@2008241448', '0000-00-00', '3333', '1111', NULL, 'gdsfgdsgsg', NULL, 'Pending', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `application_e_approval`
--

CREATE TABLE `application_e_approval` (
  `Document_no` varchar(500) NOT NULL,
  `Department` varchar(100) NOT NULL,
  `Org_Unit` varchar(100) NOT NULL,
  `Category` varchar(100) NOT NULL,
  `Head_of_account` varchar(200) DEFAULT NULL,
  `remarks_Subject` varchar(100) NOT NULL,
  `Priority` varchar(500) NOT NULL,
  `Tran_No` varchar(500) DEFAULT NULL,
  `fin_commit` varchar(100) NOT NULL,
  `Tolerance` int(11) DEFAULT NULL,
  `Total_Value` int(11) DEFAULT NULL,
  `Attachment` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `Attachment_details` varchar(100) DEFAULT NULL,
  `Technician` varchar(100) DEFAULT NULL,
  `HOD` varchar(100) DEFAULT NULL,
  `GM` varchar(100) DEFAULT NULL,
  `OfficeStaff` varchar(100) DEFAULT NULL,
  `Deputywarden` varchar(100) DEFAULT NULL,
  `staff_id` varchar(10) DEFAULT NULL,
  `GM_date` varchar(100) DEFAULT NULL,
  `HOD_date` varchar(100) DEFAULT NULL,
  `Deputywarden_date` varchar(100) DEFAULT NULL,
  `OfficeStaff_date` varchar(100) DEFAULT NULL,
  `In_words` varchar(200) DEFAULT NULL,
  `Staff` varchar(100) DEFAULT NULL,
  `Staff_date` varchar(100) DEFAULT NULL,
  `remarks_Subject1` varchar(100) DEFAULT NULL,
  `creator` varchar(200) DEFAULT NULL,
  `GM_name` varchar(100) DEFAULT NULL,
  `HOD_name` varchar(100) DEFAULT NULL,
  `Staff_name` varchar(100) DEFAULT NULL,
  `Deputywarden_name` varchar(100) DEFAULT NULL,
  `OfficeStaff_name` varchar(100) DEFAULT NULL,
  `doc_status` varchar(100) DEFAULT NULL,
  `sub_category` varchar(100) DEFAULT NULL,
  `Principal` varchar(100) DEFAULT NULL,
  `Principal_date` varchar(100) DEFAULT NULL,
  `Principal_name` varchar(100) DEFAULT NULL,
  `Transport_Incharge` varchar(100) DEFAULT NULL,
  `Transport_Incharge_date` varchar(100) DEFAULT NULL,
  `Transport_Incharge_name` varchar(100) DEFAULT NULL,
  `Vice_Principal` varchar(100) DEFAULT NULL,
  `Vice_Principal_date` varchar(100) DEFAULT NULL,
  `Vice_Principal_name` varchar(100) DEFAULT NULL,
  `creator_mail` varchar(200) DEFAULT NULL,
  `creator_name` varchar(100) DEFAULT NULL,
  `reject` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `application_e_approval`
--

INSERT INTO `application_e_approval` (`Document_no`, `Department`, `Org_Unit`, `Category`, `Head_of_account`, `remarks_Subject`, `Priority`, `Tran_No`, `fin_commit`, `Tolerance`, `Total_Value`, `Attachment`, `date`, `Attachment_details`, `Technician`, `HOD`, `GM`, `OfficeStaff`, `Deputywarden`, `staff_id`, `GM_date`, `HOD_date`, `Deputywarden_date`, `OfficeStaff_date`, `In_words`, `Staff`, `Staff_date`, `remarks_Subject1`, `creator`, `GM_name`, `HOD_name`, `Staff_name`, `Deputywarden_name`, `OfficeStaff_name`, `doc_status`, `sub_category`, `Principal`, `Principal_date`, `Principal_name`, `Transport_Incharge`, `Transport_Incharge_date`, `Transport_Incharge_name`, `Vice_Principal`, `Vice_Principal_date`, `Vice_Principal_name`, `creator_mail`, `creator_name`, `reject`) VALUES
('RIT/AC/2024/AD/Academic/00001', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Academic', 'RIT/AD/Academic/Maintenance and service', 'gsdfg', 'High', 'RIT/AC/2024/AD/Academic/00001', 'No', NULL, NULL, 'None', '2024-08-20', 'fdsgdfgsdg', NULL, 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, '1111', 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, NULL, 'fdhgsghsdh', 'Rejected by STAFF', 'sdgsgsdg', 'Technician', NULL, NULL, 'STAFF', NULL, NULL, NULL, 'Maintenance and service', 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, NULL, NULL, 'Rejected by STAFF', 'Rejected by STAFF', NULL, '1236@gmail.com', 'Technician', 'True'),
('RIT/AC/2024/AD/Academic/00002', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Academic', 'RIT/AD/Academic/Maintenance and service', 'fdgh', 'Standard', 'RIT/AC/2024/AD/Academic/00002', 'Yes', 243, 2433, 'None', '2024-08-20', 'hfgdhgfhdfdhgfhg', NULL, 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, '1111', 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, NULL, 'hsdfhasfh', 'Rejected by STAFF', 'hdfhgfdhgfd', 'Technician', NULL, NULL, 'STAFF', NULL, NULL, NULL, 'Maintenance and service', 'Rejected by STAFF', 'Rejected by STAFF', NULL, NULL, NULL, NULL, 'Rejected by STAFF', 'Rejected by STAFF', NULL, '1236@gmail.com', 'Technician', 'True'),
('RIT/AC/2024/AD/Academic/00004', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Academic', 'RIT/AD/Academic/Maintenance and service', 'FGHFDH', 'Standard', NULL, 'Yes', 323, 2322, 'None', '2024-08-20', 'HGFHDFHGFDH', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'FDHFGHFGF', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Maintenance and service', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Academic/00005', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Academic', 'RIT/AD/Academic/Calibration', 'DW', 'High', NULL, 'Yes', 43, 3433, 'media\\Attachment_1_AC 01a Academic Schedule  R21 III & V SEMESTER.pdf', '2024-08-20', 'AXWSWE', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'WFW', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Calibration', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Academic/00008', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Academic', 'RIT/AD/Academic/Maintenance and service', 'fdsa', 'High', NULL, 'Yes', 232, 232, 'media\\Attachment_12_Transcript - dhaneshkumarp-0383 _ Microsoft Learn.pdf', '2024-08-20', 'sfdfsadf', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'ffdsafasf', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Maintenance and service', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Recurring items/00009', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Recurring items', 'RIT/AD/Recurring items/Services', 'sad', 'High', NULL, 'Yes', 435, 44, 'None', '2024-08-20', 'sdafasfsadf', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'sadfasfdf', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Services', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Recurring items/00013', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Recurring items', 'RIT/AD/Recurring items/Maintenance', 'dg', 'Standard', NULL, 'Yes', 4324, 2342, 'None', '2024-08-20', 'dgdf', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'dsgdsg', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Maintenance', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Research and Development/00003', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/Interaction with Industry', 'dafg', 'High', 'RIT/AC/2024/AD/Research and Development/00003', 'Yes', 234, 234, 'None', '2024-08-20', 'gdasgfgasd', NULL, 'OK', 'Pending', NULL, NULL, '1111', NULL, '20-08-2024 13:00:00', NULL, NULL, NULL, 'gfdsgdfsg', '20-08-2024 12:51:51', 'addsggs', 'Technician', NULL, 'AD_HOD', 'STAFF', NULL, NULL, NULL, 'Interaction with Industry', 'Pending', NULL, NULL, NULL, NULL, NULL, 'Pending', NULL, NULL, '1236@gmail.com', 'Technician', 'False'),
('RIT/AC/2024/AD/Research and Development/00006', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/Interaction with Industry', 'hfgdh', 'High', NULL, 'Yes', 243, 439, 'media\\Attachment_11_Transcript - dhaneshkumarp-0383 _ Microsoft Learn.pdf', '2024-08-20', 'fdghhfdh', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'fhgfdhg', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Interaction with Industry', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Research and Development/00007', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/Innovation', 'fdgds', 'High', NULL, 'Yes', 34, 4343, 'None', '2024-08-20', 'gdfgdsfg', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'gfdgdsfgdsg', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Innovation', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Research and Development/00010', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/Interaction with Industry', 'gdsg', 'Low', NULL, 'Yes', 342, 2344, 'None', '2024-08-20', 'dgfsdgfgsd', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'sdfgsdgdsg', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Interaction with Industry', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Research and Development/00011', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/MOU', 'gd', 'Standard', NULL, 'Yes', 243, 4333, 'None', '2024-08-20', 'sgsdgd', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'fsgdsggfd', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'MOU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/AD/Research and Development/00012', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'RIT', 'Research and Development', 'RIT/AD/Research and Development/Innovation', 'sdfasf', 'Standard', NULL, 'Yes', 234, 2432, 'None', '2024-08-20', 'sfdfasf', NULL, NULL, NULL, NULL, NULL, '1111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'fsadfsdaf', 'Technician', NULL, NULL, NULL, NULL, NULL, NULL, 'Innovation', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '1236@gmail.com', 'Technician', NULL),
('RIT/AC/2024/TRANSPORT/Research and Development/00001', 'TRANSPORT', 'RIT', 'Research and Development', 'RIT/TRANSPORT/Research and Development/Interaction with Industry', 'dg', 'Standard', 'RIT/AC/2024/TRANSPORT/Research and Development/00004', 'Yes', 32, 232, 'media\\Attachment_12_953623243104_33891_2024_07_31.pdf', '2024-08-20', 'dgfgsdgsg', NULL, NULL, 'Pending', NULL, NULL, '7777', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'sgfdsgdsfg', 'Transport_Incharge', NULL, NULL, NULL, NULL, NULL, NULL, 'Interaction with Industry', 'Pending', NULL, NULL, NULL, NULL, NULL, 'Pending', NULL, NULL, 'tic@ritrjpm.ac.in', 'Transport_Incharge', 'False');

-- --------------------------------------------------------

--
-- Table structure for table `application_status`
--

CREATE TABLE `application_status` (
  `Document_no` varchar(200) NOT NULL,
  `staff` varchar(100) DEFAULT NULL,
  `HOD` varchar(100) DEFAULT NULL,
  `GM` varchar(100) DEFAULT NULL,
  `Vice_Principal` varchar(100) DEFAULT NULL,
  `Principal` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `application_user`
--

CREATE TABLE `application_user` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `staff_id` varchar(100) NOT NULL,
  `Department` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `confirm_Password` varchar(100) NOT NULL,
  `Department_code` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `application_user`
--

INSERT INTO `application_user` (`id`, `Name`, `user_name`, `staff_id`, `Department`, `email`, `role`, `Password`, `confirm_Password`, `Department_code`) VALUES
(1, 'Technician', 'Technician', '1111', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', '1236@gmail.com', 'Technician', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(2, 'AD_HOD', 'AD_HOD', '2222', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', '1233@gfjdskj.cs', 'HOD', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(3, 'GM_ADMIN', 'GM_ADMIN', '3333', 'Office', '2312@dts.tu', 'GM', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(5, 'STAFF', 'STAFF', '4444', 'ARTIFICIAL INTELLIGENCE AND DATA SCIENCE', 'aasds@dts.jkh', 'Staff', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(7, 'VICE_PRINCIPLE', 'VICE_PRINCIPLE', '5555', 'OFFICE', 'v_p@ritrjpm.ac.in', 'Vice_Principal', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(8, 'PRINCIPAL', 'PRINCIPAL', '6666', 'OFFICE', 'prin@ritrjpm.ac.in', 'Principal', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(9, 'Transport_Incharge', 'Transport_Incharge', '7777', 'TRANSPORT', 'tic@ritrjpm.ac.in', 'Transport_Incharge', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(10, 'office_staff', 'office_staff', '8888', 'OFFICE', 'office_staff@ritrjpm.ac.in', 'OfficeStaff', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', ''),
(11, 'deputy_warden', 'deputy_warden', '9999', 'HOSTEL', 'deputy_warden@ritrjpm.ac.in', 'Deputywarden', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add e_approval', 7, 'add_e_approval'),
(26, 'Can change e_approval', 7, 'change_e_approval'),
(27, 'Can delete e_approval', 7, 'delete_e_approval'),
(28, 'Can view e_approval', 7, 'view_e_approval'),
(29, 'Can add status', 8, 'add_status'),
(30, 'Can change status', 8, 'change_status'),
(31, 'Can delete status', 8, 'delete_status'),
(32, 'Can view status', 8, 'view_status'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add auth_list', 10, 'add_auth_list'),
(38, 'Can change auth_list', 10, 'change_auth_list'),
(39, 'Can delete auth_list', 10, 'delete_auth_list'),
(40, 'Can view auth_list', 10, 'view_auth_list'),
(41, 'Can add clarification', 11, 'add_clarification'),
(42, 'Can change clarification', 11, 'change_clarification'),
(43, 'Can delete clarification', 11, 'delete_clarification'),
(44, 'Can view clarification', 11, 'view_clarification'),
(45, 'Can add auth_remarks', 12, 'add_auth_remarks'),
(46, 'Can change auth_remarks', 12, 'change_auth_remarks'),
(47, 'Can delete auth_remarks', 12, 'delete_auth_remarks'),
(48, 'Can view auth_remarks', 12, 'view_auth_remarks'),
(49, 'Can add doc_remarks', 13, 'add_doc_remarks'),
(50, 'Can change doc_remarks', 13, 'change_doc_remarks'),
(51, 'Can delete doc_remarks', 13, 'delete_doc_remarks'),
(52, 'Can view doc_remarks', 13, 'view_doc_remarks'),
(53, 'Can add allotment', 14, 'add_allotment'),
(54, 'Can change allotment', 14, 'change_allotment'),
(55, 'Can delete allotment', 14, 'delete_allotment'),
(56, 'Can view allotment', 14, 'view_allotment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(14, 'application', 'allotment'),
(10, 'application', 'auth_list'),
(12, 'application', 'auth_remarks'),
(11, 'application', 'clarification'),
(13, 'application', 'doc_remarks'),
(7, 'application', 'e_approval'),
(8, 'application', 'status'),
(9, 'application', 'user'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-19 06:33:52.963739'),
(2, 'auth', '0001_initial', '2024-08-19 06:33:53.163936'),
(3, 'admin', '0001_initial', '2024-08-19 06:33:53.219287'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-19 06:33:53.219287'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-19 06:33:53.230879'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-19 06:33:53.263193'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-19 06:33:53.290158'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-19 06:33:53.300854'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-19 06:33:53.305866'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-19 06:33:53.327949'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-19 06:33:53.329961'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-19 06:33:53.335114'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-19 06:33:53.339305'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-19 06:33:53.349287'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-19 06:33:53.356129'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-19 06:33:53.362503'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-19 06:33:53.373293'),
(18, 'sessions', '0001_initial', '2024-08-19 06:33:53.379272'),
(19, 'application', '0001_initial', '2024-08-19 06:42:08.621350'),
(20, 'application', '0002_e_approval_staff_id', '2024-08-19 06:42:08.630226'),
(21, 'application', '0003_e_approval_gm_date_e_approval_hod_date_and_more', '2024-08-19 06:42:08.645818'),
(22, 'application', '0004_auth_list_auth_remarks_clarification_doc_remarks_and_more', '2024-08-19 06:42:08.702935'),
(23, 'application', '0005_auth_list_staff_auth_list_staff_clarification_and_more', '2024-08-19 06:42:08.733795'),
(24, 'application', '0006_alter_doc_remarks_document_no', '2024-08-19 06:42:08.738781'),
(25, 'application', '0007_alter_e_approval_tran_no', '2024-08-19 06:42:08.740955'),
(26, 'application', '0008_user_department_code', '2024-08-19 06:42:08.747693'),
(27, 'application', '0009_status_alter_user_department_code', '2024-08-19 06:42:08.763997'),
(28, 'application', '0010_rename_sub_category_e_approval_head_of_account', '2024-08-19 06:42:08.768498'),
(29, 'application', '0011_e_approval_remarks_subject1', '2024-08-19 06:42:08.773414'),
(30, 'application', '0012_alter_e_approval_in_words', '2024-08-19 06:42:08.789196'),
(31, 'application', '0013_alter_e_approval_in_words_and_more', '2024-08-19 06:42:08.818484'),
(32, 'application', '0014_alter_e_approval_total_value', '2024-08-19 06:42:08.844066'),
(33, 'application', '0015_e_approval_creator', '2024-08-19 06:42:08.851704'),
(34, 'application', '0016_e_approval_gm_name_e_approval_hod_name_and_more', '2024-08-19 06:42:08.868309'),
(35, 'application', '0017_temp_doc_create', '2024-08-19 06:42:08.877464'),
(36, 'application', '0018_remove_temp_doc_create_tran_no', '2024-08-19 06:42:08.886223'),
(37, 'application', '0019_rename_attachment_temp_doc_create_temp_attachment_and_more', '2024-08-19 06:42:08.929708'),
(38, 'application', '0020_delete_temp_doc_create_alter_e_approval_document_no', '2024-08-19 06:42:08.938413'),
(39, 'application', '0021_temp_doc_create', '2024-08-19 06:42:08.944255'),
(40, 'application', '0022_delete_temp_doc_create_e_approval_doc_status', '2024-08-19 06:42:08.953086'),
(41, 'application', '0023_alter_e_approval_head_of_account', '2024-08-19 06:42:08.966133'),
(42, 'application', '0024_temp', '2024-08-19 06:42:08.972814'),
(43, 'application', '0025_delete_temp_e_approval_sub_category', '2024-08-19 06:42:08.978750'),
(44, 'application', '0026_alter_e_approval_tran_no', '2024-08-19 06:42:08.994215'),
(45, 'application', '0027_allotment_rename_principal_auth_list_principal_and_more', '2024-08-19 06:42:09.150776'),
(46, 'application', '0028_allotment_total_amount_alter_allotment_capitalgoods_and_more', '2024-08-19 08:26:45.003931'),
(47, 'application', '0029_allotment_balance_amount', '2024-08-19 08:45:55.711801'),
(48, 'application', '0030_alter_allotment_academic', '2024-08-20 03:39:36.796378'),
(49, 'application', '0031_alter_allotment_academic', '2024-08-20 06:17:04.238010');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0ca6zrv5k1vxw4s76d4uh2jzx43y5109', '.eJytzs0OgjAMAOB36ZkYGIMBJ01IjAfUNyCVtZGEH7ONeCC8u0O4ebWn9kv_ZpgsmRon94TCmYmCDVoNRbznGh1CMcNu1iHztwFiHxDAgD356lzVp7K6XGGf--WSXmhcT4PzfmNuG_JKPbadBxFH4qidPbjJqxm7bdrnd7T2PZr1JKZpgjLJRSiF4FzLSJHMUkWsG8mPDEOJEcfMHDGGivI8oyxlxQqFQlrfbcaBW9PX_9y6LB9lvmNK:1sgKva:-35e-Ys3u34jsYPfSIBmp9leRVzJD4WY40ULddh0Nvs', '2024-09-03 09:13:22.703945');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `application_allotment`
--
ALTER TABLE `application_allotment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `application_auth_list`
--
ALTER TABLE `application_auth_list`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_auth_remarks`
--
ALTER TABLE `application_auth_remarks`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_clarification`
--
ALTER TABLE `application_clarification`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_doc_remarks`
--
ALTER TABLE `application_doc_remarks`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_e_approval`
--
ALTER TABLE `application_e_approval`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_status`
--
ALTER TABLE `application_status`
  ADD PRIMARY KEY (`Document_no`);

--
-- Indexes for table `application_user`
--
ALTER TABLE `application_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `application_allotment`
--
ALTER TABLE `application_allotment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `application_user`
--
ALTER TABLE `application_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
