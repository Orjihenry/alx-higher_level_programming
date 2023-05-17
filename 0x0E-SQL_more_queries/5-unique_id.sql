-- Script that creates the table unique_id with a default value of 1
-- id must be unique

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
