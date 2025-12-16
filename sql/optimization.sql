-- Indexes Added for Optimization

-- Ensure these indexes exist to optimize performance for the provided queries and views

-- Index on show.release_year (already present in schema, but good to ensure)
CREATE INDEX IF NOT EXISTS idx_show_release_year ON show(release_year);

-- Index on show.type_id (already present in schema)
CREATE INDEX IF NOT EXISTS idx_show_type_id ON show(type_id);

-- New Indexes for Join Key Performance
CREATE INDEX IF NOT EXISTS idx_show_genre_show_id ON show_genre(show_id);
CREATE INDEX IF NOT EXISTS idx_show_country_show_id ON show_country(show_id);
CREATE INDEX IF NOT EXISTS idx_show_person_show_id ON show_person(show_id);

-- Example Optimization Analysis
-- Before:
-- EXPLAIN ANALYZE SELECT * FROM show WHERE release_year = 2021;
-- After:
-- EXPLAIN ANALYZE SELECT * FROM show WHERE release_year = 2021;
