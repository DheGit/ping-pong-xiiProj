HostName = "localhost"
UserName = "root"
Password = "password"	# Enter your MySQL Password here
DatabaseName = "PongData"

TableName = "GameStats"

C_ID = "GameId"
C_WINNER = "Winner"
C_WSCORE = "Winner_Score"
C_LOSER = "Loser"
C_LSCORE = "Loser_Score"

Q_CREATE_PONGDATA = "CREATE DATABASE "+DatabaseName
Q_CREATE_GAMESTATS = "CREATE TABLE "+TableName+"("+C_ID+" INT AUTO_INCREMENT PRIMARY KEY, "+C_WINNER+" VARCHAR(32), "+C_WSCORE+" INTEGER, "+C_LOSER+" VARCHAR(32), "+C_LSCORE+" INTEGER)"
Q_ADD_GAME_DATA = "INSERT INTO "+TableName+" ("+C_WINNER+", "+C_WSCORE+", "+C_LOSER+", "+C_LSCORE+") VALUES ('{}', {}, '{}', {})"
