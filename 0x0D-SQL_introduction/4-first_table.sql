-- Script that creates a table called first_table in mysql server
-- 'IF NOT EXISTS' allows program to run without errors if db exist

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
