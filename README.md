# web_security_analysis

SQL Queries to create database and tables

CREATE DATABASE WebSecurity;
USE WebSecurity;
CREATE TABLE Threats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100),
    severity VARCHAR(50),
    date_reported DATE
);

