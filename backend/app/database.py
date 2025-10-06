-- SQL to run manually or via migration tool
CREATE TABLE IF NOT EXISTS urls (
    short VARCHAR(10) PRIMARY KEY,
    original TEXT NOT NULL
);
