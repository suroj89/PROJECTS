CREATE DATABASE admin_login_system;

USE admin_login_system;

CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
password VARCHAR(100),
register_time DATETIME
);

CREATE TABLE login_logs(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
login_time DATETIME
);

CREATE TABLE admin(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100),
password VARCHAR(100)
);

INSERT INTO admin(username,password)
VALUES('admin','admin123');
