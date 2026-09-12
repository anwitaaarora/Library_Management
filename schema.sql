CREATE DATABASE IF NOT EXISTS Library;
USE Library;

-- Table to store book records
CREATE TABLE IF NOT EXISTS Books (
    BookID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Genre VARCHAR(100),
    Price INT NOT NULL,
    Quantity INT NOT NULL,
    Status VARCHAR(50) DEFAULT 'Available',
    IssuedTo INT DEFAULT NULL
);

-- Table to store user/member accounts
CREATE TABLE IF NOT EXISTS Accounts (
    AccID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Role VARCHAR(100) NOT NULL,
    Status VARCHAR(50) NOT NULL,
    Email VARCHAR(255) NOT NULL
);
