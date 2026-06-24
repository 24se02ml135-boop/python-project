# 🎓 Student Data Organizer

A simple command-line application built in Python that allows users to manage student records efficiently. This project demonstrates the use of Python fundamentals including lists, dictionaries, loops, and the `match-case` statement.

---

## 📋 Features

- **Add Student** — Enter and store a student's details including ID, name, age, grade, date of birth, and subjects.
- **Display All Students** — View a formatted list of all registered students.
- **Update Student Information** — Modify an existing student's name, age, or grade by their ID.
- **Delete Student** — Remove a student record using their ID.
- **Display Subjects Offered** — View all unique subjects across all students.
- **Exit** — Gracefully exit the program.

---

## 🚀 How to Run

Make sure you have **Python 3.10 or later** installed (required for the `match-case` statement).

```bash
python project3.py
```

---

## 🖥️ Sample Output

```
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 1

Enter student details:
Student ID: 101
Name: Alice
Age: 20
Grade: B+
Date of Birth (YYYY-MM-DD): 2002-05-14
Subjects (comma-separated): Math, Science, English

Student added successfully!
```

---

## 📁 Project Structure

```
project3/
│
└── project3.py       # Main Python script
```

---

## 🧠 Concepts Used

| Concept | Usage |
|---|---|
| Lists | Storing student records |
| Dictionaries | Representing each student's data |
| `match-case` | Menu-based navigation (Python 3.10+) |
| `while` loop | Keeps the menu running until exit |
| `for` loop | Iterating through student records |
| String methods | Parsing comma-separated subjects |
| `input()` / `int()` | Collecting and converting user input |

---

## 🐛 Known Bug & Fix

In the **Display All Students** section (Case 2), the original code has a nested `print()` inside another `print()`:

```python
# ❌ Buggy code — prints "None" after each student
print(
    print(f"Student ID: {s['ID']} | Name: {s['Name']} ...")
)
```

This causes `None` to appear after each student record because `print()` returns `None`.

**Fix:** Remove the outer `print()`:

```python
# ✅ Corrected code
print(f"Student ID: {s['ID']} | "
      f"Name: {s['Name']} | "
      f"Age: {s['Age']} | "
      f"Grade: {s['Grade']} | "
      f"Subjects: {s['Subjects']}")
```

---

## ⚙️ Requirements

- Python 3.10+
- No external libraries required

---

## 👤 Author

Developed as a beginner Python project to practice data management using core Python concepts.
