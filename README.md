# Harshit Tiwari - 24BCS10277

**Notion Link:** [Software Engineering Intern Assignment (Backend)](https://www.notion.so/Software-Engineering-Intern-Assignment-Backend-2cb993de712f808fa4f0f021f9f05605?source=copy_link)

## Software Engineering Intern Assignment (Backend)

> **Goal:** Migrate Google Sheets–driven workflows to a PostgreSQL/NeonDB infrastructure with automated ETL, Google App Script, and interactive dashboards.

---

## 📌 Implementation Summary

This project successfully implements a complete backend infrastructure migration and automation workflow as per the assignment requirements.

### 1. ETL Pipeline & Data Migration (`etl/`)
- **Source**: Migrated raw data from `netflix_shows` table.
- **Transformation Logic**: 
  - Standardized duration into value and unit.
  - Split comma-separated fields (Directos, Cast, Countries, Genres) into atomic entities.
  - Implemented lookup tables for `Rating` and `Show Type`.
- **Normalization**: Transformed flat data into a 3NF schema involving `show`, `person`, `country`, `genre`, and respective junction tables.
- **Robustness**: The pipeline (`etl_netflix.py`) is idempotent and handles duplicates gracefully.

### 2. SQL Development & Optimization (`sql/`)
- **Analytics**: Developed analytical queries to derive insights (e.g., content distribution by country, average duration).
- **Views**: Created materialized-style views for easy reporting (`vw_show_genre_type`, `vw_show_people`).
- **Stored Procedures**: Implemented PL/pgSQL functions for dynamic data retrieval (`get_titles_by_genre`, `get_titles_by_country`).
- **Performance**: Validated query performance using `EXPLAIN ANALYZE` and optimized execution plans by adding strategic indexes on `release_year` and foreign key columns.

### 3. Google App Script Automation (`app/`)
- **Architecture**: Google Sheets $\rightarrow$ Google App Script $\rightarrow$ Python FastAPI $\rightarrow$ NeonDB.
- **Python Backend**: Built a FastAPI service (`app/main.py`) to handle reliable data insertion into the `student` table.
- **Google App Script**:
  - Implemented `onEdit` triggers for real-time validation within Google Sheets.
  - Added visual feedback (PENDING/SUCCESS/ERROR) directly in the sheet cells.
  - Configured email notifications for failed validations.
  - Deployed a Web App for JSON data export.

### 📂 Project Structure

```
e:\HARSHIT\SCALER INTERN BACKEND\
├── etl/
│   ├── etl_netflix.py      # Main ETL script
│   ├── setup_db.py         # Database setup utility
│   └── requirements.txt    # ETL dependencies
├── sql/
│   ├── new_schema.sql      # Normalized schema definition
│   ├── queries.sql         # Analytical queries
│   ├── views.sql           # Reporting views
│   ├── procedures.sql      # Stored procedures
│   └── optimization.sql    # Index definitions
├── app/
│   ├── main.py             # FastAPI backend for automation
│   ├── db.py               # Database connection module
│   └── create_table.py     # Setup script for student table
└── README.md               # Project documentation
```

### ✅ Deliverables Status
- [x] ETL Pipeline Setup
- [x] Database Schema Design
- [x] SQL Queries & Optimization
- [x] Automation Workflow (Sheets to DB)
- [x] Documentation
