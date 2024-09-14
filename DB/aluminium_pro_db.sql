-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 11, 2024 at 06:00 AM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aluminium_pro_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add aluminum data', 6, 'add_aluminumdata'),
(22, 'Can change aluminum data', 6, 'change_aluminumdata'),
(23, 'Can delete aluminum data', 6, 'delete_aluminumdata'),
(24, 'Can view aluminum data', 6, 'view_aluminumdata'),
(25, 'Can add cost and profitability', 7, 'add_costandprofitability'),
(26, 'Can change cost and profitability', 7, 'change_costandprofitability'),
(27, 'Can delete cost and profitability', 7, 'delete_costandprofitability'),
(28, 'Can view cost and profitability', 7, 'view_costandprofitability'),
(29, 'Can add environmental impact', 8, 'add_environmentalimpact'),
(30, 'Can change environmental impact', 8, 'change_environmentalimpact'),
(31, 'Can delete environmental impact', 8, 'delete_environmentalimpact'),
(32, 'Can view environmental impact', 8, 'view_environmentalimpact'),
(33, 'Can add inventory management', 9, 'add_inventorymanagement'),
(34, 'Can change inventory management', 9, 'change_inventorymanagement'),
(35, 'Can delete inventory management', 9, 'delete_inventorymanagement'),
(36, 'Can view inventory management', 9, 'view_inventorymanagement'),
(37, 'Can add production efficiency', 10, 'add_productionefficiency'),
(38, 'Can change production efficiency', 10, 'change_productionefficiency'),
(39, 'Can delete production efficiency', 10, 'delete_productionefficiency'),
(40, 'Can view production efficiency', 10, 'view_productionefficiency'),
(41, 'Can add real time metric', 11, 'add_realtimemetric'),
(42, 'Can change real time metric', 11, 'change_realtimemetric'),
(43, 'Can delete real time metric', 11, 'delete_realtimemetric'),
(44, 'Can view real time metric', 11, 'view_realtimemetric'),
(45, 'Can add wastage and loss', 12, 'add_wastageandloss'),
(46, 'Can change wastage and loss', 12, 'change_wastageandloss'),
(47, 'Can delete wastage and loss', 12, 'delete_wastageandloss'),
(48, 'Can view wastage and loss', 12, 'view_wastageandloss'),
(49, 'Can add user', 13, 'add_customuser'),
(50, 'Can change user', 13, 'change_customuser'),
(51, 'Can delete user', 13, 'delete_customuser'),
(52, 'Can view user', 13, 'view_customuser'),
(53, 'Can add profile', 14, 'add_profile'),
(54, 'Can change profile', 14, 'change_profile'),
(55, 'Can delete profile', 14, 'delete_profile'),
(56, 'Can view profile', 14, 'view_profile');

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_aluminumdata`
--

DROP TABLE IF EXISTS `baseapp_aluminumdata`;
CREATE TABLE IF NOT EXISTS `baseapp_aluminumdata` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `wastage` double NOT NULL,
  `loss` double NOT NULL,
  `profile` varchar(100) NOT NULL,
  `profit` double NOT NULL,
  `recycled_weight` double NOT NULL,
  `energy_consumption` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_aluminumdata`
--

INSERT INTO `baseapp_aluminumdata` (`id`, `date`, `wastage`, `loss`, `profile`, `profit`, `recycled_weight`, `energy_consumption`) VALUES
(1, '2024-09-11', 130.18, 86.01, 'Profile_0', 3713.96, 99.99, 750.42),
(2, '2024-09-10', 167.2, 55, 'Profile_1', 2069.75, 98.59, 985.57),
(3, '2024-09-09', 109.48, 68.4, 'Profile_2', 2831.96, 76.28, 573.05),
(4, '2024-09-08', 157.51, 71.72, 'Profile_3', 2039.06, 73.49, 838.51),
(5, '2024-09-07', 172.81, 91.13, 'Profile_4', 3910.73, 90.66, 788.05),
(6, '2024-09-06', 123.9, 98.02, 'Profile_5', 3336.34, 64.81, 908.08),
(7, '2024-09-05', 154.81, 86.55, 'Profile_6', 4148.65, 80.91, 784.23),
(8, '2024-09-04', 145.35, 58.05, 'Profile_7', 1883, 69.13, 826.67),
(9, '2024-09-03', 145.88, 51.98, 'Profile_8', 3371.46, 61.02, 569.08),
(10, '2024-09-02', 130.05, 72.15, 'Profile_9', 4609.87, 81.79, 909.55);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_costandprofitability`
--

DROP TABLE IF EXISTS `baseapp_costandprofitability`;
CREATE TABLE IF NOT EXISTS `baseapp_costandprofitability` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `raw_material_cost` double NOT NULL,
  `energy_consumption` double NOT NULL,
  `labor_cost` double NOT NULL,
  `total_cost` double NOT NULL,
  `revenue` double NOT NULL,
  `profit_margin` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_costandprofitability`
--

INSERT INTO `baseapp_costandprofitability` (`id`, `date`, `raw_material_cost`, `energy_consumption`, `labor_cost`, `total_cost`, `revenue`, `profit_margin`) VALUES
(1, '2024-09-11', 1037.36, 871.78, 385.72, 2294.86, 3612.36, 36.47),
(2, '2024-09-10', 1345.41, 761.03, 335.59, 2442.03, 4888.94, 50.05),
(3, '2024-09-09', 1238.97, 645.74, 358.9, 2243.61, 5271.65, 57.44),
(4, '2024-09-08', 1289.04, 608.58, 351.66, 2249.28, 3332.72, 32.51),
(5, '2024-09-07', 1930.79, 505.84, 321.35, 2757.98, 5736.89, 51.93),
(6, '2024-09-06', 1216.78, 869.14, 423.36, 2509.28, 5990, 58.11),
(7, '2024-09-05', 1799.11, 676.93, 342.58, 2818.62, 4546.76, 38.01),
(8, '2024-09-04', 1423.59, 836.17, 390.96, 2650.72, 3215.77, 17.57),
(9, '2024-09-03', 1892.82, 887.99, 395.82, 3176.63, 3643.81, 12.82),
(10, '2024-09-02', 1076.82, 756.19, 454.14, 2287.15, 5279.06, 56.68);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_customuser`
--

DROP TABLE IF EXISTS `baseapp_customuser`;
CREATE TABLE IF NOT EXISTS `baseapp_customuser` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_customuser`
--

INSERT INTO `baseapp_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`) VALUES
(1, 'pbkdf2_sha256$870000$kel8lwjNvKINtJBWf3Jkev$ubUgOW/wz1wSfsiYhKB313Mm6lIwpygkawo+SvN9w+4=', '2024-09-11 05:44:20.752217', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2024-09-11 05:42:44.731574', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_customuser_groups`
--

DROP TABLE IF EXISTS `baseapp_customuser_groups`;
CREATE TABLE IF NOT EXISTS `baseapp_customuser_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BaseApp_customuser_groups_customuser_id_group_id_2ad20c12_uniq` (`customuser_id`,`group_id`),
  KEY `BaseApp_customuser_groups_customuser_id_71024356` (`customuser_id`),
  KEY `BaseApp_customuser_groups_group_id_10e38eb5` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_customuser_user_permissions`
--

DROP TABLE IF EXISTS `baseapp_customuser_user_permissions`;
CREATE TABLE IF NOT EXISTS `baseapp_customuser_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `BaseApp_customuser_user__customuser_id_permission_f43ba719_uniq` (`customuser_id`,`permission_id`),
  KEY `BaseApp_customuser_user_permissions_customuser_id_06dfc6ce` (`customuser_id`),
  KEY `BaseApp_customuser_user_permissions_permission_id_51e615ea` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_environmentalimpact`
--

DROP TABLE IF EXISTS `baseapp_environmentalimpact`;
CREATE TABLE IF NOT EXISTS `baseapp_environmentalimpact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `carbon_footprint` double NOT NULL,
  `waste_management_efficiency` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_environmentalimpact`
--

INSERT INTO `baseapp_environmentalimpact` (`id`, `date`, `carbon_footprint`, `waste_management_efficiency`) VALUES
(1, '2024-09-11', 234.74, 90.77),
(2, '2024-09-10', 268.2, 70.79),
(3, '2024-09-09', 284.16, 77.35),
(4, '2024-09-08', 139.87, 93.16),
(5, '2024-09-07', 232.51, 58.35),
(6, '2024-09-06', 204.96, 62.84),
(7, '2024-09-05', 140.35, 93.77),
(8, '2024-09-04', 145.69, 55.46),
(9, '2024-09-03', 255.78, 82.51),
(10, '2024-09-02', 275.94, 82.35);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_inventorymanagement`
--

DROP TABLE IF EXISTS `baseapp_inventorymanagement`;
CREATE TABLE IF NOT EXISTS `baseapp_inventorymanagement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `raw_material_requirement` double NOT NULL,
  `current_inventory` double NOT NULL,
  `future_demand` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_inventorymanagement`
--

INSERT INTO `baseapp_inventorymanagement` (`id`, `date`, `raw_material_requirement`, `current_inventory`, `future_demand`) VALUES
(1, '2024-09-11', 1486.73, 1316.39, 170.34),
(2, '2024-09-10', 1203.08, 1117.03, 86.05),
(3, '2024-09-09', 1725.54, 512.48, 1213.06),
(4, '2024-09-08', 1459.37, 925.8, 533.57),
(5, '2024-09-07', 1301.03, 1351.22, -50.19),
(6, '2024-09-06', 1265.91, 1117.56, 148.35),
(7, '2024-09-05', 1953.25, 1293.2, 660.05),
(8, '2024-09-04', 1346.77, 1141.05, 205.72),
(9, '2024-09-03', 1333.63, 1218.83, 114.8),
(10, '2024-09-02', 1420.33, 1149.4, 270.93);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_productionefficiency`
--

DROP TABLE IF EXISTS `baseapp_productionefficiency`;
CREATE TABLE IF NOT EXISTS `baseapp_productionefficiency` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `temperature` double NOT NULL,
  `pressure` double NOT NULL,
  `production_output` double NOT NULL,
  `optimization_score` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_productionefficiency`
--

INSERT INTO `baseapp_productionefficiency` (`id`, `date`, `temperature`, `pressure`, `production_output`, `optimization_score`) VALUES
(1, '2024-09-11', 302.83, 1363.78, 281.97, 82.38),
(2, '2024-09-10', 430.06, 1206.93, 294.87, 61.76),
(3, '2024-09-09', 347.8, 1343.66, 377.49, 99.45),
(4, '2024-09-08', 310.73, 1461.27, 375.09, 51.79),
(5, '2024-09-07', 398.73, 1034.43, 269.27, 81.18),
(6, '2024-09-06', 317.77, 1075.12, 221.75, 73.33),
(7, '2024-09-05', 437.23, 1415.78, 369.52, 72.37),
(8, '2024-09-04', 338.89, 1444.07, 235.74, 95.26),
(9, '2024-09-03', 484.03, 1282.02, 202.08, 99.08),
(10, '2024-09-02', 392.93, 1304.6, 317.03, 86.83);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_profile`
--

DROP TABLE IF EXISTS `baseapp_profile`;
CREATE TABLE IF NOT EXISTS `baseapp_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `avatar` varchar(100) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `job_position` varchar(255) NOT NULL,
  `date_of_birth` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `bio` longtext NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_profile`
--

INSERT INTO `baseapp_profile` (`id`, `avatar`, `full_name`, `phone_number`, `job_position`, `date_of_birth`, `gender`, `bio`, `user_id`) VALUES
(1, 'avatars/photo_2024-08-26_19-39-00.jpg', 'Santhosh Raj K', '9345683396', 'Full Stack Python Developer', '2003-12-18', 'M', 'learning!...', 1);

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_realtimemetric`
--

DROP TABLE IF EXISTS `baseapp_realtimemetric`;
CREATE TABLE IF NOT EXISTS `baseapp_realtimemetric` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `metric_name` varchar(100) NOT NULL,
  `current_value` double NOT NULL,
  `threshold_value` double NOT NULL,
  `alert_triggered` tinyint(1) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `BaseApp_realtimemetric_metric_name_72cdea5e` (`metric_name`),
  KEY `BaseApp_realtimemetric_timestamp_1439ecba` (`timestamp`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_realtimemetric`
--

INSERT INTO `baseapp_realtimemetric` (`id`, `metric_name`, `current_value`, `threshold_value`, `alert_triggered`, `timestamp`) VALUES
(1, 'Metric_0', 63.85, 64.47, 0, '2024-09-11 05:43:09.111326'),
(2, 'Metric_1', 92.59, 87.19, 0, '2024-09-10 05:43:09.136707'),
(3, 'Metric_2', 85.88, 78.17, 1, '2024-09-09 05:43:09.143651'),
(4, 'Metric_3', 88.14, 89.46, 0, '2024-09-08 05:43:09.143651'),
(5, 'Metric_4', 74.33, 86.14, 0, '2024-09-07 05:43:09.157189'),
(6, 'Metric_5', 73.55, 89.09, 1, '2024-09-06 05:43:09.164149'),
(7, 'Metric_6', 73.16, 84.01, 1, '2024-09-05 05:43:09.169801'),
(8, 'Metric_7', 93.81, 81.53, 0, '2024-09-04 05:43:09.178117'),
(9, 'Metric_8', 96.31, 60.42, 0, '2024-09-03 05:43:09.190161'),
(10, 'Metric_9', 59.32, 71.63, 1, '2024-09-02 05:43:09.190161');

-- --------------------------------------------------------

--
-- Table structure for table `baseapp_wastageandloss`
--

DROP TABLE IF EXISTS `baseapp_wastageandloss`;
CREATE TABLE IF NOT EXISTS `baseapp_wastageandloss` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `material_loss` double NOT NULL,
  `recyclability_score` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `baseapp_wastageandloss`
--

INSERT INTO `baseapp_wastageandloss` (`id`, `date`, `material_loss`, `recyclability_score`) VALUES
(1, '2024-09-11', 27.96, 31.17),
(2, '2024-09-10', 26.78, 27.63),
(3, '2024-09-09', 45.54, 94.47),
(4, '2024-09-08', 42.22, 78.59),
(5, '2024-09-07', 40.54, 0.8),
(6, '2024-09-06', 19.33, 62.44),
(7, '2024-09-05', 38.33, 33.16),
(8, '2024-09-04', 23.31, 5.26),
(9, '2024-09-03', 32.53, 48.85),
(10, '2024-09-02', 31.25, 26.95);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'BaseApp', 'aluminumdata'),
(7, 'BaseApp', 'costandprofitability'),
(8, 'BaseApp', 'environmentalimpact'),
(9, 'BaseApp', 'inventorymanagement'),
(10, 'BaseApp', 'productionefficiency'),
(11, 'BaseApp', 'realtimemetric'),
(12, 'BaseApp', 'wastageandloss'),
(13, 'BaseApp', 'customuser'),
(14, 'BaseApp', 'profile');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-09-11 05:42:20.398406'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-09-11 05:42:20.462729'),
(3, 'auth', '0001_initial', '2024-09-11 05:42:20.700852'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-09-11 05:42:20.732892'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-09-11 05:42:20.743338'),
(6, 'auth', '0004_alter_user_username_opts', '2024-09-11 05:42:20.748074'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-09-11 05:42:20.759703'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-09-11 05:42:20.760567'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-09-11 05:42:20.766835'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-09-11 05:42:20.772881'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-09-11 05:42:20.779669'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-09-11 05:42:20.808789'),
(13, 'auth', '0011_update_proxy_permissions', '2024-09-11 05:42:20.821349'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-09-11 05:42:20.828106'),
(15, 'BaseApp', '0001_initial', '2024-09-11 05:42:21.293524'),
(16, 'admin', '0001_initial', '2024-09-11 05:42:21.477743'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-09-11 05:42:21.488738'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-09-11 05:42:21.502060'),
(19, 'sessions', '0001_initial', '2024-09-11 05:42:21.534722');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('yri5yvo14kijwk2pw82qo66dxi5l94sx', '.eJxVjMsOwiAQRf-FtSEMUB4u3fsNhIFBqgaS0q6M_65NutDtPefcFwtxW2vYBi1hzuzMgJ1-N4zpQW0H-R7brfPU27rMyHeFH3Twa8_0vBzu30GNo35rb6wWjgp6CYDKCQHKFAMJwUTCyYFwHoiUQFm0BK1EMs4WOXlntSb2_gC1SDaA:1soG9M:fR14Sd7lwotgWxN6eCVGiKAYlljV9JM1clABkh19z_s', '2024-09-25 05:44:20.758759');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
