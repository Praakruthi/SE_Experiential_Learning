# Software Engineering – Experiential Learning

A collection of laboratory exercises, assignments, and practical implementations completed as part of the **Software Engineering – Experiential Learning** course at **PES University**.

This repository documents the application of software engineering principles across the software development lifecycle, including requirements engineering, Agile project management, software architecture, AI-assisted development, static code analysis, and software testing.

## Student Details

| Detail | Information |
|---|---|
| Name | Praakruthi PS |
| Program | B.Tech – Computer Science and Engineering |
| Section | 5F |
| University | PES University |
| Course | Software Engineering – Experiential Learning |

---

## Laboratory Work

### Lab 1 – Requirements Engineering & UML Use-Case Modelling

**Project: Hospital Bed & ICU Allocation Dashboard**

This lab focuses on understanding a healthcare problem, identifying system requirements, and modelling the interactions between users and the proposed system.

**Key activities:**
- Identifying stakeholders and system actors.
- Defining functional and non-functional requirements.
- Prioritizing requirements based on importance.
- Establishing acceptance criteria and rationales.
- Creating a UML Use-Case Diagram.
- Preparing detailed Use-Case Flow Specifications.

**Problem Statement:** #20 – Healthcare & Telemedicine

**Deliverables:** Requirements Table, Use-Case Diagram, and Use-Case Flow Specification.

### Lab 2 – Agile Backlog Creation & Sprint Simulation

**Project: Hospital Bed & ICU Allocation Dashboard**

This lab translates the requirements identified in Lab 1 into an Agile development plan using **Jira**.

**Key activities:**
- Creating Epics and User Stories.
- Prioritizing user stories.
- Estimating effort using Fibonacci-based Story Points.
- Creating and organizing the Product Backlog.
- Planning and simulating two development sprints.
- Tracking sprint progress through To Do, In Progress, and Done.
- Analysing sprint performance using Burndown Charts.

**Sprint Summary:**

| Sprint | Planned Story Points | Status |
|---|---:|---|
| Sprint 1 | 21 | Completed |
| Sprint 2 | 13 | Completed |
| **Total** | **34** | **Completed** |

**Deliverables:** Agile Backlog, Sprint Planning and Progress Evidence, Burndown Charts, and Sprint Reflection.

### Lab 3 – Component Modelling & Architectural Pattern Selection

**Project: Hospital Bed & ICU Allocation Dashboard**

This lab focuses on designing the software architecture and identifying the major components required to support the proposed healthcare system.

**Key activities:**
- Creating a UML Component Diagram.
- Identifying the major system components and their interactions.
- Selecting and justifying a suitable architectural pattern.
- Organizing the system using a Layered Architecture.
- Identifying Presentation, Application, and Data layers.
- Understanding authentication, authorization, and real-time communication.

**Selected Architecture:** Layered Architecture.

**Major Components:**
- Real-Time Dashboard
- Authentication & Authorization Service
- Triage & Prioritization Service
- Bed Management & Allocation Service
- Transfer & Ambulance Coordination Service
- Real-Time Notification Service
- Hospital Database

**Deliverables:** UML Component Diagram and Architecture Selection & Justification Document.

### Lab 4 – VibeCoding: AI-Assisted Software Development

**Project: Scenario 19 – Battleship vs AI**

This lab explores AI-assisted software development using **GitHub Copilot** to analyse, debug, and enhance an existing terminal-based Python Battleship game.

The objective was to understand the existing implementation, identify defects, and incrementally improve the application's functionality with AI assistance.

**Key tasks:**

1. **Consistent Coordinate Handling:** Identified and fixed coordinate inconsistencies between user input, ship placement, player shots, and AI shots.

2. **Complete Fleet & Win Logic:** Implemented multiple-ship support, individual ship damage tracking, sinking detection, repeated-shot prevention, and fleet completion logic.

3. **Improved AI:** Enhanced AI targeting by prioritizing nearby untried cells after a hit and preventing duplicate shots.

4. **Shot-Level Feedback:** Improved HIT, MISS, and SUNK feedback to ensure that results are displayed correctly for actual shots.

**Technologies:** Python, GitHub Copilot, VS Code, Git, and GitHub.

**Deliverables:** Updated Battleship implementation, before-and-after gameplay recordings, and complete AI chat history.

### Lab 5 – Static Code Analysis

**Project: Music Catalog and Playlist Manager**

This lab focuses on improving software quality, maintainability, security, and coding standards through static code analysis.

The assigned Python application was analysed using three static analysis tools.

**Tools Used:**

- **Pylint:** Identifying code quality, naming convention, documentation, and maintainability issues.
- **Bandit:** Identifying potentially insecure coding practices and security vulnerabilities.
- **Flake8:** Detecting formatting violations and Python style inconsistencies.

**Key activities:**
- Analysing the original source code.
- Running Pylint, Bandit, and Flake8.
- Comparing before-and-after analysis reports.
- Identifying and documenting code quality and security issues.
- Applying fixes to improve code quality and security.
- Verifying the changes through repeated static analysis.

**Deliverables:**
- Updated `music_catalog.py`.
- `issues.md` documenting identified issues and proposed fixes.
- Before-and-after Pylint reports.
- Before-and-after Bandit reports.
- Before-and-after Flake8 reports.

### Lab 6 – Code and Branch Coverage Analysis

**Project: Parking Fee Management Application**

This lab focuses on measuring and improving software test coverage using Python's `coverage` library and `pytest`.

The assigned parking fee application contains functionality for calculating parking fees, assigning parking slots, and determining monthly pass prices.

**Key activities:**
- Understanding code coverage and branch coverage.
- Analysing the existing application and starter test cases.
- Writing additional test cases to exercise uncovered statements.
- Testing conditional branches and edge cases.
- Generating and interpreting coverage reports.
- Maintaining separate test suites for code coverage and branch coverage.

**Test Files:**

| File | Purpose |
|---|---|
| `CodeCoverageTest_19_application.py` | Test cases for code coverage |
| `BranchCoverageTest_19_application.py` | Test cases for branch coverage |

**Verified Coverage Results:**

| Metric | Result |
|---|---:|
| Code Coverage | 100% |
| Branch Coverage | 100% |
| Code Coverage Tests | 12 passed |
| Branch Coverage Tests | 17 passed |

**Deliverables:** Separate code and branch coverage test files, terminal output screenshots, coverage reports, and separate Git commits for both activities.

---

## Repository Structure

```text
SE_Experiential_Learning/
│
├── Lab1/
│   ├── Requirements_Table.docx
│   ├── Use_Case_Diagram.pdf
│   └── Use_Case_Flow.docx
│
├── Lab2/
│   ├── EPICS AND USER STORIES
│   ├── Sprint Planning and Progress Evidence
│   ├── Sprint Burndown Charts
│   └── Lab_2_Agile_Backlog_and_Sprint_Simulation.pdf
│
├── Lab3/
│   ├── Component_diagram.pdf
│   └── Lab_3_Architecture_Justification.docx
│
├── Lab4/
│   ├── 19_battleship/
│   │   ├── main.py
│   │   ├── game.py
│   │   ├── board.py
│   │   ├── ai.py
│   │   └── README.md
│   ├── LAB4_BEFORE.mp4
│   ├── LAB4_AFTER.mp4
│   └── Copilot_Chat_History.pdf
│
├── Lab5/
│   ├── Deliverables/
│   │   ├── pylint_before.txt
│   │   ├── pylint_after.txt
│   │   ├── bandit_before.txt
│   │   ├── bandit_after.txt
│   │   ├── flake8_before.txt
│   │   └── flake8_after.txt
│   │
│   └── L5_19_music_catalog-main/
│       ├── music_catalog.py
│       ├── issues.md
│       └── README.md
│
├── Lab6/
│   ├── parking_fee.py
│   ├── test_parking_fee.py
│   ├── CodeCoverageTest_19_application.py
│   ├── BranchCoverageTest_19_application.py
│   ├── code_coverage_screenshot.png
│   ├── code_coverage_report.png
│   ├── branch_coverage_tests.png
│   ├── branch_coverage_report.png
│   └── README.md
│
├── .gitignore
└── README.md
```

---

## Tools & Technologies

| Category | Tools / Technologies |
|---|---|
| Programming Language | Python |
| IDE | Visual Studio Code |
| Version Control | Git, GitHub |
| Agile Project Management | Jira |
| Software Modelling | UML |
| AI-Assisted Development | GitHub Copilot |
| Static Code Analysis | Pylint, Bandit, Flake8 |
| Software Testing | pytest, coverage.py |

---

## Learning Outcomes

Through these laboratory exercises, I gained practical experience in:

- Analysing problem statements and translating them into software requirements.
- Preparing functional and non-functional requirements.
- Modelling software systems using UML diagrams.
- Applying Agile methodologies through backlog creation and sprint planning.
- Understanding software architecture and component interactions.
- Debugging and improving existing applications.
- Using AI coding assistants responsibly during software development.
- Identifying security vulnerabilities and code quality issues through static analysis.
- Designing test cases and measuring code and branch coverage.
- Managing project files, changes, and deliverables using Git and GitHub.

---

## Repository Purpose

This repository serves as a record of my practical work and learning throughout the Software Engineering – Experiential Learning course.

Each laboratory demonstrates a different aspect of software engineering, progressing from requirements analysis and system design to implementation, code quality improvement, and software testing.

---

**Author:** Praakruthi PS  
**Course:** Software Engineering – Experiential Learning  
**University:** PES University  
**Program:** B.Tech – Computer Science and Engineering