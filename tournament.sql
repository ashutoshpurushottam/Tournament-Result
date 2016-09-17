-- Table definitions for the tournament project.

-- Delete the database if it exists already
DROP DATABASE IF EXISTS tournament;

-- Create database 
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Players table
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	player_name TEXT NOT NULL
);

-- Matches table
CREATE TABLE matches(
	match_id SERIAL PRIMARY KEY,
	match_loser INT REFERENCES players(player_id),
	match_winner INT REFERENCES players(player_id)
);

-- Views --

-- Player count
CREATE OR REPLACE View players_count AS
SELECT COUNT(*) FROM players;

-- Random seeding of matches before the tournament starts
CREATE OR REPLACE View initial_seed AS
SELECT * FROM players ORDER BY random();

-- Player standing 
CREATE OR REPLACE View player_standings AS
SELECT  player_id, player_name, SUM(CASE WHEN players.player_id = matches.match_winner THEN 1 ELSE 0 END) AS win_count,
COUNT(matches) AS match_count
FROM players
LEFT OUTER JOIN matches
ON players.player_id = matches.match_winner OR players.player_id = matches.match_loser
GROUP BY player_id
ORDER BY win_count DESC, match_count ASC;







	
	
	
	  



