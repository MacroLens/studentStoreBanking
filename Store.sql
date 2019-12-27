-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Linux (x86_64)
--
-- Host: 192.168.1.163    Database: Store
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Audit`
--

DROP TABLE IF EXISTS `Audit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Audit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` bigint(20) DEFAULT NULL,
  `event_datetime` datetime NOT NULL,
  `event_type` text NOT NULL,
  `value_old` text COMMENT 'It needs to be text to catch all types.',
  `value_new` text COMMENT 'It needs to be text to catch all types.',
  PRIMARY KEY (`id`),
  KEY `student_id` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COMMENT='A log of all activity on Students';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Audit`
--

LOCK TABLES `Audit` WRITE;
/*!40000 ALTER TABLE `Audit` DISABLE KEYS */;
INSERT INTO `Audit` VALUES (15,1227830179,'2019-12-26 21:45:38','UPDATE_BALANCE','292.25','312.25'),(20,1227830179,'2019-12-26 21:51:02','UPDATE_BALANCE','312.25','332.25'),(21,1227830179,'2019-12-26 21:56:39','UPDATE_BALANCE','332.25','352.25'),(22,1227830179,'2019-12-26 21:58:11','UPDATE_BALANCE','352.25','362.25'),(23,1227830179,'2019-12-26 21:58:15','UPDATE_BALANCE','362.25','372.25'),(24,1227830179,'2019-12-26 22:01:16','UPDATE_BALANCE','372.25','342.25'),(25,1227830179,'2019-12-26 22:01:32','UPDATE_BALANCE','342.25','312.25'),(26,1227830180,'2019-12-26 22:04:50','INSERT',NULL,'1227830180'),(27,1227830180,'2019-12-26 22:07:14','DELETE','1227830180',NULL),(28,4098948934,'2019-12-27 00:28:37','INSERT',NULL,'4098948934'),(29,4098948934,'2019-12-27 00:29:40','DELETE','4098948934',NULL),(30,4098948934,'2019-12-27 00:30:47','INSERT',NULL,'4098948934'),(31,4098948934,'2019-12-27 00:31:17','DELETE','4098948934',NULL),(32,4098948934,'2019-12-27 00:50:02','INSERT',NULL,'4098948934'),(33,4098948934,'2019-12-27 00:55:30','UPDATE_BALANCE','10.25','0.25'),(34,4098948934,'2019-12-27 00:55:37','UPDATE_BALANCE','0.25','0'),(35,4098948934,'2019-12-27 01:04:44','UPDATE_BALANCE','0','2'),(36,4098948934,'2019-12-27 01:09:55','UPDATE_BALANCE','2','7'),(37,4026888870,'2019-12-27 01:31:06','INSERT',NULL,'4026888870'),(38,1227830179,'2019-12-27 01:37:08','UPDATE_BALANCE','312.25','292.25');
/*!40000 ALTER TABLE `Audit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Students`
--

DROP TABLE IF EXISTS `Students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Students` (
  `id` bigint(20) NOT NULL,
  `name` text,
  `balance` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `Students_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Students`
--

LOCK TABLES `Students` WRITE;
/*!40000 ALTER TABLE `Students` DISABLE KEYS */;
INSERT INTO `Students` VALUES (1227830179,'Dylan Le',292.25),(4026888870,'Anh',12.5),(4098948934,'Not Dylan',7);
/*!40000 ALTER TABLE `Students` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`192.168.1.172`*/ /*!50003 trigger insertStudents
    before INSERT
    on Students
    for each row
    insert into Store.Audit
    (student_id, event_datetime, event_type, value_old, value_new) values  
    (NEW.id, now(), "INSERT", NULL, NEW.id) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`192.168.1.172`*/ /*!50003 trigger updateStudents
    before UPDATE
    on Students
    for each row
    BEGIN 
    if OLD.id != NEW.id then
        insert into Store.Audit
        (student_id, event_datetime, event_type, value_old, value_new) values
        (OLD.id, now(), "UPDATE_ID", OLD.id, NEW.id);
    end if;
    if OLD.balance != NEW.balance then
        insert into Store.Audit
        (student_id, event_datetime, event_type, value_old, value_new) values
        (OLD.id, now(), "UPDATE_BALANCE", OLD.balance, NEW.balance);
    end if;
    if OLD.name != NEW.name then 
        insert into Store.Audit
        (student_id, event_datetime, event_type, value_old, value_new) values
        (OLD.id, now(), "UPDATE_NAME", OLD.name, NEW.name);
    end if;
    END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`admin`@`192.168.1.172`*/ /*!50003 trigger deleteStudents
    before delete
    on Students
    for each row
    BEGIN
        insert into Store.Audit
        (student_id, event_datetime, event_type, value_old, value_new) values
        (OLD.id, now(), "DELETE", OLD.id, NULL);
    END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping routines for database 'Store'
--
/*!50003 DROP PROCEDURE IF EXISTS `AddAccount` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`192.168.1.172` PROCEDURE `AddAccount`(IN s_id bigint, IN s_name text, IN bal float, OUT done tinyint(1))
BEGIN
    declare count int;
    select count(*) into count from Students where id = s_id;
    if count = 0 then
        insert into Store.Students
        (id, name, balance) values (s_id, s_name, bal);
        set done = TRUE;
    else 
        set done = FALSE;
    end if; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ChangeBalance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`192.168.1.172` PROCEDURE `ChangeBalance`(IN s_id bigint, IN diff float, OUT done tinyint(1))
BEGIN
    declare newbal float;
    select balance + diff into newbal from Students where id = s_id;
    if newbal < 0 then
        set done = FALSE;
    else
        update Students
            set balance = newbal
            where id = s_id;
        set done = TRUE;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetBalance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`192.168.1.172` PROCEDURE `GetBalance`(IN s_id bigint, out bal float, out done bool)
BEGIN
    declare count int;
    select count(balance) into count from Students where id = s_id;
    if count = 0 then
        set done = FALSE;
    else
        select balance into bal from Students where id = s_id;
        set done = TRUE;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetStudentName` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'IGNORE_SPACE,STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`admin`@`192.168.1.172` PROCEDURE `GetStudentName`(IN s_id bigint, OUT s_name text, OUT done tinyint(1))
BEGIN
    declare count int;
    select count(name) into count from Students where id = s_id;
    if count = 0 then
        set done = FALSE;
    else
        select name into s_name from Students where id = s_id;
        set done = TRUE;
    end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-26 19:49:14
