-- Table definitions for the tournament project.

-- Delete the database if it exists already
DROP DATABASE IF EXISTS tournament;

-- Create database 
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Players table
CREATE TABLE players(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

-- Matches table
CREATE TABLE matches(
	id SERIAL PRIMARY KEY,
	match_loser INT REFERENCES players(id),
	match_winner INT REFERENCES players(id)
);

-- Views --

-- Player standing 
CREATE OR REPLACE View player_standings AS
	SELECT  players.id AS player_id, name, SUM(CASE WHEN players.id = matches.match_winner THEN 1 ELSE 0 END) AS win_count,
	COUNT(matches) AS match_count
	FROM players
	LEFT OUTER JOIN matches
	ON players.id = matches.match_winner OR players.id = matches.match_loser
	GROUP BY player_id
	ORDER BY win_count DESC, match_count ASC;







	
	
	
	  



