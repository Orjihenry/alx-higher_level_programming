-- Script that creates a table second_table in the database
-- second_table should have 'id', 'name' and 'score'
-- should not return any errors if table exists

CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	score INT
);

-- The id arguement does not need to be passed as it has
-- an auto_increment feature. It will automatically be 
-- issued an id accordingly.
INSERT INTO second_table (name, score)
 VALUES ('John', 0), ('Alex', 3), ('Bob', 14), ('George', 8);
