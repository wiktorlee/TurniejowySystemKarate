DROP TABLE IF EXISTS athletes CASCADE;
DROP TABLE IF EXISTS categories CASCADE;
DROP TABLE IF EXISTS clubs CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  login TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE clubs (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE,
  city TEXT NOT NULL
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  code TEXT NOT NULL UNIQUE,
  name TEXT NOT NULL,
  min_age INTEGER,
  max_age INTEGER,
  min_weight NUMERIC(5,2),
  max_weight NUMERIC(5,2),
  gender TEXT CHECK (gender IN ('M','F','OPEN')) DEFAULT 'OPEN'
);

CREATE TABLE athletes (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  birth_date DATE,
  gender TEXT CHECK (gender IN ('M','F')),
  weight NUMERIC(5,2),
  grade TEXT,
  club_id INTEGER REFERENCES clubs(id) ON DELETE SET NULL
);

CREATE INDEX idx_athletes_name ON athletes(last_name, first_name);
