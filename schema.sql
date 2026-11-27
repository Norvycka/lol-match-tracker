CREATE TABLE matches (
    match_id   TEXT PRIMARY KEY,
    game_start BIGINT NOT NULL,
    duration_s INT NOT NULL
);