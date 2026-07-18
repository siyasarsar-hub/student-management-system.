# Student Management System

## Project Description
The Student Management System is a simple Python project that allows users to manage student records. It supports adding, searching, updating, and removing students. The project also includes unit testing and GitHub Actions for automated testing.

---

## Project Structure

```
student-management-system/
│── Students.py
│── test_students.py
│── requirements.txt
│── README.md
│── .github/
│   └── workflows/
│       └── python.yml
```

---

## Features

- Add Student
- Search Student
- Update Student
- Remove Student

---

## Project Setup

1. Clone the repository

```bash
git clone https://github.com/siyasarsar-hub/student-management-system.git
```

2. Open the project folder

```bash
cd student-management-system
```

3. Install the required package

```bash
pip install pytest
```

4. Run the tests

```bash
pytest
```

---

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial Commit"

git checkout -b feature-student-search

git add .
git commit -m "Implemented student search functionality"

git push -u origin feature-student-search

git add .
git commit -m "Added GitHub Actions workflow"

git push

git checkout master
git merge feature-student-search
```

---

## GitHub Actions Workflow

The GitHub Actions workflow is configured to run automatically on every **push** and **pull request**.

The workflow:
- Checks out the repository
- Sets up Python
- Installs pytest
- Runs all unit tests automatically

---

## Testing

The project contains unit tests for:

- Add Student
- Search Student
- Update Student
- Remove Student

All tests pass successfully using **pytest**.
