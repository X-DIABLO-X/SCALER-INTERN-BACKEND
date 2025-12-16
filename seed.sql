-- =========================================================
-- seed.sql
-- Reference / lookup data only
-- =========================================================

BEGIN;

-- =====================
-- Show Types
-- =====================

INSERT INTO show_type (type_name) VALUES
('Movie'),
('TV Show')
ON CONFLICT DO NOTHING;

-- =====================
-- Ratings
-- =====================

INSERT INTO rating (rating_code) VALUES
('G'),
('PG'),
('PG-13'),
('R'),
('TV-Y'),
('TV-Y7'),
('TV-G'),
('TV-PG'),
('TV-14'),
('TV-MA'),
('NR')
ON CONFLICT DO NOTHING;

-- =====================
-- Genres (Netflix common categories)
-- =====================

INSERT INTO genre (genre_name) VALUES
('Action & Adventure'),
('Anime Features'),
('British TV Shows'),
('Children & Family Movies'),
('Classic Movies'),
('Comedies'),
('Crime TV Shows'),
('Documentaries'),
('Dramas'),
('Horror Movies'),
('Independent Movies'),
('International Movies'),
('International TV Shows'),
('Kids TV'),
('Reality TV'),
('Romantic Movies'),
('Sci-Fi & Fantasy'),
('Sports Movies'),
('TV Action & Adventure'),
('TV Comedies'),
('TV Dramas'),
('TV Horror'),
('TV Mysteries'),
('TV Thrillers')
ON CONFLICT DO NOTHING;

COMMIT;
