# Refined planning

*Date:* 2025-11-04

*Time:* 09:17

---

Spent the morning going over my initial plan and updating the goals. In light of some recent reading I had the idea to try and focus the direction of my intial project practice to a more specialised area of IT. I don't know what the future holds for me in regards to my industry placement and overall career prospects but the idea of data engineering seems somewhat future proof with the way the IT landscape is evolving. May not be perfect but I'm feeling like specialising in something is the play here and the skills and transferrable. I removed languge/gym from the schedule as I'll manage them on my own. This is kept programming focused. Here is the updated list:

# Peter’s Daily Coding & Growth Checklist (Python + Data Engineering Pivot)

## Concept Study (30–60 min)  
Pick one topic to research, read docs/tutorials, and build your mental map.

- **Python basics** — functions, classes, modules, venv  
  *Start*: Real Python tutorials, Python docs  
- **Unix CLI** — navigation, pipes, grep  
  *Start*: *The Linux Command Line* book  
- **Data structures** — lists, stacks, queues, hash maps, trees, graphs  
  *Start*: LeetCode DS tag, GeeksforGeeks  
- **Big‑O complexity** — runtime analysis  
  *Start*: bigocheatsheet.com  
- **OOP & SOLID in Python** — design principles  
  *Start*: refactoring.guru, Real Python  
- **Unit testing** — pytest basics  
  *Start*: pytest docs, Real Python  
- **SQL basics** — SELECT, JOIN, GROUP BY  
  *Start*: sqlzoo.net, LeetCode SQL  
- **Relational modeling** — PK/FK, ER diagrams  
  *Start*: dbdiagram.io, GeeksforGeeks keys tutorial  
- **ETL basics** — Extract/Transform/Load, batch vs streaming  
  *Start*: DataTalksClub YouTube  
- **pandas basics** — load/filter/group CSVs  
  *Start*: pandas docs, Kaggle exercises  
- **System design basics** — client/server/DB, scaling, APIs  
  *Start*: System Design Primer GitHub, ByteByteGo YouTube  
- **Logging & data quality checks** — why logs matter, schema/row validation  
  *Start*: Python logging docs, Great Expectations intro  
- **Scheduling basics** — cron, Python `schedule` library  
  *Start*: cron tutorials  
- **Cloud basics** — what S3 (file storage), Postgres (DB), RDS (managed DB) are  
  *Start*: AWS docs intros  

---

## Coding Challenge (30–60 min)  
Rotate through these practice modes.

- Algorithm problem (LeetCode easy/medium)  
- SQL query problem (LeetCode SQL, HackerRank SQL, sqlzoo.net)  
- pandas cleanup/aggregation (Kaggle pandas exercises)  
- Refactor with tests — take an old LeetCode solution, rewrite cleaner, add pytest test  
- TDD mini — pick a tiny function (e.g., reverse a string), write failing test first, then implement  

---

## Project Work (60–90 min)  
Suggested pathway for your Russian Vocabulary Trainer. Each step = a checkpoint you can build toward. Tools listed; **bold = industry‑standard**.

1. **Project skeleton** — repo, venv, requirements, one test  
   Tools: **git**, Python, **pytest**  
2. **Data model** — decide entities (Word, Review, maybe User)  
   Tools: Python classes/dataclasses  
3. **CLI** — add/list/review commands  
   Tools: argparse (built‑in), Click (popular)  
4. **Persistence** — move from in‑memory to DB  
   Tools: **SQLite** (local), **Postgres** (industry), SQLAlchemy (ORM)  
5. **Core logic** — implement spaced repetition rules  
   Tools: Python functions, pytest  
6. **Import/export** — handle CSVs for interoperability  
   Tools: csv module, **pandas** (industry)  
7. **UI** — add a user interface  
   Tools: Streamlit (browser‑based, quick), Tkinter/PyQt (desktop window)  
8. **Logging & checks** — add logs and data validation  
   Tools: Python logging, **Great Expectations** (industry)  
9. **Scheduling** — automate daily review prep  
   Tools: cron (simple), Python `schedule`, **Airflow** (industry)  
10. **Dockerize app** — package app + DB for consistent runs  
    Tools: **Docker**, **docker‑compose**  
11. **Optional cloud** — try cloud storage/DB  
    Tools: **AWS S3**, **AWS RDS (Postgres)**, boto3  
12. **Polish** — README, diagram, demo  
    Tools: Markdown, draw.io/Excalidraw, screen recording  

---

## Career Prep (10–30 min)  
Concrete, repeatable actions to build interview readiness.

- **Technical interview practice**  
  - Solve 1 coding problem (LeetCode/HackerRank)  
  - Solve 1 SQL query problem  
  - Explain your solution out loud (practice communication)  

- **System design practice**  
  - Pick a small system (your vocab trainer, a URL shortener)  
  - Sketch components (UI, logic, DB)  
  - Practice explaining trade‑offs (SQL vs NoSQL, caching, scaling)  

- **Behavioral interview practice**  
  - Use the **STAR method** (Situation, Task, Action, Result)  
  - Example: “Tell me about a time you solved a difficult problem.” Use STAR to structure your answer  
  - Practice 1 question per session (resources: Interviewing.io blog, Big Interview)  

- **Portfolio prep**  
  - Update README/docs for your project  
  - Write 1–2 bullet points describing what you built and what you learned  

- **Industry awareness**  
  - Read 1 job description for data engineer/backend roles  
  - Note recurring skills/tools (SQL, Python, Docker, Airflow)  
  - Add those to your study/practice focus  

---

# Tool Glossary (Quick Reference)

- **argparse** — built‑in Python library for parsing command‑line arguments  
- **Click** — third‑party Python library for building nicer CLIs  
- **SQLite** — lightweight, file‑based relational database  
- **Postgres (PostgreSQL)** — industry‑standard relational database, scalable and feature‑rich  
- **SQLAlchemy** — Python ORM (object‑relational mapper) to interact with databases using Python objects  
- **pytest** — Python testing framework  
- **pandas** — Python library for working with tabular data (CSV, Excel, SQL)  
- **Streamlit** — Python library to quickly build browser‑based UIs for data apps  
- **Tkinter** — built‑in Python library for desktop GUIs  
- **PyQt** — Python bindings for Qt, a powerful GUI framework  
- **Python logging** — standard library for recording logs  
- **Great Expectations** — framework for automated data validation and quality checks  
- **cron** — Unix scheduler for running tasks at set times  
- **schedule (Python)** — lightweight Python library for scheduling jobs  
- **Airflow** — industry‑standard workflow orchestrator for managing complex data pipelines  
- **Docker** — containerization tool to package apps and dependencies consistently  
- **docker‑compose** — tool to define and run multi‑container apps (e.g., app + DB)  
- **AWS S3** — cloud object storage service (files, backups, datasets)  
- **AWS RDS (Postgres)** — managed relational database service  
- **boto3** — AWS SDK for Python to interact with services like S3 and RDS  
- **Markdown** — lightweight markup language for README/docs  
- **draw.io / Excalidraw** — diagramming tools for architecture sketches  
- **PyInstaller** — tool to package Python apps into standalone executables
