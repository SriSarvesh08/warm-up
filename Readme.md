# Python Warmup

## Project Overview

This repository documents my Python warmup tasks completed over two days. The tasks cover Python fundamentals, functions, file handling, exception handling, object-oriented programming, CSV/JSON processing, Pandas, and Git version control.

## Tech Stack & Tools

- **Language:** Python
- **Data Processing:** Pandas
- **Data Formats:** CSV, JSON
- **Version Control:** Git and GitHub
- **IDE:** Visual Studio Code
- **Environment:** Python virtual environment (`venv`)

## Day 1 — Python Fundamentals (T01–T05)

| Task | Description | Intern Notes / Blockers |
|---|---|---|
| T01 | Python environment setup and Git basics | Verified the Python installation, set up the virtual environment, and practiced basic Git commands. Python 3.12.0 was already installed. No major blockers. |
| T02 | Hello World and initial project setup | Created and executed the initial Python program. Verified the development environment. |
| T03 | Python basics | Created `day1/basics.py` with 10 examples covering fundamental Python concepts. |
| T04 | Python exercises | Created `day1/exercises.py` with 8 functions and tested their outputs. |
| T05 | Word count program | Created `day1/word_count.py` to count word frequencies and display the most frequent words. |

### Day 1 Key Learnings

- Python syntax, variables, and basic data types
- Conditional statements and loops
- Functions and reusable code
- String processing and word-frequency counting
- Virtual environments and basic Git workflow

## Day 2 — Data Processing, OOP & Git (T06–T10)

| Task | Description | Intern Notes / Blockers |
|---|---|---|
| T06 | CSV to JSON conversion | Processed student data from a CSV file and generated a JSON summary. |
| T07 | Error handling | Practiced exception handling and managed project dependencies using `requirements.txt`. |
| T08 | Object-oriented programming | Implemented a `BankAccount` class with validation and tested account operations. No major blockers. |
| T09 | Pandas CSV analysis | Used Pandas to clean student data and generate summary outputs. |
| T10 | Git workflow practice | Practiced branches, merging, conflict resolution, stash, restore, and revert. Captured screenshots of the Git history and pushed them to GitHub. |

### Day 2 Key Learnings

- Reading and writing CSV and JSON files
- Exception handling and dependency management
- Classes, objects, and input validation
- Data cleaning and analysis using Pandas
- Git branching, merging, conflict resolution, and commit history
- Safely managing temporary changes with `git stash` and `git restore`
- Undoing a commit's changes using `git revert`

## Project Structure

```text
python-warmup/
├── day1/
│   ├── basics.py
│   ├── exercises.py
│   └── word_count.py
├── day2/
│   ├── screenshots/
│   │   ├── T10-merge-conflict.png
│   │   └── T10.git-graph.png
│   ├── cleaned_students.csv
│   └── summary.json
├── hello.py
├── .gitignore
├── README.md
└── requirements.txt
```

*Note: The structure above summarizes the main project files. Actual files may vary depending on the current repository state.*

## Git Workflow Practiced

- Created feature branches for isolated changes.
- Merged branches into `main`.
- Resolved a merge conflict and committed the resolution.
- Used `git stash` and `git stash pop` to temporarily save and restore changes.
- Used `git restore` to discard an unwanted working-tree change.
- Used `git revert` to undo a previous commit through a new commit.
- Reviewed commit history using `git log --oneline --graph --all`.
- Committed and pushed Git practice screenshots to GitHub.

## Overall Learning Outcomes

By completing Day 1 and Day 2, I practiced Python programming fundamentals, data processing, object-oriented programming, error handling, and collaborative version-control workflows.

**Status:** Day 1 and Day 2 practice tasks completed.
