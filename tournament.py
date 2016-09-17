#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    # delete all rows
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM players_count")
    total = c.fetchall[0][0]
    DB.commit()
    DB.close()
    return total
    


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    name_bleached = bleach.clean(name, strip=True)
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (player_name) VALUES (%s)", (name_bleached, ))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM player_standings")
    player_standings = c.fetchall()
    DB.commit() 
    DB.close()
    return player_standings
    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches (match_loser, match_winner) VALUE(%s, %s);", (loser, winner))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    c = DB.cursor()
    # count number of matches
    match_count = c.execute("SELECT COUNT(*) FROM matches")
    # get player standings
    c.execute("SELECT player_id, player_name FROM player_standings")
    standings = c.fetchall()
    DB.commit()
    # get initial seed 
    c.execute("SELECT player_id, player_name FROM initial_seed")
    initial_seed = c.fetchall()
    DB.commit()
    # get number of players
    num_players = count_players()
    
    pairings = []
    if match_count == 0:
        for i in range(0, num_players-1, 2):
            pairings.append(seed[i] + seed[i+1])
    else:
        for i in range(1, num_players-1, 2):
            pairings.append(standings[i] + standings[i+1])
    DB.close()
    return pairings





    

    


