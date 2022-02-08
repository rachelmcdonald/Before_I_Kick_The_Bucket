DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visited BOOLEAN,
  country_id INT REFERENCES countries(id)
);
-- This is the first part of the four CRUD
-- operations: CREATE, where I am using the
-- "INSERT" clause to create a new value within
-- the name variable
INSERT INTO countries (name, visited) VALUES ('France', True);
INSERT INTO countries (name, visited) VALUES ('Scotland', True);
INSERT INTO cities (name, visited, country_id) VALUES ('Edinburgh', True, 2);
INSERT INTO cities (name, visited, country_id) VALUES ('Paris', True, 1);
-- This is the second part of the four CRUD
-- operations: READ, where I am using the
-- "SELECT" clause to read the fields I have selected
-- in this instance is all from the table "countries"
SELECT * FROM countries;
-- This is the third part of the four CRUD
-- operations: UPDATE, where I am using the 
-- "UPDATE" clause to change the values, or specific value
-- as I demonstrate here, in the exisiting records within my database.
UPDATE cities SET visited = false WHERE name = 'Paris';
SELECT * FROM cities;
