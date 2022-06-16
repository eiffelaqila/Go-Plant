-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: goplant
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

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
-- Current Database: `goplant`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `goplant` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `goplant`;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  PRIMARY KEY (`id_admin`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','admin123');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderlist`
--

DROP TABLE IF EXISTS `orderlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orderlist` (
  `id_orderlist` int(11) NOT NULL AUTO_INCREMENT,
  `id_pelanggan` int(11) NOT NULL,
  `id_tanaman` int(11) NOT NULL,
  `jumlah_sewa` int(11) NOT NULL,
  `tanggal_awal` date NOT NULL,
  `tanggal_akhir` date NOT NULL,
  `status` int(11) DEFAULT 1,
  PRIMARY KEY (`id_orderlist`),
  KEY `id_pelanggan` (`id_pelanggan`),
  KEY `id_tanaman` (`id_tanaman`),
  CONSTRAINT `orderlist_ibfk_1` FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id_pelanggan`),
  CONSTRAINT `orderlist_ibfk_2` FOREIGN KEY (`id_tanaman`) REFERENCES `tanaman` (`id_tanaman`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderlist`
--

LOCK TABLES `orderlist` WRITE;
/*!40000 ALTER TABLE `orderlist` DISABLE KEYS */;
INSERT INTO `orderlist` VALUES (1,1,3,5,'2022-03-03','2022-05-05',1),(2,1,4,2,'2022-03-03','2022-05-05',1),(3,4,1,3,'2022-02-10','2022-03-01',1),(4,2,2,2,'2022-02-02','2022-02-22',1),(5,3,6,3,'2022-03-10','2022-05-04',1),(6,3,7,4,'2022-03-10','2022-05-04',1),(7,5,8,1,'2022-04-10','2022-05-14',1),(8,2,3,1,'2022-04-04','2022-05-05',1),(9,3,1,3,'2022-03-02','2022-06-07',1),(10,4,2,6,'2022-04-01','2022-09-25',1),(11,3,2,6,'2022-04-01','2022-09-25',1),(12,3,4,6,'2022-04-01','2022-09-25',1),(13,3,3,6,'2022-04-01','2022-09-20',1),(14,3,1,3,'2022-04-01','2022-09-03',1),(15,3,8,3,'2022-04-01','2022-10-03',1),(16,3,8,3,'2022-04-01','2022-11-03',1),(17,3,7,3,'2022-04-01','2022-01-03',1),(18,3,7,3,'2022-04-20','2022-01-03',0),(19,2,2,3,'2022-04-22','2022-01-03',0),(20,4,6,2,'2022-04-25','2022-01-15',0),(21,3,5,2,'2022-04-26','2022-01-15',0),(22,1,3,2,'2022-04-25','2022-01-15',0),(23,2,3,2,'2022-04-26','2022-01-15',0),(24,2,8,4,'2022-04-26','2022-01-18',0),(25,4,5,19,'2022-04-26','2022-01-20',0),(26,5,1,6,'2022-04-27','2022-01-20',0);
/*!40000 ALTER TABLE `orderlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pelanggan`
--

DROP TABLE IF EXISTS `pelanggan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pelanggan` (
  `id_pelanggan` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  `alamat` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`id_pelanggan`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pelanggan`
--

LOCK TABLES `pelanggan` WRITE;
/*!40000 ALTER TABLE `pelanggan` DISABLE KEYS */;
INSERT INTO `pelanggan` VALUES (1,'ilham','ilham123','jalan ilham'),(2,'eiffel','eiffel123','jalan eiffel'),(3,'yakobus','yakobus123','jalan yakobus'),(4,'hilda','hilda123','jalan hilda'),(5,'customer','customer123','customer address');
/*!40000 ALTER TABLE `pelanggan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tanaman`
--

DROP TABLE IF EXISTS `tanaman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tanaman` (
  `id_tanaman` int(11) NOT NULL AUTO_INCREMENT,
  `nama_tanaman` varchar(120) NOT NULL,
  `deskripsi_tanaman` varchar(500) DEFAULT NULL,
  `stok` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `img_path` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_tanaman`),
  UNIQUE KEY `nama_tanaman` (`nama_tanaman`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tanaman`
--

LOCK TABLES `tanaman` WRITE;
/*!40000 ALTER TABLE `tanaman` DISABLE KEYS */;
INSERT INTO `tanaman` VALUES (1,'Lidah Mertua','Lidah mertua atau dengan nama latin Sansevieria, merupakan tanaman hias daun yang bisa kamu pilih sebagai tanaman hias di rumah. Tanaman ini cukup populer di kalangan pecinta tanaman hias, karena mampu tumbuh dengan sedikit cahaya matahari dan air. Lidah mertua juga memberikan beberapa manfaat, di antaranya mengandung antiseptik alami dengan anti racun yang baik, sehingga bisa digunakan untuk membunuh kuman.',1,1000,'img/Lidah mertua.jpg'),(2,'Janda Bolong','Tanaman hias satu ini termasuk pada jenis tanaman yang langka dan mahal di Indonesia, karena aslinya berasal dari Amerika Tengah. Janda bolong menjadi tanaman hias daun untuk dekorasi kekinian yang memiliki banyak penggemarnya. Tanaman janda bolong juga memiliki beberapa manfaat yaitu untuk memperbaiki kualitas udara. Tanaman ini juga cocok diletakan di dalam rumah karena dapat menyerap zat yang beracun di udara.',1,1000,'img/Janda bolong.jpg'),(3,'Sirih Gading','Sirih gading dapat menjadi alternatif pilihan tanaman hias selanjutnya, yang mudah ditemukan dan tidak membutuhkan perawatan yang sulit. Tanaman ini akan memberikan suasana segar karena warnanya hijau cerah. Selain sebagai hiasan, tanaman sirih gading memiliki manfaat untuk memberikan efek tenang, sebagai pemasok oksigen dan dapat menyedot racun berbahaya yang terdapat di udara.',1,1000,'img/Sirih Gading.png'),(4,'Suplir','Meskipun tanaman hias ini sudah cukup lama populer di Indonesia, namun tanaman ini cukup mudah untuk ditemukan dirawat. Sehingga tidak heran jika suplir menjadi tanaman yang populer dan banyak ditemukan di rumah-rumah. Tanaman hias suplir ini juga bagus untuk kesehatan, selain manfaatnya yang mampu memberikan kesejukan dan asri. Suplir cocok ditanam di dalam rumah karena mampu meningkatkan kualitas udara.',1,1000,'img/Suplir.jpg'),(5,'Gelombang Cinta','Inspirasi tanaman hias lainnya yaitu gelombang cinta, yang menjadi salah satu tanaman hias daun paling populer. Baik diletakkan di dalam maupun luar rumah, akan sangat indah mengisi pojok ruangan. Tanaman hias ini memiliki harga yang relatif mahal dikarenakan keindahan dan keunikannya. Selain itu, tanaman ini jadi cenderung memiliki penggemar dan pembeli yang berasal dari kalangan atas, karena harga tersebut.',1,1000,'img/Gelombang Cinta.jpg'),(6,'Lili Paris','Lili paris juga cocok untuk diletakkan di pot gantung selain ditanam di taman, sehingga menambah nilai keindahan visualnya. Tanaman ini mampu beradaptasi di segala lingkungan sehingga mudah dirawat. Lili paris juga memberikan manfaat berupa penghasil oksigen, menghilangkan racun dari cat dinding maupun perabotan di dalam rumah.',1,1000,'img/Lili Paris.jpeg'),(7,'Pucuk Merak','Tanaman hias ini memiliki bagian pucuk yang berwarna kemerahan, sesuai dengan namanya. Tumbuhan jenis ini biasanya tumbuh dengan rimbun sehingga sering menjadi pembatas halaman atana tanaman pagar. Selain itu, tanaman pucuk merah juga memberikan beberapa manfaat di antaranya untuk menurunkan kadar gula darah, meningkatkan fungsi kekebalan tubuh dan melawan pertumbuhan kanker.',1,1000,'img/Pucuk Merah.jpeg'),(8,'Kuping Gajah','Kuping gajah bisa menambah koleksi tanaman di rumah kamu, karena tanaman ini merupakan tumbuhan yang populer di Indonesia. Bentuknya yang melebar sehingga sering disebut sebagai bunga kuping gajah. Terdapat beberapa manfaat yang diberikan dari tanaman kuping gajah, di antaranya adalah untuk mempercepat penuaan bisul, sebagai obat relaksasi, mengobati penyakit kulit, mencegah infeksi karena kuman dan bakteri, serta untuk menyembuhkan pembengkakan pada mulut dan tenggorokan.',1,1000,'img/Kuping Gajah.png'),(9,'Calathea','Tanaman hias calathea ini memiliki motif daun yang belang-belang sehingga mampu memberikan keindahan secara visual. Calathea memiliki komposisi warna dan pola yang berbeda-beda. Selain memberikan keindahan dan kecantikan, calathea juga memberikan manfaat sebagai suplai udara bersih. Tanaman ini juga sangat cocok bila ditanam di kota-kota besar.',1,1000,'img/Calathea.jpg'),(10,'Daun Dollar','Disebut daun dolar karena tumbuhan hias ini memiliki daun yang banyak dan berukuran cukup kecil. Daun yang dimiliki tebal dengan tampilan yang mengkilap. Tanaman hias daun ini cocok digunakan sebagai dekorasi di dalam ruangan. Tanaman hias yang mudah untuk dirawat ini memiliki beberapa manfaat bagi kesehatan, yaitu sebagai obat diare, anti bakteri, mengatasi wasir, melancarkan pencernaan dan mengatasi pegal.',1,1000,'img/Daun Dollar.jpeg');
/*!40000 ALTER TABLE `tanaman` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-20 15:47:52
