CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username, VARCHAR(1000) -- surely nobody has a username above 1000 characters
    lvl INT,
    exp INT,
    shrimp INT
);