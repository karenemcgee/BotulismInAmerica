
DROP TABLE IF EXISTS BOTULISM;


--========================================================================================

-- Before running, modify the csv import portion to explicitly define the directory where the
-- csv file is located.  You might need to set permissions in that directory so the script
-- can access the file.  


--CREATE TABLES

CREATE TABLE BOTULISM (
	state_name VARCHAR(100) NOT NULL,
	record_year INT NOT NULL,
	BotType VARCHAR(100) NOT NULL,
	ToxinType VARCHAR(100) NOT NULL,
	record_count INT NOT NULL
  );
  

COPY BOTULISM(state_name, record_year, BotType, ToxinType, record_count)
FROM 'c:\users\stacey.smith\source\Project2\data\Botulism.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM BOTULISM LIMIT 10
--========================================================================================
