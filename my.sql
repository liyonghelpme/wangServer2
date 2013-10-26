-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: mywangguo
-- ------------------------------------------------------
-- Server version	5.5.28-0ubuntu0.12.04.3-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(200) COLLATE utf8_bin NOT NULL,
  `name` char(255) COLLATE utf8_bin NOT NULL DEFAULT '',
  `crystal` int(11) NOT NULL DEFAULT '0',
  `silver` int(11) NOT NULL DEFAULT '0',
  `gold` int(11) NOT NULL DEFAULT '0',
  `exp` int(11) NOT NULL DEFAULT '0',
  `level` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (5,'liyong','',207,575,0,255,0),(6,'wangxiaoming','',4,30,0,7,0),(7,'liyong1','',0,0,0,0,0),(8,'liyong2','',0,0,0,0,0),(9,'liyong3-del','liyong',9211,1574,100,152,0),(10,'liyong3','liyong2',23,1085,100,509,0),(11,'860755013247455','liyonghelpme',500,1000,100,0,0),(12,'','gdf',350,1005,100,43,0);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserBuilding`
--

DROP TABLE IF EXISTS `UserBuilding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserBuilding` (
  `uid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `kind` int(11) NOT NULL,
  `px` int(11) NOT NULL,
  `py` int(11) NOT NULL,
  `state` int(11) NOT NULL DEFAULT '1',
  `objectTime` int(11) NOT NULL DEFAULT '0',
  `objectId` int(11) NOT NULL DEFAULT '0',
  `objectList` char(255) COLLATE utf8_bin NOT NULL DEFAULT '[]',
  PRIMARY KEY (`uid`,`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserBuilding`
--

LOCK TABLES `UserBuilding` WRITE;
/*!40000 ALTER TABLE `UserBuilding` DISABLE KEYS */;
INSERT INTO `UserBuilding` VALUES (3,0,200,1000,350,1,0,0,'[]'),(3,1,202,1200,300,1,0,0,'[]'),(3,2,0,2000,300,1,0,0,'[]'),(3,3,300,1500,300,1,0,0,'[]'),(4,0,200,1500,300,1,1380501007,0,'[]'),(4,1,202,1200,300,1,1380501007,0,'[]'),(4,2,0,1700,250,1,1380501007,0,'[]'),(4,3,300,1300,250,1,1380501007,0,'[]'),(5,0,200,1568,224,1,1380504249,0,'[]'),(5,1,202,1344,368,1,1380504249,0,'[]'),(5,2,0,1472,336,1,1381875791,11,'[]'),(5,3,300,1696,384,1,1381708842,0,'[]'),(5,4,0,2464,352,1,1381532877,13,'[]'),(5,5,0,2720,416,1,1381532883,11,'[]'),(5,6,0,2368,432,1,1381532611,13,'[]'),(5,7,300,2784,256,1,1381637761,0,'[]'),(5,8,224,2272,224,1,1381704369,0,'[]'),(6,0,200,1500,300,1,1381878645,0,'[]'),(6,1,202,1200,300,1,1381878645,0,'[]'),(6,2,0,1700,250,1,1381965512,11,'[]'),(6,3,300,1300,100,1,1381961722,0,'[]'),(7,0,200,1500,300,1,1382052661,0,'[]'),(7,1,202,1200,300,1,1382052661,0,'[]'),(7,2,0,1700,250,1,1382052661,0,'[]'),(7,3,300,1300,100,1,1382052661,0,'[]'),(8,0,200,1500,300,1,1382052739,0,'[]'),(8,1,202,1200,300,1,1382052739,0,'[]'),(8,2,0,1700,250,1,1382052739,0,'[]'),(8,3,300,1300,100,1,1382052739,0,'[]'),(8,4,224,1550,200,1,1382052739,0,'[]'),(9,0,200,1500,300,1,1382052814,0,'[]'),(9,1,202,1200,300,1,1382052814,0,'[]'),(9,2,0,1824,192,1,1382052814,0,'[]'),(9,3,300,1300,100,1,1382314865,0,'[]'),(9,4,224,1550,200,1,0,0,'[3, 3, 3]'),(9,5,0,1504,128,1,1382250607,0,'[]'),(9,6,224,2560,432,1,1382253858,0,'[]'),(9,7,0,2368,400,1,1382314531,0,'[]'),(10,0,200,1500,300,1,1382314913,0,'[]'),(10,1,202,1200,300,1,1382314913,0,'[]'),(10,2,0,1700,250,1,1382484574,11,'[]'),(10,3,300,1300,100,1,1382484573,0,'[]'),(10,4,224,1550,200,1,1382484350,0,'[]'),(11,0,200,1500,300,1,1382671645,0,'[]'),(11,1,202,1200,300,1,1382671645,0,'[]'),(11,2,0,1700,250,1,1382671645,0,'[]'),(11,3,300,1300,100,1,1382671645,0,'[]'),(11,4,224,1550,200,1,1382671645,0,'[]'),(12,0,200,1632,192,1,1382681201,0,'[]'),(12,1,202,1200,300,1,1382681201,0,'[]'),(12,2,0,1568,128,1,1382781032,0,'[]'),(12,3,300,1472,272,1,1382781051,0,'[]'),(12,4,224,1472,176,1,1382780642,0,'[]'),(12,5,0,2432,464,1,1382780420,0,'[]'),(12,6,0,2560,368,1,1382780713,0,'[]'),(12,7,0,2624,400,1,1382780717,0,'[]');
/*!40000 ALTER TABLE `UserBuilding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserSoldier`
--

DROP TABLE IF EXISTS `UserSoldier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserSoldier` (
  `uid` int(11) NOT NULL,
  `kind` int(11) NOT NULL,
  `num` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`,`kind`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserSoldier`
--

LOCK TABLES `UserSoldier` WRITE;
/*!40000 ALTER TABLE `UserSoldier` DISABLE KEYS */;
INSERT INTO `UserSoldier` VALUES (5,3,1),(5,413,1),(9,3,0),(9,23,0),(10,3,0),(12,3,-1);
/*!40000 ALTER TABLE `UserSoldier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strings`
--

DROP TABLE IF EXISTS `strings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `strings` (
  `key` varchar(100) COLLATE utf8_bin NOT NULL,
  `cn` varchar(500) COLLATE utf8_bin NOT NULL,
  `eng` varchar(500) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strings`
--

LOCK TABLES `strings` WRITE;
/*!40000 ALTER TABLE `strings` DISABLE KEYS */;
INSERT INTO `strings` VALUES ('resLack','资源不足','Resource not enough!');
/*!40000 ALTER TABLE `strings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-10-26 18:22:53
