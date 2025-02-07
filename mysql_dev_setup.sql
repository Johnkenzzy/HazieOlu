-- Prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS tm_dev_db;
CREATE USER IF NOT EXISTS 'tm_dev'@'localhost' IDENTIFIED BY 'tm_dev_pwd';
GRANT ALL PRIVILEGES ON tm_dev_db.* TO 'tm_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'tm_dev'@'localhost';
