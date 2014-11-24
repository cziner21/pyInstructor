-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Hoszt: 127.0.0.1
-- Létrehozás ideje: 2014. Nov 23. 17:21
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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=318 ;

--
-- A tábla adatainak kiíratása `answers`
--

INSERT INTO `answers` (`id`, `answerText`, `questionId`, `isItCorrect`, `topicId`) VALUES
(164, 'True', 61, 1, 48),
(165, 'False', 61, NULL, 48),
(166, 'A property can simultaneously be read only or write only', 62, NULL, 48),
(167, 'A property can be either read only or write only', 62, 1, 48),
(168, 'A write only property will have only get accessor', 62, NULL, 48),
(169, 'A write only property will always return a value', 62, NULL, 48),
(170, 'Declare rollNo property with both get and set accessors', 63, 0, 48),
(171, 'Declare rollNo property with only set accessor', 63, 0, 48),
(172, 'Declare rollNo property with get, set and normal accessors', 63, 0, 48),
(173, 'Declare rollNo property with only get accessor', 63, 1, 48),
(174, 'None of the above', 63, 0, 48),
(175, 'Sample m = new Sample(); m.Length = 10;', 64, NULL, 48),
(176, '\nSample m = new Sample(); m.Length = m.Length + 20', 64, NULL, 48),
(177, 'Sample m = new Sample(); int l; l = m.Length;', 64, 1, 48),
(178, 'Sample.Length = 20;', 64, NULL, 48),
(179, 'Console.WriteLine(Sample.Length);', 64, NULL, 48),
(180, 'new', 65, 1, 48),
(181, 'base', 65, 0, 48),
(182, 'overloads', 65, 0, 48),
(183, 'override', 65, 0, 48),
(184, 'overridable', 65, 0, 48),
(185, 'inherits', 66, NULL, 48),
(186, 'extends', 66, NULL, 48),
(187, 'extends', 66, NULL, 48),
(188, 'not inheritable', 66, NULL, 48),
(189, 'sealed', 66, 1, 48),
(190, 'When used as a modifier, the new keyword explicitly hides a member inherited from a base class', 67, 1, 48),
(191, 'Operator overloading works in different ways for structures and classes', 67, NULL, 48),
(192, 'It is not necessary that all operator overloads are static methods of the class', 67, NULL, 48),
(193, 'The cast operator can be overloaded', 67, NULL, 48),
(194, 'Char', 68, NULL, 48),
(195, 'Long', 68, 1, 48),
(196, 'Short', 68, NULL, 48),
(197, 'Byte', 68, NULL, 48),
(198, 'Integer', 68, NULL, 48),
(199, 'Integer ', 69, 1, 48),
(200, 'Array', 69, NULL, 48),
(201, 'Single ', 69, 1, 48),
(202, 'String ', 69, NULL, 48),
(203, 'Long ', 69, 1, 48),
(204, 'An argument passed to a ref parameter need not be initialized first.', 70, NULL, 48),
(205, 'Variables passed as out arguments need to be initialized prior to being passed. ', 70, NULL, 48),
(206, 'Argument that uses params keyword must be the last argument of variable argument list of a method.', 70, 1, 48),
(207, 'Pass by reference eliminates the overhead of copying large data items', 70, 1, 48),
(208, 'To use a ref parameter only the calling method must explicitly use the ref keyword', 70, NULL, 48),
(209, 'True', 71, 1, 48),
(210, 'False', 71, 0, 48),
(211, 'Use the existing functionality of base class. ', 72, 1, 48),
(212, 'Overrride the existing functionality of base class', 72, 1, 48),
(213, 'Implement new functionality in the derived class. ', 72, 1, 48),
(214, 'Implement polymorphic behaviour.', 72, NULL, 48),
(215, 'Implement containership.', 72, NULL, 48),
(216, 'Sample s = new Sample()', 73, 1, 48),
(217, 'Sample s;', 73, NULL, 48),
(218, 'Sample s; s = new Sample();', 73, 1, 48),
(219, 's = new Sample()', 73, NULL, 48),
(220, 'Data members ofa class are by default public', 74, NULL, 48),
(221, 'Data members of a class are by default private. ', 74, 1, 48),
(222, 'Member functions of a class are by default public. ', 74, NULL, 48),
(223, 'A private function of a class can access a public function within the same class. ', 74, 1, 48),
(224, 'Member function of a class are by default private. ', 74, 1, 48),
(225, 'It will create an object called sample.', 75, 0, 48),
(226, 'It will create a nameless object of the type sample', 75, 1, 48),
(227, 'It will create an object of the type sample on the stack', 75, 0, 48),
(228, 'It will create a reference c on the stack and an object of the type sample on the heap', 75, 1, 48),
(229, 'It will create an object of the type sample either on the heap or on the stack depending on the size of the object.', 75, 0, 48),
(230, 'Class is a value type', 76, NULL, 48),
(231, 'Since objects are typically big in size, they are created on the stack', 76, NULL, 48),
(232, ' 	Objects of smaller size are created on the heap', 76, NULL, 48),
(233, 'Smaller objects that get created on the stack can be given names.', 76, NULL, 48),
(234, 'Objects are always nameless.', 76, 1, 48),
(235, 'Array elements can be of integer type only', 77, NULL, 48),
(236, 'The rank of an Array is the total number of elements it can contain.', 77, NULL, 48),
(237, 'The length of an Array is the number of dimensions in the Array', 77, NULL, 48),
(238, 'The default value of numeric array elements is zero', 77, 1, 48),
(239, 'The Array elements are guaranteed to be sorted', 77, NULL, 48),
(240, 'Arrays can be rectangular or jagged', 78, 1, 48),
(241, 'Rectangular arrays have similar rows stored in adjacent memory locations. ', 78, 1, 48),
(242, 'Jagged arrays do not have an access to the methods of System.Array Class.', 78, NULL, 48),
(243, 'Rectangular arrays do not have an access to the methods of System.Array Class.', 78, NULL, 48),
(244, 'Jagged arrays have dissimilar rows stored in non-adjacent memory locations.', 78, 1, 48),
(245, 'By default the first enumerator has the value equal to the number of elements present in the list. ', 79, 0, 48),
(246, 'The value of each successive enumerator is decreased by 1. ', 79, 0, 48),
(247, 'An enumerator contains white space in its name. ', 79, 0, 48),
(248, 'A variable cannot be assigned to an enum element', 79, 1, 48),
(249, 'Values of enum elements cannot be populated from a database. ', 79, 1, 48),
(250, 'If an exception occurs then the program terminates abruptly without getting any chance to recover from the exception.', 80, NULL, 48),
(251, 'No matter whether an exception occurs or not, the statements in the finally clause (if present) will get executed. ', 80, 1, 48),
(252, 'A program can contain multiple finally clauses. ', 80, NULL, 48),
(253, 'A finally clause is written outside the try block. ', 80, NULL, 48),
(254, 'finally clause is used to perform clean up operations like closing the network/database connections. ', 80, 1, 48),
(278, 'memory.h', 87, NULL, 52),
(279, 'stdlib.h', 87, 1, 52),
(280, 'string.h', 87, NULL, 52),
(281, 'dos.h', 87, NULL, 52),
(282, 'dealloc();', 88, NULL, 52),
(283, 'malloc(variable_name, 0)', 88, NULL, 52),
(284, 'free();', 88, 1, 52),
(285, 'memalloc(variable_name, 0)', 88, NULL, 52),
(286, 'malloc() and memalloc()', 89, NULL, 52),
(287, 'alloc() and memalloc()', 89, NULL, 52),
(288, 'malloc() and calloc()', 89, 1, 52),
(289, 'memalloc() and faralloc()', 89, NULL, 52),
(290, 'Representation of NULL pointer', 90, 1, 52),
(291, 'Representation of void pointer', 90, NULL, 52),
(292, 'Error', 90, NULL, 52),
(293, 'None of above', 90, NULL, 52),
(294, '.', 91, 0, 52),
(295, '&', 91, 0, 52),
(296, '*', 91, 0, 52),
(297, '->', 91, 1, 52),
(298, 'remove(var-name);', 92, NULL, 52),
(299, 'delete(var-name);', 92, 1, 52),
(300, 'free(var-name);', 92, NULL, 52),
(301, 'dalloc(var-name);', 92, NULL, 52),
(302, 'switch', 93, NULL, 52),
(303, 'goto', 93, NULL, 52),
(304, 'go back', 93, NULL, 52),
(305, 'return', 93, 1, 52),
(306, 'strinit()', 94, NULL, 52),
(307, 'strset()', 94, NULL, 52),
(308, 'strnset()', 94, 1, 52),
(309, 'strcset()', 94, NULL, 52),
(310, 'printf("\\n");', 95, NULL, 52),
(311, 'echo "\\\\n";', 95, NULL, 52),
(312, 'printf(''\\n'');', 95, NULL, 52),
(313, 'printf("\\\\n");', 95, 1, 52),
(314, '/ + * -', 96, NULL, 52),
(315, '* - / +', 96, NULL, 52),
(316, '+ - / *', 96, NULL, 52),
(317, '/ * + -', 96, 1, 52);

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- A tábla adatainak kiíratása `profil`
--

INSERT INTO `profil` (`id`, `profilPictureURL`, `city`, `address`, `phone`, `userId`, `birthday`, `privilidge`) VALUES
(1, NULL, 'Budapest', 'Hungária körút 81. 3. emelet 14/A', '+3611234567', 25, '1990-04-21', 0),
(2, NULL, 'Eger', 'Leányka út 12.', '+36201213456', 26, '1978-12-06', 1),
(3, NULL, '', '', '', 27, NULL, 1);

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=97 ;

--
-- A tábla adatainak kiíratása `questions`
--

INSERT INTO `questions` (`id`, `questionText`, `topicId`) VALUES
(61, 'A property can be declared inside a class, struct, Interface', 48),
(62, 'Which of the following statements is correct about properties used in C#.NET', 48),
(63, 'A Student class has a property called RollNo and myStudent is a reference to a Student object and we want the statement myStudent.RollNo = 28 to fail. Which of the following options will ensure this functionality\n', 48),
(64, 'If Sample class has a Length property with get accessor then which of the following statements will work correctly?', 48),
(65, 'Which of the following keyword is used to change the data and behavior of a base class by replacing a member of a base class with a new derived member', 48),
(66, 'A derived class can stop virtual inheritance by declaring an override a', 48),
(67, 'Which of the following statements is correct?', 48),
(68, 'Which of the following is an 8-byte Integer', 48),
(69, 'Which of the following are value types?', 48),
(70, 'Which of the following statements are correct?', 48),
(71, 'A function returns a value, whereas a subroutine cannot return a value\n', 48),
(72, 'Which of the following can be facilitated by the Inheritance mechanism?', 48),
(73, 'Which of the following is the correct way to create an object of the class Sample?', 48),
(74, 'Which of the following statements are correct?', 48),
(75, 'Which of the following statements are correct about the C#.NET code snippet given below?\nsample c; c = new sample();', 48),
(76, 'Which of the following statements is correct about classes and objects in C#.NET', 48),
(77, 'Which one of the following statements is correct?', 48),
(78, 'Which of the following statements are correct about arrays used in C#.NET? ', 48),
(79, 'Which of the following statements are correct about an enum used inC#.NET?', 48),
(80, 'Which of the following statements are correct about exception handling in C#.NET? ', 48),
(87, 'Which header file should be included to use functions like malloc() and calloc()\n', 52),
(88, 'What function should be used to free the memory allocated by calloc() ?', 52),
(89, 'Specify the 2 library functions to dynamically allocate memory?', 52),
(90, 'What is (void*)0?', 52),
(91, 'If a variable is a pointer to a structure, then which of the following operator is used to access data members of the structure through the pointer variable?', 52),
(92, 'How will you free the allocated memory ?', 52),
(93, 'The keyword used to transfer control from a function back to the calling function is\n', 52),
(94, 'Which of the following function sets first n characters of a string to a given character?', 52),
(95, 'How will you print \\n on the screen?', 52),
(96, 'Which of the following correctly shows the hierarchy of arithmetic operations in C?', 52);

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=199 ;

--
-- A tábla adatainak kiíratása `results`
--

INSERT INTO `results` (`id`, `result`, `userId`, `topicId`, `examDate`) VALUES
(191, 20, 25, 48, '2014-11-23 15:10:28'),
(192, 17, 25, 48, '2014-11-23 15:12:41'),
(193, 17, 25, 48, '2014-11-23 15:12:42'),
(194, 15, 26, 48, '2014-11-23 15:25:52'),
(195, 15, 26, 48, '2014-11-23 15:25:52'),
(196, 19, 27, 48, '2014-11-23 15:30:21'),
(197, 7, 25, 52, '2014-11-23 17:19:17'),
(198, 7, 25, 52, '2014-11-23 17:19:17');

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=53 ;

--
-- A tábla adatainak kiíratása `topics`
--

INSERT INTO `topics` (`id`, `name`) VALUES
(52, 'C'),
(48, 'C#');

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
(48, 25),
(48, 25),
(48, 25),
(48, 26),
(48, 26),
(48, 27),
(52, 25),
(52, 25);

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1703 ;

--
-- A tábla adatainak kiíratása `useranswers`
--

INSERT INTO `useranswers` (`id`, `questionId`, `answerId`) VALUES
(1470, 61, 164),
(1471, 62, 167),
(1472, 63, 173),
(1473, 64, 177),
(1474, 65, 180),
(1475, 66, 189),
(1476, 67, 190),
(1477, 68, 195),
(1478, 69, 199),
(1479, 69, 201),
(1480, 69, 203),
(1481, 70, 206),
(1482, 70, 207),
(1483, 71, 209),
(1484, 72, 211),
(1485, 72, 212),
(1486, 72, 213),
(1487, 73, 216),
(1488, 73, 218),
(1489, 74, 221),
(1490, 74, 223),
(1491, 74, 224),
(1492, 75, 226),
(1493, 75, 228),
(1494, 76, 234),
(1495, 77, 238),
(1496, 78, 240),
(1497, 78, 241),
(1498, 78, 244),
(1499, 79, 248),
(1500, 79, 249),
(1501, 80, 251),
(1502, 80, 254),
(1503, 61, 164),
(1504, 62, 167),
(1505, 63, 173),
(1506, 64, 177),
(1507, 65, 180),
(1508, 65, 181),
(1509, 66, 189),
(1510, 67, 190),
(1511, 68, 195),
(1512, 69, 199),
(1513, 69, 202),
(1514, 69, 203),
(1515, 70, 206),
(1516, 70, 207),
(1517, 71, 209),
(1518, 72, 211),
(1519, 72, 212),
(1520, 72, 213),
(1521, 73, 216),
(1522, 73, 218),
(1523, 74, 220),
(1524, 74, 221),
(1525, 75, 226),
(1526, 75, 228),
(1527, 76, 234),
(1528, 77, 238),
(1529, 78, 240),
(1530, 78, 241),
(1531, 78, 244),
(1532, 79, 248),
(1533, 79, 249),
(1534, 80, 251),
(1535, 80, 254),
(1536, 61, 164),
(1537, 62, 167),
(1538, 63, 173),
(1539, 64, 177),
(1540, 65, 180),
(1541, 65, 181),
(1542, 66, 189),
(1543, 67, 190),
(1544, 68, 195),
(1545, 69, 199),
(1546, 69, 202),
(1547, 69, 203),
(1548, 70, 206),
(1549, 70, 207),
(1550, 71, 209),
(1551, 72, 211),
(1552, 72, 212),
(1553, 72, 213),
(1554, 73, 216),
(1555, 73, 218),
(1556, 74, 220),
(1557, 74, 221),
(1558, 75, 226),
(1559, 75, 228),
(1560, 76, 234),
(1561, 77, 238),
(1562, 78, 240),
(1563, 78, 241),
(1564, 78, 244),
(1565, 79, 248),
(1566, 79, 249),
(1567, 80, 251),
(1568, 80, 254),
(1569, 61, 164),
(1570, 62, 167),
(1571, 63, 173),
(1572, 64, 177),
(1573, 65, 180),
(1574, 66, 189),
(1575, 67, 190),
(1576, 68, 195),
(1577, 69, 199),
(1578, 69, 201),
(1579, 69, 203),
(1580, 70, 206),
(1581, 70, 207),
(1582, 71, 209),
(1583, 72, 211),
(1584, 72, 212),
(1585, 72, 213),
(1586, 73, 216),
(1587, 73, 218),
(1588, 74, 221),
(1589, 74, 223),
(1590, 74, 224),
(1591, 75, 226),
(1592, 75, 227),
(1593, 75, 228),
(1594, 76, 232),
(1595, 76, 233),
(1596, 76, 234),
(1597, 77, 235),
(1598, 78, 240),
(1599, 78, 241),
(1600, 78, 242),
(1601, 78, 243),
(1602, 79, 245),
(1603, 79, 248),
(1604, 79, 249),
(1605, 80, 251),
(1606, 80, 254),
(1607, 61, 164),
(1608, 62, 167),
(1609, 63, 173),
(1610, 64, 177),
(1611, 65, 180),
(1612, 66, 189),
(1613, 67, 190),
(1614, 68, 195),
(1615, 69, 199),
(1616, 69, 201),
(1617, 69, 203),
(1618, 70, 206),
(1619, 70, 207),
(1620, 71, 209),
(1621, 72, 211),
(1622, 72, 212),
(1623, 72, 213),
(1624, 73, 216),
(1625, 73, 218),
(1626, 74, 221),
(1627, 74, 223),
(1628, 74, 224),
(1629, 75, 226),
(1630, 75, 227),
(1631, 75, 228),
(1632, 76, 232),
(1633, 76, 233),
(1634, 76, 234),
(1635, 77, 235),
(1636, 78, 240),
(1637, 78, 241),
(1638, 78, 242),
(1639, 78, 243),
(1640, 79, 245),
(1641, 79, 248),
(1642, 79, 249),
(1643, 80, 251),
(1644, 80, 254),
(1645, 61, 164),
(1646, 62, 167),
(1647, 63, 173),
(1648, 64, 177),
(1649, 65, 180),
(1650, 66, 189),
(1651, 67, 190),
(1652, 68, 195),
(1653, 69, 199),
(1654, 69, 201),
(1655, 69, 203),
(1656, 70, 206),
(1657, 70, 207),
(1658, 71, 209),
(1659, 72, 211),
(1660, 72, 212),
(1661, 72, 213),
(1662, 73, 216),
(1663, 73, 218),
(1664, 74, 221),
(1665, 74, 223),
(1666, 74, 224),
(1667, 75, 226),
(1668, 75, 228),
(1669, 76, 234),
(1670, 77, 238),
(1671, 78, 240),
(1672, 78, 241),
(1673, 78, 242),
(1674, 78, 243),
(1675, 79, 248),
(1676, 79, 249),
(1677, 80, 251),
(1678, 80, 254),
(1679, 87, 278),
(1680, 87, 279),
(1681, 88, 284),
(1682, 89, 286),
(1683, 89, 288),
(1684, 90, 291),
(1685, 91, 297),
(1686, 92, 299),
(1687, 93, 305),
(1688, 94, 308),
(1689, 95, 313),
(1690, 96, 317),
(1691, 87, 278),
(1692, 87, 279),
(1693, 88, 284),
(1694, 89, 286),
(1695, 89, 288),
(1696, 90, 291),
(1697, 91, 297),
(1698, 92, 299),
(1699, 93, 305),
(1700, 94, 308),
(1701, 95, 313),
(1702, 96, 317);

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
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=28 ;

--
-- A tábla adatainak kiíratása `users`
--

INSERT INTO `users` (`id`, `firstName`, `lastName`, `email`, `password`, `registered`) VALUES
(25, 'Admin', 'Demo', 'admin@admin.hu', '3096c5e4e548c713662da783a6c766da03a92dfd088e15ab03dc8b641be2af6902f4687dc58ce89042b01d47c470ee7718ab1a326ef8648118929315b6489f3b', '2014-11-23 11:16:21'),
(26, 'User', 'Demo', 'user@user.hu', '3096c5e4e548c713662da783a6c766da03a92dfd088e15ab03dc8b641be2af6902f4687dc58ce89042b01d47c470ee7718ab1a326ef8648118929315b6489f3b', '2014-11-23 11:16:58'),
(27, 'Ádám', 'Cziner', 'cziner.adam@gmail.com', 'e9b9b0b275153d1300f7fe51fe12024166f4b9ec3921f5f4e592c3136c7852cf2b4012cd0033c4f4a73529b961b157025b476cacfdabfe43d714b34edf8510f2', '2014-11-23 15:27:23');

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
