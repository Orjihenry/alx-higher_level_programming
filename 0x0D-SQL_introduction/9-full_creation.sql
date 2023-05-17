-- Script that creates a table second_table in the database
-- second_table should have 'id', 'name' and 'score'
-- should not return any errors if table exists

CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	score INT
);

INSERT INTO second_table (id, name, score)
 VALUES (1, 'John', 0), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
