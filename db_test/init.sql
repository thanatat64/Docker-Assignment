CREATE DATABASE IF NOT EXISTS db_test;
USE db_test;

CREATE TABLE Users (
    uid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Fname VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

INSERT INTO Users (Fname, age) VALUES ('admin', 21);