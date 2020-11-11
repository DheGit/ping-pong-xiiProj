#Stores the information of the database

HOST="localhost"
USER="root" # Place the respective
PASS="pass"	# credentials here.
DBNAME="pongdata"

TB_GAMESTAT = "gamestat" #Name of the table storing game statuses 
C_ID="GameId"
C_WNAME="Winner"
C_LNAME="Loser"

Q_CREATE_PONGDATA="CREATE DATABASE "+DBNAME
Q_CREATE_GSTAT="CREATE TABLE "+TB_GAMESTAT+"("+C_ID+" INT AUTO_INCREMENT PRIMARY KEY, "+C_WNAME+" VARCHAR(32), "+C_LNAME+" VARCHAR(32))"
Q_ADD_GAME_DATA="INSERT INTO "+TB_GAMESTAT+" ("+C_WNAME+", "+C_LNAME+") VALUES ('{}', '{}')"
