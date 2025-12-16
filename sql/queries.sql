-- 1. Count of Movies vs TV Shows
SELECT
    st.type_name,
    COUNT(*) AS total_titles
FROM show s
JOIN show_type st ON s.type_id = st.type_id
GROUP BY st.type_name;

-- 2. Top 10 Genres by Number of Titles
SELECT
    g.genre_name,
    COUNT(*) AS total_titles
FROM show_genre sg
JOIN genre g ON sg.genre_id = g.genre_id
GROUP BY g.genre_name
ORDER BY total_titles DESC
LIMIT 10;

-- 3. Number of Titles per Country
SELECT
    c.country_name,
    COUNT(*) AS total_titles
FROM show_country sc
JOIN country c ON sc.country_id = c.country_id
GROUP BY c.country_name
ORDER BY total_titles DESC;

-- 4. Average Movie Duration (Minutes)
SELECT
    ROUND(AVG(duration_value), 2) AS avg_movie_duration_min
FROM show s
JOIN show_type st ON s.type_id = st.type_id
WHERE st.type_name = 'Movie'
  AND duration_unit = 'min';

-- 5. Shows Released per Year
SELECT
    release_year,
    COUNT(*) AS total_titles
FROM show
GROUP BY release_year
ORDER BY release_year DESC;

-- 6. Duplicate Title Detection
SELECT
    title,
    COUNT(*) AS occurrences
FROM show
GROUP BY title
HAVING COUNT(*) > 1;
