-- Stored Procedure: Get Titles by Genre
CREATE OR REPLACE FUNCTION get_titles_by_genre(p_genre TEXT)
RETURNS TABLE (
    show_id TEXT,
    title TEXT,
    release_year INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.show_id,
        s.title,
        s.release_year
    FROM show s
    JOIN show_genre sg ON s.show_id = sg.show_id
    JOIN genre g ON sg.genre_id = g.genre_id
    WHERE g.genre_name = p_genre;
END;
$$;

-- Usage:
-- SELECT * FROM get_titles_by_genre('Documentaries');

-- Stored Procedure: Titles by Country
CREATE OR REPLACE FUNCTION get_titles_by_country(p_country TEXT)
RETURNS TABLE (
    title TEXT,
    release_year INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.title,
        s.release_year
    FROM show s
    JOIN show_country sc ON s.show_id = sc.show_id
    JOIN country c ON sc.country_id = c.country_id
    WHERE c.country_name = p_country;
END;
$$;
