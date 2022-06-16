CREATE TABLE Admin (
    id_admin INT AUTO_INCREMENT,
    username VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL,
    PRIMARY KEY(id_admin)
);

CREATE TABLE Pelanggan (
    id_pelanggan INT AUTO_INCREMENT,
    username VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL,
    alamat VARCHAR(120),
    PRIMARY KEY(id_pelanggan)
);

CREATE TABLE Tanaman (
    id_tanaman INT AUTO_INCREMENT,
    nama_tanaman VARCHAR(120) UNIQUE NOT NULL,
    deskripsi_tanaman VARCHAR(500),
    stok INT NOT NULL,
    harga INT NOT NULL,
    img_path VARCHAR(255),
    PRIMARY KEY(id_tanaman)
);

CREATE TABLE OrderList (
    id_orderlist INT AUTO_INCREMENT,
    id_pelanggan INT NOT NULL,
    id_tanaman INT NOT NULL,
    jumlah_sewa INT NOT NULL,
    tanggal_awal DATE NOT NULL,
    tanggal_akhir DATE NOT NULL,
    PRIMARY KEY(id_orderlist),
    FOREIGN KEY (id_pelanggan) REFERENCES Pelanggan(id_pelanggan),
    FOREIGN KEY (id_tanaman) REFERENCES Tanaman(id_tanaman)
);