CREATE TABLE users (
    discord_user VARCHAR(1000) NOT NULL, 
    username VARCHAR(1000) NOT NULL, -- surely nobody has a username above 1000 characters
    lvl INT DEFAULT 1,
    exp INT DEFAULT 0,
    shrimp INT DEFAULT 0 -- currency name
);