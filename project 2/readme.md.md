# ⭐ Pattern Generator and Number Analyzer

A simple interactive command-line application built in Python that lets users generate star patterns and analyze ranges of numbers. This project demonstrates Python fundamentals including loops, `match-case`, and basic arithmetic.

---

## 📋 Features

- **Generate a Pattern** — Prints an increasing triangle of `*` characters (rows 1 through 5).
- **Analyze a Range of Numbers** — For a user-defined range, labels each number as Even or Odd and prints the total sum.
- **Exit** — Cleanly exits the program with a goodbye message.

---

## 🚀 How to Run

Make sure you have **Python 3.10 or later** installed (required for the `match-case` statement).

```bash
python python2.py
```

---

## 🖥️ Sample Output

```
Welcome to the Pattern Generator and Number Analyzer

Select an option:
1. Generate a pattern
2. Analyze a range of numbers
3. Exit
Select your option: 1
*
**
***
****
*****

Select an option:
1. Generate a pattern
2. Analyze a range of numbers
3. Exit
Select your option: 2
Enter the start of the range: 10
Enter the end of the range: 15
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Sum of all numbers from 10 to 15 is: 75

Select an option:
1. Generate a pattern
2. Analyze a range of numbers
3. Exit
Select your option: 3

Exiting the program. Goodbye!
```

---

## 📁 Project Structure

```
project2/
│
└── python2.py       # Main Python script
```

---

## 🧠 Concepts Used

| Concept | Usage |
|---|---|
| `match-case` | Menu-based navigation (Python 3.10+) |
| `while` loop | Keeps the menu running until exit |
| Nested `for` loops | Generating the star triangle pattern |
| Modulo operator `%` | Checking even/odd numbers |
| Accumulator variable | Summing numbers in a range |
| `input()` / `int()` | Collecting and converting user input |

---

## ⚙️ Requirements

- Python 3.10+
- No external libraries required

---

## 👤 Author

Developed as a beginner Python project to practice loops, pattern generation, and menu-driven programming using core Python concepts.
