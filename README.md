
# IT Operations Personal Hub

A cross-platform desktop application for IT workflow management, knowledge documentation, automation planning, and operational reporting.

## Overview

IT Operations Personal Hub is an independent portfolio project built to help IT professionals organize their daily activities and improve workflow efficiency.

The application combines task management, technical knowledge documentation, learning progress, and reporting in one desktop workspace.

## Key Features

### 1. Work Tracker
- Create, update, and complete tasks
- Track ticket references and task priorities
- Set follow-up dates and reminders
- Identify overdue tasks

### 2. Issue Knowledge Base
- Document technical issues and solutions
- Categorize troubleshooting records
- Search previously documented solutions

### 3. Automation Ideas
- Record repetitive IT processes
- Track potential automation opportunities
- Document PowerShell automation concepts

### 4. Learning Tracker
- Track technical learning activities
- Record study hours
- Monitor progress across IT skill areas

### 5. Career Tracker
- Define professional development goals
- Track certifications and projects
- Monitor career milestones

### 6. Reporting Dashboard
- Summarize completed and outstanding tasks
- Track knowledge base contributions
- Generate weekly activity reports

## Technology Stack

- Python 3.13
- PySide6 (Qt for Python)
- SQLite
- Git and GitHub

## Project Structure

```text
IT-Operations-Personal-Hub/
├── src/
│   └── it_operations_hub/
│       ├── __init__.py
│       └── main.py
├── .gitignore
└── README.md
```

## Getting Started

### macOS

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install PySide6
python src/it_operations_hub/main.py
```

## Development Roadmap

- [x] Day 1: Development environment and initial application
- [ ] Day 2: SQLite database and Work Tracker
- [ ] Day 3: Follow-up reminder system
- [ ] Day 4: Issue Knowledge Base
- [ ] Day 5: Automation Ideas and Learning Tracker
- [ ] Day 6: Dashboard and reporting
- [ ] Day 7: Testing, packaging, and documentation

## Privacy and Security

This is an independent personal project.

All demonstration data is fictional. No confidential employer information, real employee records, or internal company tickets are included.

The application is designed to store user data locally using SQLite.

## Project Status

Under active development.
```
