-- Script that creates the database hbtn_0d_2, user and grants a privilege
-- the script should not return an error if user or database exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creates user and grants the user SELECT privileges
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
