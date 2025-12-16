-- =========================================================
-- schema.sql
-- Production-grade normalized schema for Netflix dataset
-- PostgreSQL 15 / NeonDB
-- =========================================================

BEGIN;

-- =====================
-- Lookup Tables
-- =====================

CREATE TABLE show_type (
    type_id SMALLSERIAL PRIMARY KEY,
    type_name TEXT NOT NULL UNIQUE
);

CREATE TABLE rating (
    rating_id SMALLSERIAL PRIMARY KEY,
    rating_code TEXT NOT NULL UNIQUE
);

CREATE TABLE genre (
    genre_id SMALLSERIAL PRIMARY KEY,
    genre_name TEXT NOT NULL UNIQUE
);

CREATE TABLE country (
    country_id SMALLSERIAL PRIMARY KEY,
    country_name TEXT NOT NULL UNIQUE
);

-- =====================
-- Core Tables
-- =====================

CREATE TABLE show (
    show_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    type_id SMALLINT NOT NULL REFERENCES show_type(type_id),
    rating_id SMALLINT REFERENCES rating(rating_id),
    release_year INTEGER CHECK (release_year >= 1900),
    date_added DATE,
    duration_value INTEGER CHECK (duration_value > 0),
    duration_unit TEXT CHECK (duration_unit IN ('min', 'season', 'seasons')),
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE person (
    person_id BIGSERIAL PRIMARY KEY,
    full_name TEXT NOT NULL UNIQUE
);

-- =====================
-- Junction Tables
-- =====================

CREATE TABLE show_person (
    show_id TEXT NOT NULL REFERENCES show(show_id) ON DELETE CASCADE,
    person_id BIGINT NOT NULL REFERENCES person(person_id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK (role IN ('Director', 'Cast')),
    PRIMARY KEY (show_id, person_id, role)
);

CREATE TABLE show_country (
    show_id TEXT NOT NULL REFERENCES show(show_id) ON DELETE CASCADE,
    country_id SMALLINT NOT NULL REFERENCES country(country_id),
    PRIMARY KEY (show_id, country_id)
);

CREATE TABLE show_genre (
    show_id TEXT NOT NULL REFERENCES show(show_id) ON DELETE CASCADE,
    genre_id SMALLINT NOT NULL REFERENCES genre(genre_id),
    PRIMARY KEY (show_id, genre_id)
);

-- =====================
-- Indexes (Performance)
-- =====================

CREATE INDEX idx_show_title ON show(title);
CREATE INDEX idx_show_release_year ON show(release_year);
CREATE INDEX idx_show_type ON show(type_id);
CREATE INDEX idx_show_rating ON show(rating_id);
CREATE INDEX idx_person_name ON person(full_name);

COMMIT;
