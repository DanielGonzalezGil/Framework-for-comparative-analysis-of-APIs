CREATE TABLE nba_players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    team VARCHAR(100),
    position VARCHAR(50),
    height VARCHAR(10),
    weight DECIMAL(5, 2),
    points_per_game DECIMAL(5, 2),
    assists_per_game DECIMAL(5, 2),
    rebounds_per_game DECIMAL(5, 2)
);


INSERT INTO nba_players (name, team, position, height, weight, points_per_game, assists_per_game, rebounds_per_game)
VALUES ('Michael Jordan', 'Chicago Bulls', 'Shooting Guard/Small Forward', '6 ft 6 in', 198, 30.1, 5.3, 6.2);

SELECT * FROM nba_players;

INSERT INTO nba_players (name, team, position, height, weight, points_per_game, assists_per_game, rebounds_per_game)
VALUES ('Kareem Abdul-Jabbar', 'Los Angeles Lakers', 'Center', '7 ft 2 in', 225, 24.6, 3.6, 11.2);

INSERT INTO nba_players (name, team, position, height, weight, points_per_game, assists_per_game, rebounds_per_game)
VALUES ('Dennis Rodman', 'Chicago Bulls', 'Power Forward/Small Forward', '6 ft 7 in', 210, 7.3, 1.8, 13.1);

INSERT INTO nba_players (name, team, position, height, weight, points_per_game, assists_per_game, rebounds_per_game)
VALUES ('Wilt Chamberlain', 'Los Angeles Lakers', 'Center', '7 ft 1 in', 275, 30.1, 4.4, 22.9);

INSERT INTO nba_players (name, team, position, height, weight, points_per_game, assists_per_game, rebounds_per_game)
VALUES ('Kobe Bryant', 'Los Angeles Lakers', 'Shooting Guard/Small Forward', '6 ft 6 in', 212, 25.0, 4.7, 5.2);

SELECT * FROM nba_players;



