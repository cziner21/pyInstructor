-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Hoszt: 127.0.0.1
-- Létrehozás ideje: 2014. Nov 18. 08:19
-- Szerver verzió: 5.6.16
-- PHP verzió: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Adatbázis: `pyinstructor`
--
CREATE DATABASE IF NOT EXISTS `pyinstructor` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pyinstructor`;

DELIMITER $$
--
-- Eljárások
--
DROP PROCEDURE IF EXISTS `sp_DeleteAnswer`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteAnswer`(IN `p_id` INT)
BEGIN 

    DELETE FROM answers
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_DeleteQuestion`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteQuestion`(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM questions       
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_DeleteTopic`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteTopic`(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM topics
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_DeleteUser`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_DeleteUser`(
     	IN  p_id			   INT          
                
     )
BEGIN 

    DELETE FROM users
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_InsertIntoUsers`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_InsertIntoUsers`(IN `p_firstname` VARCHAR(255), IN `p_lastname` VARCHAR(255), IN `p_email` VARCHAR(255), IN `p_password` VARCHAR(255))
BEGIN 

    INSERT INTO users
         (
           firstname, 
           lastname, 
           email, 
           password
         )
    VALUES 
         ( 
           p_firstname, 
           p_lastname, 
           p_email, 
           p_password                 
         ) ; 
END$$

DROP PROCEDURE IF EXISTS `sp_UpdateAnswers`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateAnswers`(IN `p_id` INT, IN `p_answerText` VARCHAR(255), IN `p_isItCorrect` INT, IN `p_topicId` INT)
BEGIN 

    UPDATE answers
    SET                 
       answerText = p_answerText,
       isItCorrect = p_isItCorrect,
       topicId = p_topicId
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_UpdateOwnuserDataAndProfil`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateOwnuserDataAndProfil`(IN `p_id` INT, IN `p_firstName` VARCHAR(255), IN `p_lastName` VARCHAR(255), IN `p_email` VARCHAR(255), IN `p_password` VARCHAR(255), IN `p_city` VARCHAR(255), IN `p_address` VARCHAR(255), IN `p_phone` VARCHAR(100), IN `p_birthday` DATE)
BEGIN 

    UPDATE users u
    INNER JOIN profil p ON u.id = p.userId
    SET                 
       u.firstName = p_firstName,
       u.lastName = p_lastName,
       u.email = p_email,
       u.password = p_password,
       p.city = p_city,
       p.address = p_address,
       p.phone = p_phone,
       p.birthday = p_birthday
       
    WHERE 
       u.id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_UpdateQuestions`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateQuestions`(IN `p_id` INT, IN `p_questionText` VARCHAR(255), IN `p_topicId` INT)
BEGIN 

    UPDATE questions
    SET                 
       questionText = p_questionText,
       topicId = p_topicId
    WHERE 
       id = p_id;

END$$

DROP PROCEDURE IF EXISTS `sp_UpdateUserAndProfil`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_UpdateUserAndProfil`(IN `p_id` INT, IN `p_firstName` VARCHAR(255), IN `p_lastName` VARCHAR(255), IN `p_email` VARCHAR(255), IN `p_city` VARCHAR(255), IN `P_address` VARCHAR(255), IN `p_phone` VARCHAR(100), IN `p_birthday` DATE, IN `p_privilidge` INT(1))
BEGIN 

    UPDATE users u
    INNER JOIN profil p ON u.id = p.userId
    SET                 
       u.firstName = p_firstName,
       u.lastName = p_lastName,
       u.email = p_email,
       p.city = p_city,
       p.address = p_address,
       p.phone = p_phone,
       p.birthday = p_birthday,
       p.privilidge = p_privilidge
    WHERE 
       u.id = p_id;

END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `answers`
--

DROP TABLE IF EXISTS `answers`;
CREATE TABLE IF NOT EXISTS `answers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answerText` text NOT NULL,
  `questionId` int(11) NOT NULL,
  `isItCorrect` tinyint(1) DEFAULT NULL,
  `topicId` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_answers_questions1_idx` (`questionId`),
  KEY `fk_answers_topics1_idx` (`topicId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=164 ;

--
-- A tábla adatainak kiíratása `answers`
--

INSERT INTO `answers` (`id`, `answerText`, `questionId`, `isItCorrect`, `topicId`) VALUES
(79, 'A constructor can be used to set default values and limit instantiation.', 39, 1, 32),
(80, 'C# provides a copy constructor.', 39, NULL, 32),
(81, 'Destructors are used with classes as well as structures.', 39, NULL, 32),
(82, 'A class can have more than one destructor.', 39, NULL, 32),
(88, 'Static functions can access only static data. ', 41, 1, 32),
(89, 'Static functions cannot call instance function', 41, 1, 32),
(90, 'It is necessary to initialize static data', 41, NULL, 32),
(91, 'Instance functions can call static functions and access static data.', 41, 1, 32),
(92, 'this reference is passed to static functions. ', 41, NULL, 32),
(93, 'If we provide a one-argument constructor then the compiler still provides a zero-argument constructor', 42, NULL, 32),
(94, 'Static constructors can use optional arguments.', 42, NULL, 32),
(95, 'Overloaded constructors cannot use optional arguments', 42, NULL, 32),
(96, 'If we do not provide a constructor, then the compiler provides a zero-argument constructor.', 42, 1, 32),
(97, 'Type of arguments', 43, 0, 32),
(98, 'Return type of method', 43, 0, 32),
(99, 'Number of argument', 43, 1, 32),
(100, 'Names of methods ', 43, 0, 32),
(101, 'Order of arguments ', 43, 0, 32),
(102, 'Yes', 44, NULL, 32),
(103, 'No', 44, 1, 32),
(140, 'rowspan="2" paraccsal', 54, NULL, 35),
(141, 'cellspan="2" paranccsal', 54, NULL, 35),
(142, 'colspan="2" paranccsal', 54, 1, 35),
(143, 'columnspan="2" paranccsal', 54, NULL, 35),
(144, '.kozepre{ margin: 0 auto; }', 55, 0, 35),
(145, '#kozepre{ margin 0 auto;}', 55, 1, 35),
(146, '4', 56, 1, 38),
(147, '3', 56, NULL, 38),
(148, '2', 56, NULL, 38),
(149, '6', 56, NULL, 38),
(150, '62', 57, NULL, 38),
(151, '36', 57, 1, 38),
(152, '6', 57, NULL, 38),
(153, '10', 58, 0, 38),
(154, '13/3', 58, 1, 38),
(155, '4,33', 58, 1, 38),
(156, '13', 58, 0, 38),
(157, 'Sample s = new Sample();', 59, 1, 32),
(158, 'Sample s;', 59, NULL, 32),
(159, 'Sample s; s = new Sample();', 59, 1, 32),
(160, 's = new Sample();', 59, NULL, 32),
(161, 'vdfvlétz', 60, 1, 46),
(162, 'ggdhth', 60, NULL, 46),
(163, 'gbdgdfg', 60, NULL, 46);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `profil`
--

DROP TABLE IF EXISTS `profil`;
CREATE TABLE IF NOT EXISTS `profil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profilPictureURL` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `userId` int(11) NOT NULL,
  `birthday` date DEFAULT NULL,
  `privilidge` int(1) NOT NULL DEFAULT '1' COMMENT '0- admin\n1- user',
  PRIMARY KEY (`id`),
  KEY `fk_profil_users1_idx` (`userId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=26 ;

--
-- A tábla adatainak kiíratása `profil`
--

INSERT INTO `profil` (`id`, `profilPictureURL`, `city`, `address`, `phone`, `userId`, `birthday`, `privilidge`) VALUES
(13, NULL, 'Eger', 'Kazinczy Ferenc utca 1/B', '+30304467980', 13, '1990-04-21', 0),
(18, NULL, 'Miskolc', 'Hatvani út 31.', '', 18, '1965-10-28', 1),
(22, NULL, 'Budapest', 'Hungária körút 81. 6. emelet 30/B', '', 21, NULL, 0),
(23, NULL, NULL, NULL, NULL, 22, NULL, 1),
(25, NULL, 'Gyor', '', '', 24, NULL, 1);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `questions`
--

DROP TABLE IF EXISTS `questions`;
CREATE TABLE IF NOT EXISTS `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `questionText` text NOT NULL,
  `topicId` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_questions_topics1_idx` (`topicId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=61 ;

--
-- A tábla adatainak kiíratása `questions`
--

INSERT INTO `questions` (`id`, `questionText`, `topicId`) VALUES
(39, 'Which of the following statements is correct?', 32),
(41, 'Which of the following statements are correct about static functions? ', 32),
(42, 'Which of the following statements is correct about constructors?', 32),
(43, 'In which of the following should the methods of a class differ if they are to be treated as overloaded methods? \n', 32),
(44, 'Can static procedures access instance data', 32),
(54, 'Hogyan kell HTML-ben 2 cellát összevonni?', 35),
(55, 'Css segítségével, hogyan tudunk egy divet középre hekyezni?\nA div így néz ki: <div id="kozepre"><a href="google.hu">Google</a></div>', 35),
(56, 'Mennyi 2+2?', 38),
(57, 'Mennyi 6*6', 38),
(58, 'Mennyi x értéke?\n3x + 2 = 15', 38),
(59, 'Which of the following is the correct way to create an object of the class Sample?', 32),
(60, 'vxvdsf', 46);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `results`
--

DROP TABLE IF EXISTS `results`;
CREATE TABLE IF NOT EXISTS `results` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `result` int(11) NOT NULL,
  `userId` int(11) NOT NULL,
  `topicId` int(11) NOT NULL,
  `examDate` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_results_users1_idx` (`userId`),
  KEY `fk_results_topics1_idx` (`topicId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=151 ;

--
-- A tábla adatainak kiíratása `results`
--

INSERT INTO `results` (`id`, `result`, `userId`, `topicId`, `examDate`) VALUES
(91, 5, 13, 32, '2014-11-13 17:16:36'),
(92, 8, 13, 32, '2014-11-13 17:18:56'),
(93, 3, 21, 32, '2014-11-13 17:20:56'),
(94, 5, 13, 32, '2014-11-13 18:41:13'),
(95, 10, 13, 32, '2014-11-13 18:42:02'),
(96, 20, 13, 32, '2014-11-13 18:42:02'),
(97, 7, 21, 32, '2014-11-13 18:48:57'),
(98, 1, 21, 32, '2014-11-13 18:49:55'),
(99, 2, 21, 32, '2014-11-13 18:49:56'),
(100, 7, 21, 32, '2014-11-13 18:52:36'),
(101, 0, 21, 32, '2014-11-13 18:52:59'),
(102, 0, 21, 32, '2014-11-13 18:52:59'),
(103, 4, 13, 32, '2014-11-13 18:58:30'),
(104, 0, 13, 32, '2014-11-13 19:19:48'),
(105, 0, 13, 32, '2014-11-13 19:19:58'),
(106, 0, 13, 32, '2014-11-13 19:19:58'),
(107, 4, 13, 32, '2014-11-13 21:33:06'),
(108, 6, 13, 32, '2014-11-13 21:34:02'),
(109, 12, 13, 32, '2014-11-13 21:34:02'),
(110, 4, 21, 32, '2014-11-13 21:34:47'),
(111, 5, 13, 32, '2014-11-13 22:15:24'),
(112, 1, 13, 32, '2014-11-13 22:16:25'),
(113, 2, 13, 32, '2014-11-13 22:16:25'),
(114, 2, 21, 32, '2014-11-13 22:16:59'),
(115, 4, 21, 32, '2014-11-13 22:17:24'),
(116, 8, 21, 32, '2014-11-13 22:17:24'),
(117, 1, 13, 32, '2014-11-13 22:21:39'),
(118, 1, 13, 32, '2014-11-13 22:21:47'),
(119, 2, 13, 32, '2014-11-13 22:21:47'),
(120, 1, 13, 32, '2014-11-13 22:23:52'),
(121, 1, 13, 32, '2014-11-13 22:23:59'),
(122, 2, 13, 32, '2014-11-13 22:23:59'),
(123, 3, 13, 32, '2014-11-13 22:27:02'),
(124, 1, 13, 32, '2014-11-13 22:27:12'),
(125, 2, 13, 32, '2014-11-13 22:27:12'),
(126, 5, 13, 32, '2014-11-13 22:30:30'),
(127, 10, 13, 32, '2014-11-13 22:30:30'),
(128, 15, 13, 32, '2014-11-13 22:30:30'),
(129, 6, 13, 32, '2014-11-13 22:35:31'),
(130, 1, 13, 32, '2014-11-13 22:35:50'),
(131, 2, 13, 32, '2014-11-13 22:35:50'),
(132, 3, 13, 32, '2014-11-13 22:45:53'),
(133, 1, 13, 32, '2014-11-13 22:46:04'),
(135, 7, 13, 32, '2014-11-14 10:29:11'),
(139, 4, 21, 32, '2014-11-14 10:30:40'),
(140, 8, 21, 32, '2014-11-14 10:30:40'),
(141, 2, 13, 35, '2014-11-15 08:51:03'),
(142, 4, 13, 38, '2014-11-15 08:54:31'),
(143, 2, 13, 38, '2014-11-15 08:54:57'),
(144, 3, 21, 38, '2014-11-15 08:55:52'),
(145, 0, 13, 32, '2014-11-15 12:35:34'),
(146, 12, 13, 32, '2014-11-15 15:39:13'),
(147, 24, 13, 32, '2014-11-15 15:39:14'),
(148, 36, 13, 32, '2014-11-15 15:39:14'),
(149, 8, 13, 32, '2014-11-15 15:40:54'),
(150, 4, 24, 38, '2014-11-18 07:57:28');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `topics`
--

DROP TABLE IF EXISTS `topics`;
CREATE TABLE IF NOT EXISTS `topics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=47 ;

--
-- A tábla adatainak kiíratása `topics`
--

INSERT INTO `topics` (`id`, `name`) VALUES
(32, 'C#'),
(46, 'Css'),
(35, 'Html'),
(34, 'Java'),
(38, 'Math'),
(40, 'Python');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `topics_user_conn`
--

DROP TABLE IF EXISTS `topics_user_conn`;
CREATE TABLE IF NOT EXISTS `topics_user_conn` (
  `topicsId` int(11) NOT NULL,
  `usersId` int(11) NOT NULL,
  KEY `fk_topics_has_users_users1_idx` (`usersId`),
  KEY `fk_topics_has_users_topics1_idx` (`topicsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- A tábla adatainak kiíratása `topics_user_conn`
--

INSERT INTO `topics_user_conn` (`topicsId`, `usersId`) VALUES
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 21),
(32, 13),
(32, 13),
(32, 13),
(32, 21),
(32, 21),
(32, 21),
(32, 21),
(32, 21),
(32, 21),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 21),
(32, 13),
(32, 13),
(32, 13),
(32, 21),
(32, 21),
(32, 21),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 21),
(32, 21),
(32, 13),
(35, 13),
(35, 13),
(35, 13),
(38, 13),
(38, 13),
(38, 13),
(38, 13),
(38, 13),
(38, 21),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(32, 13),
(38, 24);

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `useranswers`
--

DROP TABLE IF EXISTS `useranswers`;
CREATE TABLE IF NOT EXISTS `useranswers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `questionId` int(11) NOT NULL,
  `answerId` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_userAnswers_questions1_idx` (`questionId`),
  KEY `fk_userAnswers_answers1_idx` (`answerId`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=359 ;

--
-- A tábla adatainak kiíratása `useranswers`
--

INSERT INTO `useranswers` (`id`, `questionId`, `answerId`) VALUES
(123, 39, 79),
(124, 41, 89),
(125, 42, 93),
(126, 43, 100),
(127, 44, 103),
(130, 39, 79),
(131, 41, 88),
(132, 41, 89),
(133, 41, 91),
(134, 42, 95),
(135, 43, 97),
(136, 44, 103),
(140, 39, 79),
(141, 41, 91),
(142, 42, 93),
(143, 43, 99),
(144, 44, 102),
(146, 39, 79),
(147, 41, 92),
(148, 42, 96),
(149, 43, 97),
(150, 44, 103),
(153, 39, 79),
(154, 41, 88),
(155, 41, 89),
(156, 41, 91),
(157, 42, 96),
(158, 43, 99),
(159, 44, 103),
(163, 39, 79),
(164, 41, 88),
(165, 41, 89),
(166, 41, 91),
(167, 42, 96),
(168, 43, 99),
(169, 44, 103),
(173, 39, 79),
(174, 41, 88),
(175, 41, 89),
(176, 41, 91),
(177, 42, 96),
(178, 43, 100),
(179, 44, 102),
(182, 39, 79),
(183, 39, 79),
(184, 39, 79),
(185, 41, 88),
(186, 41, 89),
(187, 41, 91),
(188, 42, 95),
(189, 43, 99),
(190, 44, 103),
(192, 43, 97),
(193, 43, 97),
(194, 39, 79),
(195, 41, 88),
(196, 41, 89),
(197, 41, 91),
(198, 39, 79),
(199, 41, 88),
(200, 41, 89),
(201, 41, 91),
(202, 39, 79),
(203, 41, 88),
(204, 41, 89),
(205, 41, 91),
(206, 42, 93),
(207, 43, 99),
(208, 44, 103),
(209, 39, 79),
(210, 41, 88),
(211, 41, 89),
(212, 41, 91),
(213, 42, 93),
(214, 43, 99),
(215, 44, 103),
(216, 39, 79),
(217, 41, 88),
(218, 41, 89),
(219, 41, 91),
(220, 39, 79),
(221, 44, 103),
(225, 44, 103),
(226, 44, 103),
(227, 39, 79),
(228, 42, 95),
(229, 44, 103),
(230, 44, 103),
(234, 44, 103),
(238, 39, 79),
(239, 39, 79),
(240, 39, 79),
(241, 39, 79),
(242, 39, 79),
(243, 39, 79),
(244, 39, 79),
(245, 41, 88),
(246, 41, 89),
(247, 41, 92),
(248, 39, 79),
(249, 39, 79),
(250, 39, 79),
(251, 44, 103),
(255, 39, 79),
(256, 44, 103),
(260, 39, 79),
(261, 44, 103),
(265, 39, 79),
(266, 41, 88),
(267, 41, 89),
(268, 41, 91),
(269, 42, 96),
(270, 43, 100),
(271, 44, 103),
(272, 39, 79),
(273, 39, 79),
(277, 39, 79),
(279, 39, 79),
(280, 41, 88),
(281, 41, 89),
(282, 41, 91),
(283, 42, 96),
(284, 43, 99),
(285, 44, 103),
(289, 39, 79),
(293, 39, 79),
(297, 54, 142),
(298, 55, 145),
(299, 56, 146),
(300, 57, 151),
(301, 58, 154),
(302, 58, 155),
(303, 56, 147),
(304, 57, 151),
(305, 58, 154),
(306, 56, 146),
(307, 57, 152),
(308, 58, 154),
(309, 58, 155),
(310, 39, 79),
(311, 41, 88),
(312, 41, 89),
(313, 41, 91),
(314, 42, 96),
(315, 43, 99),
(316, 44, 103),
(320, 59, 157),
(321, 59, 159),
(322, 39, 79),
(323, 41, 88),
(324, 41, 89),
(325, 41, 91),
(326, 42, 96),
(327, 43, 99),
(328, 44, 103),
(332, 59, 157),
(333, 59, 159),
(334, 39, 79),
(335, 41, 88),
(336, 41, 89),
(337, 41, 91),
(338, 42, 96),
(339, 43, 99),
(340, 44, 103),
(344, 59, 157),
(345, 59, 159),
(346, 39, 79),
(347, 41, 88),
(348, 41, 89),
(349, 41, 91),
(350, 42, 95),
(351, 43, 99),
(352, 44, 103),
(353, 59, 157),
(354, 59, 159),
(355, 56, 146),
(356, 57, 151),
(357, 58, 154),
(358, 58, 155);

-- --------------------------------------------------------

--
-- A nézet helyettes szerkezete `userlist`
--
DROP VIEW IF EXISTS `userlist`;
CREATE TABLE IF NOT EXISTS `userlist` (
`id` int(11)
,`fullName` varchar(511)
,`email` varchar(255)
,`city` varchar(255)
,`address` varchar(255)
,`phone` varchar(100)
,`birthday` date
,`registered` datetime
,`privilidge` int(1)
);
-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `registered` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=25 ;

--
-- A tábla adatainak kiíratása `users`
--

INSERT INTO `users` (`id`, `firstName`, `lastName`, `email`, `password`, `registered`) VALUES
(13, 'Ádám ', 'Cziner', 'cziner.adam@gmail.com', 'e9b9b0b275153d1300f7fe51fe12024166f4b9ec3921f5f4e592c3136c7852cf2b4012cd0033c4f4a73529b961b157025b476cacfdabfe43d714b34edf8510f2', '2014-11-09 11:29:43'),
(18, 'János', 'Kovács', 'kovacs@gmail.com', '4cb70c6454cd3c77b948201c71ca942409837b445490f7c5ee5dcf0f76669908a6ed44b51c71cd7897745cf53a0485c923d9c577e006293ef43fff05a3b63df3', '2014-11-10 08:32:59'),
(21, 'János', 'Nagy', 'nagy.jani@gmail.com', 'e183a52fac90caae0b95385429ebf95cd876707e0d94762dc4c4cc6dd799a9166b033b91f455f11c6ef7b493c28a80d1275dc799e0b9b62d864a572bb25dc247', '2014-11-13 13:06:36'),
(22, 'Imre', 'Horváth', 'h.imre@gmail.com', 'e183a52fac90caae0b95385429ebf95cd876707e0d94762dc4c4cc6dd799a9166b033b91f455f11c6ef7b493c28a80d1275dc799e0b9b62d864a572bb25dc247', '2014-11-15 15:07:18'),
(24, 'János', 'Kiss', 'kissj@gmail.com', 'e9b9b0b275153d1300f7fe51fe12024166f4b9ec3921f5f4e592c3136c7852cf2b4012cd0033c4f4a73529b961b157025b476cacfdabfe43d714b34edf8510f2', '2014-11-18 07:53:51');

--
-- Eseményindítók `users`
--
DROP TRIGGER IF EXISTS `afterTriggerInsertProfiles`;
DELIMITER //
CREATE TRIGGER `afterTriggerInsertProfiles` AFTER INSERT ON `users`
 FOR EACH ROW BEGIN
 insert into profil(userId)
 select id from users where id = New.id;
END
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Nézet szerkezete `userlist`
--
DROP TABLE IF EXISTS `userlist`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `userlist` AS select `u`.`id` AS `id`,concat(`u`.`lastName`,' ',`u`.`firstName`) AS `fullName`,`u`.`email` AS `email`,`p`.`city` AS `city`,`p`.`address` AS `address`,`p`.`phone` AS `phone`,`p`.`birthday` AS `birthday`,`u`.`registered` AS `registered`,`p`.`privilidge` AS `privilidge` from (`users` `u` join `profil` `p` on((`p`.`userId` = `u`.`id`)));

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `answers`
--
ALTER TABLE `answers`
  ADD CONSTRAINT `fk_answers_questions1` FOREIGN KEY (`questionId`) REFERENCES `questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_answers_topics1` FOREIGN KEY (`topicId`) REFERENCES `topics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `profil`
--
ALTER TABLE `profil`
  ADD CONSTRAINT `fk_profil_users1` FOREIGN KEY (`userId`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `fk_questions_topics1` FOREIGN KEY (`topicId`) REFERENCES `topics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `results`
--
ALTER TABLE `results`
  ADD CONSTRAINT `fk_results_topics1` FOREIGN KEY (`topicId`) REFERENCES `topics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_results_users1` FOREIGN KEY (`userId`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `topics_user_conn`
--
ALTER TABLE `topics_user_conn`
  ADD CONSTRAINT `fk_topics_has_users_topics1` FOREIGN KEY (`topicsId`) REFERENCES `topics` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_topics_has_users_users1` FOREIGN KEY (`usersId`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Megkötések a táblához `useranswers`
--
ALTER TABLE `useranswers`
  ADD CONSTRAINT `fk_userAnswers_answers1` FOREIGN KEY (`answerId`) REFERENCES `answers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_userAnswers_questions1` FOREIGN KEY (`questionId`) REFERENCES `questions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
