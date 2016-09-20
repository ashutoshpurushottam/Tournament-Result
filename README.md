# Tournament-Result
Udacity Fullstack Nanodegree Project. The project works with a PostgreSQL database to set up a tournament
based on Swiss-Pairing.


## What's included
Tournament project 
- tournament.sql
- tournament.py
- tournament_test.py


### tournament.sql
Sets up tournament database schema with tables like players, matches and view for player standings.

### tournament.py
Contains methods to connect, read, add, delete players and matches in swiss-pairings.

### tournament_test.py
Contains code to test CRUD operations.

##How to run the project ?
1. Clone or download the project in your computer. 
2. Install virtual machine on your computer [https://udacity.atlassian.net/wiki/display/BENDH/Vagrant+VM+Installation] 
3. Inside your virtual machine move to /vagrant/tournament directory
4. Load SQL schema: `psql tournament < tournament.sql`
5. For testing the project run the test file: `/vagrant/tournament$ python tournament_test.py`

