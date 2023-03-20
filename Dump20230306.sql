CREATE DATABASE  IF NOT EXISTS `bdproyecto` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bdproyecto`;
-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: bdproyecto
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `actividades`
--

DROP TABLE IF EXISTS `actividades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actividades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `actividad` varchar(55) DEFAULT NULL,
  `nro` int DEFAULT NULL,
  `description` text,
  `nivel` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actividades`
--

LOCK TABLES `actividades` WRITE;
/*!40000 ALTER TABLE `actividades` DISABLE KEYS */;
INSERT INTO `actividades` VALUES (1,'Peso',1,'se debe calcular masa',1,'2023-03-05 10:48:47','2023-03-05 10:48:47'),(2,'Peso 2',1,'se debe calcular masa avanzada',2,'2023-03-05 11:15:25','2023-03-06 14:42:48'),(3,'Masa',2,'se debe calcular masa',1,'2023-03-05 11:15:49','2023-03-05 11:15:49'),(4,'Rotación',5,'se debe calcular como rotan los objetos',2,'2023-03-05 11:16:46','2023-03-05 11:16:46');
/*!40000 ALTER TABLE `actividades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registros`
--

DROP TABLE IF EXISTS `registros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registros` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `puntaje` int DEFAULT NULL,
  `duracion` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `usuario_id` int NOT NULL,
  `actividad_id` int NOT NULL,
  `usuario_id_actividad` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_registros_usuarios_idx` (`usuario_id`),
  KEY `fk_registros_actividades1_idx` (`actividad_id`),
  KEY `fk_registros_usuarios1_idx` (`usuario_id_actividad`),
  CONSTRAINT `fk_registros_actividades1` FOREIGN KEY (`actividad_id`) REFERENCES `actividades` (`id`),
  CONSTRAINT `fk_registros_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `fk_registros_usuarios1` FOREIGN KEY (`usuario_id_actividad`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registros`
--

LOCK TABLES `registros` WRITE;
/*!40000 ALTER TABLE `registros` DISABLE KEYS */;
INSERT INTO `registros` VALUES (1,'2023-03-06','12:00:00',10,1,'2023-03-06 17:00:53','2023-03-06 17:00:53',1,1,1),(2,'2023-03-06','14:00:00',34,2,'2023-03-06 17:01:42','2023-03-06 17:01:42',2,2,2);
/*!40000 ALTER TABLE `registros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(55) DEFAULT NULL,
  `last_name` varchar(55) DEFAULT NULL,
  `email` varchar(155) DEFAULT NULL,
  `password` varchar(500) DEFAULT NULL,
  `level` varchar(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'BENITO','ALMADA','bnito86@hotmail.com','$2b$12$DK2jlM9emhQ0e9y4NXtItuyXJRyX1/uYJIk1xUSJ5ZTOvC8HaTzEG','1',NULL,NULL),(2,'Roberto','Perez','examen1@correo.com','$2b$12$stiOdgrOnJQGBALva0DYz.rUbOKuALTSh1ZrP08jWmEDNsUc8GCAi','2',NULL,NULL),(3,'Agustín B','Almada Barrios','bnito86@gmail.com','$2b$12$ku4gv4jQqwjyrTw0t4mPKO6Zf4GXkHGJc0PhLZHrU7Kghc6v.3DuK',NULL,NULL,NULL),(4,'Alumno1','Alumno1','alumno1@correo.com','$2b$12$96bXxIFjOY2.rt2uGvfoMu2zoSzsNDmxk6ROtEkFHSMBEkmdtuxVa','2',NULL,NULL),(5,'Alumno2','Alumno2','alumno2@correo.com','$2b$12$y4TKx6OvVFv3cGWllQv2KOw0peotlPn5s/EmZAJpRLiqJ4wyGfob2','2',NULL,NULL),(6,'alumno3','alumno3','alumno3@correo.com','$2b$12$kx4gSyPonvs/EerosikpNexiSuXFe/d7a751Rckg37uoDMwXQstL2','2',NULL,NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-06 20:06:52
