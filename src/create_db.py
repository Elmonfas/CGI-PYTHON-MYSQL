#!/usr/bin/python3
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    if con.is_connected():
        print("Conexión establecida correctamente")
        cur = con.cursor()
        cur.execute("DROP DATABASE IF EXISTS exploreexpress;")
        cur.execute("CREATE DATABASE exploreexpress;")
        cur.execute("USE exploreexpress;")
        cur.execute("""CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            rol VARCHAR(20) NOT NULL
        );""")
        cur.execute("""CREATE TABLE lugares (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            img VARCHAR(200) NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            usuario_id INT,
            FOREIGN KEY (usuario_id) REFERENCES users(id)
        );""")
        cur.execute("INSERT INTO users (email, password, rol) VALUES ('admin@admin.com', 'admin', 'admin');")

        con.commit()
        cur.close()
        con.close()
except Exception as e:
    print("Error en la conexión SQL:", e)