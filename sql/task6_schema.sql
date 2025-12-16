CREATE TABLE IF NOT EXISTS student (
    student_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    year INT CHECK (year BETWEEN 1 AND 5),
    department TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
