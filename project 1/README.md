<div align="center">

# -- ! User Data Collector ! --
### *Interactive Console-Based Personal Information & Variable Type Explorer*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Variables](https://img.shields.io/badge/Variables-int%20%7C%20float%20%7C%20str-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Math](https://img.shields.io/badge/Math-Basic%20Arithmetic-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Understanding data types is the first step to mastering any programming language."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📥 Input Collection](#-input-collection)
- [🔍 Variable Inspection](#-variable-inspection)
- [🧮 Data Processing](#-data-processing)
- [📊 User Summary](#-user-summary)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Sample Output](#-sample-output)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **User Data Collector** is a beginner-friendly, interactive Python console application that demonstrates core programming fundamentals such as **data types**, **type casting**, **user input handling**, **memory address inspection**, and **basic arithmetic**. The program collects personal information from the user and displays it along with each variable's type and memory address.

This project is designed to:
- Build a strong foundation in Python's core **data types** (`str`, `int`, `float`)
- Practice **type conversion** (`int()`, `float()`) with user input
- Understand how Python manages variables in **memory** using `id()`
- Apply simple **arithmetic operations** for real-world calculations
- Present a clean, formatted **user summary** in the console

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive program to collect, inspect, and summarize user data.

You are building a simple data entry utility for students learning Python. The program must prompt the user for personal details, store them in appropriately typed variables, inspect each variable's type and memory address, perform a simple calculation, and display a formatted summary.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Data Collection | Console Input | Collects name, age, height, and favourite number |
| Type Inspection | Metadata Display | Shows `type()` and `id()` for each variable |
| Birth Year Calculation | Arithmetic | Approximates birth year from entered age |
| User Summary | Console Output | Prints a clean, formatted personal summary |

The goal is to demonstrate **fundamental Python data handling skills** through a simple, linear interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 📝 **Multi-type Input** | Collects `str`, `int`, and `float` values from the user |
| 🔍 **Type Inspection** | Displays `type()` for every variable to reinforce type awareness |
| 🧠 **Memory Address** | Uses `id()` to show each variable's memory location |
| 🧮 **Birth Year Calc** | Computes approximate birth year using simple subtraction |
| 🖥️ **CLI Interface** | Simple, clean sequential console flow |
| 📋 **User Summary** | Presents all collected data in a formatted summary block |

---

## 🏗️ Project Structure

```
📦 user-data-collector/
│
├── 📄 project_1.py          ← Main Python script (entry point)
│
└── 📄 README.md             ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Welcome Message           │  ← Greets user and introduces the program
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Collect User Inputs       │  ← name (str), age (int), height (float), fav_number (int)
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Inspect Variable Metadata │  ← Print type() and id() for each variable
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Calculate Birth Year      │  ← birth_year = 2025 - age
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│   Print User Summary        │  ← Display all collected data in formatted block
└────────────┬────────────────┘
             │
             ▼
      Exit Message ✅
```

---

## 📥 Input Collection

### 📝 1. What is User Input in Python?

Python's built-in `input()` function pauses the program and waits for the user to type a value. By default, all input is returned as a **string**, so type conversion is needed for numeric values.

---

### 🗃️ 2. Variables Collected — Overview

| Variable | Data Type | Conversion | Example Value |
|----------|-----------|------------|---------------|
| `name` | `str` | None (direct) | `"Aatha"` |
| `age` | `int` | `int(input(...))` | `20` |
| `height` | `float` | `float(input(...))` | `5.6` |
| `fav_number` | `int` | `int(input(...))` | `29` |

---

### 💻 3. Input Code

```python
name       = input("Please enter your name here: ")
age        = int(input("Please enter your age here: "))
height     = float(input("Please enter your height here: "))
fav_number = int(input("Please enter your favourite number here: "))
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| `input()` | Reads user input from the console as a string |
| `int()` | Converts string to integer for whole numbers |
| `float()` | Converts string to decimal/floating-point number |

---

## 🔍 Variable Inspection

### 🧠 4. Type and Memory Address Display

> After collecting inputs, each variable's **data type** and **memory address** is printed.

**Logic:**
```python
print("name:", name, "Type:", type(name), "Memory Address:", id(name))
print("age:", age, "Type:", type(age), "Memory Address:", id(age))
print("height:", height, "Type:", type(height), "Memory Address:", id(height))
print("Favourite number:", fav_number, "Type:", type(fav_number), "Memory Address:", id(fav_number))
```

**Key Concepts Used:**

| Function | Purpose |
|----------|---------|
| `type()` | Returns the data type of a variable (e.g., `<class 'str'>`) |
| `id()` | Returns the unique memory address of the variable |

---

## 🧮 Data Processing

### ➗ 5. Birth Year Calculation

> Approximates the user's birth year based on the age they entered.

**Logic:**
```python
current_year = 2025
birth_year = current_year - age
print("Your birth year is here based on approximate:", birth_year)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| Integer Variable | `current_year` stores a fixed reference year |
| Arithmetic `-` | Subtracts `age` from `current_year` |
| Result Storage | Result saved to `birth_year` for reuse in summary |

---

## 📊 User Summary

### 📋 6. Final Summary Output

> All collected and computed data is printed in a clean summary block.

**Logic:**
```python
print("\nUSER SUMMARY")
print("Hello", name)
print("you are", age, "years old")
print("your height is", height)
print("your favourite number is", fav_number)
print("your approximate birth year is", birth_year)
print("-----------------------------")
```

**Sample Summary Output:**
```
USER SUMMARY
Hello Aatha
you are 20 years old
your height is 5.6
your favourite number is 29
your approximate birth year is 2005
-----------------------------
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 🖨️ **print()** | Built-in | Console output |
| ⌨️ **input()** | Built-in | Reading user input |
| 🔢 **int() / float()** | Built-in | Type conversion / casting |
| 🔍 **type()** | Built-in | Runtime type inspection |
| 🧠 **id()** | Built-in | Memory address retrieval |
| ➕ **Arithmetic `-`** | Built-in | Birth year calculation |

---

## 📈 Sample Output

The following is a real output captured from running the program:

```
hello we are here collect the some data
welcome to this side

Please enter your name here: Aatha
Please enter your age here: 20
Please enter your height here: 5.6
Please enter your favourite number here: 29

Thank you for giving the information:

name: Aatha  Type: <class 'str'>   Memory Address: 1489332197088
age: 20      Type: <class 'int'>   Memory Address: 140711350355672
height: 5.6  Type: <class 'float'> Memory Address: 1489331258672
Favourite number: 29  Type: <class 'int'> Memory Address: 140711350355960

your birth year is here based on approximate; 2005

USER SUMMARY
Hello Aatha
you are 20 years old
your height is  5.6
your favourite number is 29
your approximate birth year is 2005
-----------------------------

Thank you for help the data collection
```

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Introduces the most fundamental Python concepts in a single script |
| 📚 **Educational** | Teaches `type()` and `id()` in a practical, hands-on way |
| 🔄 **Reusable Template** | Easily extended with more fields or logic |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Can be upgraded with validation, loops, or file saving |
| 📖 **Readable Code** | Clear linear structure makes logic easy to follow and learn |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Aastha Chodvadiya

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"Every program starts with a single variable — understand it deeply, and the rest follows."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · Data Types · CLI Applications · Logic Building · Input Handling

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 🔢 [Real Python — Variables](https://realpython.com/python-variables/) — In-depth variable and type tutorials
- 🧠 [GeeksForGeeks — Data Types](https://www.geeksforgeeks.org/python-data-types/) — Python data type reference
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 🔍 [Python id() and type()](https://realpython.com/python-type-checking/) — Type inspection guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: June 2026*

</div>
