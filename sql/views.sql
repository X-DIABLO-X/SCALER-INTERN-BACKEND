-- View 1: Show + Genre + Type (Reporting View)
CREATE OR REPLACE VIEW vw_show_genre_type AS
SELECT
    s.show_id,
    s.title,
    st.type_name,
    g.genre_name,
    s.release_year
FROM show s
JOIN show_type st ON s.type_id = st.type_id
JOIN show_genre sg ON s.show_id = sg.show_id
JOIN genre g ON sg.genre_id = g.genre_id;

-- View 2: Show + Country Distribution
CREATE OR REPLACE VIEW vw_show_country AS
SELECT
    s.show_id,
    s.title,
    c.country_name
FROM show s
JOIN show_country sc ON s.show_id = sc.show_id
JOIN country c ON sc.country_id = c.country_id;

-- View 3: Cast & Crew per Show
CREATE OR REPLACE VIEW vw_show_people AS
SELECT
    s.title,
    p.full_name,
    sp.role
FROM show s
JOIN show_person sp ON s.show_id = sp.show_id
JOIN person p ON sp.person_id = p.person_id;
