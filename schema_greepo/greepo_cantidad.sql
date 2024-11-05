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
-- Table structure for table `cantidad`
--

DROP TABLE IF EXISTS `cantidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cantidad` (
  `id_cantidad` int NOT NULL,
  `cant1` int DEFAULT NULL,
  `cant2` int DEFAULT NULL,
  `cant3` int DEFAULT NULL,
  `cant4` int DEFAULT NULL,
  `cant5` int DEFAULT NULL,
  `cant6` int DEFAULT NULL,
  `cant7` int DEFAULT NULL,
  `cant8` int DEFAULT NULL,
  `cant9` int DEFAULT NULL,
  `cant10` int DEFAULT NULL,
  `cant11` int DEFAULT NULL,
  `cant12` int DEFAULT NULL,
  `cant13` int DEFAULT NULL,
  `cant14` int DEFAULT NULL,
  `cant15` int DEFAULT NULL,
  `cant16` int DEFAULT NULL,
  `cant17` int DEFAULT NULL,
  `cant18` int DEFAULT NULL,
  `cant19` int DEFAULT NULL,
  `cant20` int DEFAULT NULL,
  `cant21` int DEFAULT NULL,
  `cant22` int DEFAULT NULL,
  `cant23` int DEFAULT NULL,
  `cant24` int DEFAULT NULL,
  `cant25` int DEFAULT NULL,
  `cant26` int DEFAULT NULL,
  `cant27` int DEFAULT NULL,
  `cant28` int DEFAULT NULL,
  PRIMARY KEY (`id_cantidad`),
  UNIQUE KEY `id_cantidad_UNIQUE` (`id_cantidad`) /*!80000 INVISIBLE */,
  CONSTRAINT `id_cantidad` FOREIGN KEY (`id_cantidad`) REFERENCES `posicion` (`id_posicion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cantidad`
--

LOCK TABLES `cantidad` WRITE;
/*!40000 ALTER TABLE `cantidad` DISABLE KEYS */;
INSERT INTO `cantidad` VALUES (7,0,450,1200,300,0,0,0,750,0,0,750,1500,750,750,750,0,0,0,0,0,0,750,0,0,0,0,0,0),(8,750,0,0,0,0,0,0,0,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0),(9,750,0,0,0,0,0,0,750,0,0,0,0,0,0,750,0,0,0,0,0,0,0,0,0,0,0,0,0),(10,750,750,0,0,0,0,0,750,0,0,0,0,0,0,750,0,0,0,0,0,0,750,0,0,0,0,0,0),(11,0,750,0,0,0,0,0,750,0,0,1500,0,0,1500,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
/*!40000 ALTER TABLE `cantidad` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-05  6:08:32
