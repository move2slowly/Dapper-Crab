CREATE TABLE users (
    id PRIMARY KEY,
    discord_user VARCHAR(1000) NOT NULL, 
    username VARCHAR(1000) NOT NULL, -- surely nobody has a username above 1000 characters
    lvl INT DEFAULT 1,
    exp INT DEFAULT 0,
    shrimp INT DEFAULT 0, -- currency name
    last_daily TIMESTAMP -- the last time a user used the daily command
);

CREATE TABLE items (
    id PRIMARY KEY,
    item_name VARCHAR(50),
    item_rarity REAL,
    item_dscr VARCHAR(1000),
    item_image_url VARCHAR(500)
);

CREATE TABLE player_items (
    id PRIMARY KEY,
    user_id INT,
    item_id INT,
    quantity INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (item_id) REFERENCES items(id)
);