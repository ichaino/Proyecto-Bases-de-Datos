CREATE DATABASE  IF NOT EXISTS `matriculas` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `matriculas`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: matriculas
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `calificaciones`
--

DROP TABLE IF EXISTS `calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calificaciones` (
  `Calificaciones_ID` int NOT NULL,
  `Estudiante_ID` int NOT NULL,
  `Curso_ID` int NOT NULL,
  `Nota` decimal(2,1) NOT NULL,
  `Fecha_Evaluaciones` date NOT NULL,
  PRIMARY KEY (`Calificaciones_ID`),
  KEY `Estudiante_ID` (`Estudiante_ID`),
  KEY `Curso_ID` (`Curso_ID`),
  CONSTRAINT `calificaciones_ibfk_1` FOREIGN KEY (`Estudiante_ID`) REFERENCES `estudiante` (`Estudiante_ID`),
  CONSTRAINT `calificaciones_ibfk_2` FOREIGN KEY (`Curso_ID`) REFERENCES `cursos` (`Curso_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificaciones`
--

LOCK TABLES `calificaciones` WRITE;
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
INSERT INTO `calificaciones` VALUES (1,1,1,4.8,'2024-07-15'),(2,2,2,5.0,'2024-07-20'),(3,3,3,4.2,'2024-07-25'),(4,4,4,3.9,'2024-08-01'),(5,5,5,4.5,'2024-08-05'),(6,6,6,4.7,'2024-08-10'),(7,7,3,4.5,'2024-09-10'),(8,8,3,5.8,'2024-09-10'),(9,9,5,4.6,'2024-09-15');
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso_estudiante`
--

DROP TABLE IF EXISTS `curso_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso_estudiante` (
  `Curso_ID` int NOT NULL,
  `Estudiante_ID` int NOT NULL,
  PRIMARY KEY (`Curso_ID`,`Estudiante_ID`),
  KEY `Estudiante_ID` (`Estudiante_ID`),
  CONSTRAINT `curso_estudiante_ibfk_1` FOREIGN KEY (`Curso_ID`) REFERENCES `cursos` (`Curso_ID`),
  CONSTRAINT `curso_estudiante_ibfk_2` FOREIGN KEY (`Estudiante_ID`) REFERENCES `estudiante` (`Estudiante_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso_estudiante`
--

LOCK TABLES `curso_estudiante` WRITE;
/*!40000 ALTER TABLE `curso_estudiante` DISABLE KEYS */;
INSERT INTO `curso_estudiante` VALUES (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(3,7),(3,8),(5,9);
/*!40000 ALTER TABLE `curso_estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cursos`
--

DROP TABLE IF EXISTS `cursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cursos` (
  `Curso_ID` int NOT NULL,
  `Facultad_ID` int NOT NULL,
  `Nombre_Curso` varchar(100) NOT NULL,
  `Creditos` int NOT NULL,
  `Requisitos` tinyint(1) NOT NULL,
  PRIMARY KEY (`Curso_ID`),
  KEY `Facultad_ID` (`Facultad_ID`),
  CONSTRAINT `cursos_ibfk_1` FOREIGN KEY (`Facultad_ID`) REFERENCES `facultad` (`Facultad_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cursos`
--

LOCK TABLES `cursos` WRITE;
/*!40000 ALTER TABLE `cursos` DISABLE KEYS */;
INSERT INTO `cursos` VALUES (1,1,'Introducción al Derecho',4,1),(2,1,'Derecho Constitucional',5,1),(3,2,'Programación',4,0),(4,2,'Calculo III',5,1),(5,3,'Psicología Social',4,0),(6,3,'Teorías de la Personalidad',5,1);
/*!40000 ALTER TABLE `cursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `Estudiante_ID` int NOT NULL,
  `Direccion` varchar(100) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Fecha_Nacimiento` date NOT NULL,
  `Telefono` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  PRIMARY KEY (`Estudiante_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiante`
--

LOCK TABLES `estudiante` WRITE;
/*!40000 ALTER TABLE `estudiante` DISABLE KEYS */;
INSERT INTO `estudiante` VALUES (1,'Ejército 260','María Contreras','2001-02-12','987654321','maria.contreras@udp.cl'),(2,'Vergara 249','Andrés Morales','2000-05-18','987123456','andres.morales@udp.cl'),(3,'República 180','Paula Soto','1999-07-25','987987987','paula.soto@udp.cl'),(4,'Ejército 141','Jorge Torres','2002-03-30','987321654','jorge.torres@udp.cl'),(5,'Ejército 333','Carla Vidal','2000-12-09','987456123','carla.vidal@udp.cl'),(6,'Vergara 678','Rodrigo López','2001-11-01','987654654','rodrigo.lopez@udp.cl'),(7,'Santa Isabel 123','Luis Martínez','2002-04-15','987654789','luis.martinez@udp.cl'),(8,'Carmen 456','Ana Gómez','2001-09-22','987321987','ana.gomez@udp.cl'),(9,'Providencia 789','Diego Pérez','1998-12-05','987987321','diego.perez@udp.cl');
/*!40000 ALTER TABLE `estudiante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facultad`
--

DROP TABLE IF EXISTS `facultad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facultad` (
  `Facultad_ID` int NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Ubicacion` varchar(100) NOT NULL,
  PRIMARY KEY (`Facultad_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facultad`
--

LOCK TABLES `facultad` WRITE;
/*!40000 ALTER TABLE `facultad` DISABLE KEYS */;
INSERT INTO `facultad` VALUES (1,'Facultad de Derecho','Edificio A - Ejército 260'),(2,'Facultad de Ingeniería','Edificio B - Vergara 249'),(3,'Facultad de Psicología','Edificio C - República 180');
/*!40000 ALTER TABLE `facultad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horario_sala`
--

DROP TABLE IF EXISTS `horario_sala`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horario_sala` (
  `Horario_ID` int NOT NULL,
  `Sala_ID` int NOT NULL,
  PRIMARY KEY (`Horario_ID`,`Sala_ID`),
  KEY `Sala_ID` (`Sala_ID`),
  CONSTRAINT `horario_sala_ibfk_1` FOREIGN KEY (`Horario_ID`) REFERENCES `horarios` (`Horario_ID`),
  CONSTRAINT `horario_sala_ibfk_2` FOREIGN KEY (`Sala_ID`) REFERENCES `salas` (`Sala_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horario_sala`
--

LOCK TABLES `horario_sala` WRITE;
/*!40000 ALTER TABLE `horario_sala` DISABLE KEYS */;
INSERT INTO `horario_sala` VALUES (2,1),(4,2),(1,3),(6,3),(5,4),(3,5);
/*!40000 ALTER TABLE `horario_sala` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `Horario_ID` int NOT NULL,
  `Curso_ID` int NOT NULL,
  `Sala_ID` int NOT NULL,
  `Dia` varchar(20) NOT NULL,
  `Hora_Inicio` time NOT NULL,
  `Hora_Fin` time NOT NULL,
  PRIMARY KEY (`Horario_ID`),
  KEY `Curso_ID` (`Curso_ID`),
  KEY `Sala_ID` (`Sala_ID`),
  CONSTRAINT `horarios_ibfk_1` FOREIGN KEY (`Curso_ID`) REFERENCES `cursos` (`Curso_ID`),
  CONSTRAINT `horarios_ibfk_2` FOREIGN KEY (`Sala_ID`) REFERENCES `salas` (`Sala_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (1,1,1,'Lunes','08:30:00','10:00:00'),(2,2,1,'Lunes','10:15:00','11:45:00'),(3,3,4,'Martes','08:30:00','10:00:00'),(4,4,5,'Martes','10:15:00','11:45:00'),(5,5,2,'Miércoles','08:30:00','10:00:00'),(6,6,3,'Miércoles','10:15:00','11:45:00');
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matricula`
--

DROP TABLE IF EXISTS `matricula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matricula` (
  `Inscripcion_ID` int NOT NULL,
  `Estudiante_ID` int NOT NULL,
  `Curso_ID` int NOT NULL,
  `Fecha_Inscripcion` date NOT NULL,
  `Estado` varchar(100) NOT NULL,
  PRIMARY KEY (`Inscripcion_ID`),
  KEY `Estudiante_ID` (`Estudiante_ID`),
  KEY `Curso_ID` (`Curso_ID`),
  CONSTRAINT `matricula_ibfk_1` FOREIGN KEY (`Estudiante_ID`) REFERENCES `estudiante` (`Estudiante_ID`),
  CONSTRAINT `matricula_ibfk_2` FOREIGN KEY (`Curso_ID`) REFERENCES `cursos` (`Curso_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matricula`
--

LOCK TABLES `matricula` WRITE;
/*!40000 ALTER TABLE `matricula` DISABLE KEYS */;
INSERT INTO `matricula` VALUES (1,1,1,'2024-03-01','En Curso'),(2,2,2,'2024-03-02','En Curso'),(3,3,3,'2024-03-03','En Curso'),(4,4,4,'2024-03-04','En Curso'),(5,5,5,'2024-03-05','En Curso'),(6,6,6,'2024-03-06','En Curso'),(7,7,3,'2024-03-07','Reprobado'),(8,8,3,'2024-03-08','Reprobado'),(9,9,5,'2024-03-09','Reprobado');
/*!40000 ALTER TABLE `matricula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesor_curso`
--

DROP TABLE IF EXISTS `profesor_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesor_curso` (
  `Profesor_ID` int NOT NULL,
  `Curso_ID` int NOT NULL,
  PRIMARY KEY (`Profesor_ID`,`Curso_ID`),
  KEY `Curso_ID` (`Curso_ID`),
  CONSTRAINT `profesor_curso_ibfk_1` FOREIGN KEY (`Profesor_ID`) REFERENCES `profesores` (`Profesor_ID`),
  CONSTRAINT `profesor_curso_ibfk_2` FOREIGN KEY (`Curso_ID`) REFERENCES `cursos` (`Curso_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesor_curso`
--

LOCK TABLES `profesor_curso` WRITE;
/*!40000 ALTER TABLE `profesor_curso` DISABLE KEYS */;
INSERT INTO `profesor_curso` VALUES (1,1),(1,2),(2,3),(3,4),(4,5),(5,6);
/*!40000 ALTER TABLE `profesor_curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profesores`
--

DROP TABLE IF EXISTS `profesores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profesores` (
  `Profesor_ID` int NOT NULL,
  `Facultad_ID` int NOT NULL,
  `Nombre_Profesor` varchar(100) NOT NULL,
  `Especialidad` varchar(100) NOT NULL,
  `Telefono_Profesor` varchar(100) NOT NULL,
  `Email_Profesor` varchar(100) NOT NULL,
  PRIMARY KEY (`Profesor_ID`),
  KEY `Facultad_ID` (`Facultad_ID`),
  CONSTRAINT `profesores_ibfk_1` FOREIGN KEY (`Facultad_ID`) REFERENCES `facultad` (`Facultad_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profesores`
--

LOCK TABLES `profesores` WRITE;
/*!40000 ALTER TABLE `profesores` DISABLE KEYS */;
INSERT INTO `profesores` VALUES (1,1,'Dr. Pedro Alarcón','Derecho Constitucional','223456789','pedro.alarcon@udp.cl'),(2,2,'Ing. Javier Morales','Programación','224567890','javier.morales@udp.cl'),(3,2,'Ing. Camila Vargas','Matemáticas Aplicadas','225678901','camila.vargas@udp.cl'),(4,3,'Dra. Carolina Díaz','Psicología Social','226789012','carolina.diaz@udp.cl'),(5,3,'Dr. Francisco González','Psicología Clínica','227890123','francisco.gonzalez@udp.cl');
/*!40000 ALTER TABLE `profesores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salas`
--

DROP TABLE IF EXISTS `salas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salas` (
  `Sala_ID` int NOT NULL,
  `Numero_Sala` int NOT NULL,
  `Capacidad` int NOT NULL,
  PRIMARY KEY (`Sala_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salas`
--

LOCK TABLES `salas` WRITE;
/*!40000 ALTER TABLE `salas` DISABLE KEYS */;
INSERT INTO `salas` VALUES (1,101,40),(2,102,35),(3,103,30),(4,201,45),(5,202,50),(6,203,25);
/*!40000 ALTER TABLE `salas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'matriculas'
--

--
-- Dumping routines for database 'matriculas'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-02 17:25:18
