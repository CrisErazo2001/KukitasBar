-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: greepo
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posicion`
--

DROP TABLE IF EXISTS `posicion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posicion` (
  `id_posicion` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `pos1` int DEFAULT NULL,
  `pos2` int DEFAULT NULL,
  `pos3` int DEFAULT NULL,
  `pos4` int DEFAULT NULL,
  `pos5` int DEFAULT NULL,
  `pos6` int DEFAULT NULL,
  `pos7` int DEFAULT NULL,
  `pos8` int DEFAULT NULL,
  `pos9` int DEFAULT NULL,
  `pos10` int DEFAULT NULL,
  `pos11` int DEFAULT NULL,
  `pos12` int DEFAULT NULL,
  `pos13` int DEFAULT NULL,
  `pos14` int DEFAULT NULL,
  `pos15` int DEFAULT NULL,
  `pos16` int DEFAULT NULL,
  `pos17` int DEFAULT NULL,
  `pos18` int DEFAULT NULL,
  `pos19` int DEFAULT NULL,
  `pos20` int DEFAULT NULL,
  `pos21` int DEFAULT NULL,
  `pos22` int DEFAULT NULL,
  `pos23` int DEFAULT NULL,
  `pos24` int DEFAULT NULL,
  `pos25` int DEFAULT NULL,
  `pos26` int DEFAULT NULL,
  `pos27` int DEFAULT NULL,
  `pos28` int DEFAULT NULL,
  PRIMARY KEY (`id_posicion`),
  UNIQUE KEY `id_posicion_UNIQUE` (`id_posicion`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posicion`
--

LOCK TABLES `posicion` WRITE;
/*!40000 ALTER TABLE `posicion` DISABLE KEYS */;
INSERT INTO `posicion` VALUES (7,'aaaaaa',0,3,7,11,0,0,0,3,0,0,3,7,11,3,11,0,0,0,0,0,0,11,0,0,0,0,0,0),(8,'equis',3,0,0,0,0,0,0,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0),(9,'equis2',3,0,0,0,0,0,0,11,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0),(10,'pppppp',3,3,0,0,0,0,0,3,0,0,0,0,0,0,11,0,0,0,0,0,0,11,0,0,0,0,0,0),(11,'ccccc',0,3,0,0,0,0,0,3,0,0,7,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `posicion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-05  6:08:33
