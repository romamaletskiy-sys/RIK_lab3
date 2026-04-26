# Lab 3 — Survey Form (PyQt6)

A desktop **Survey Form** application built with Python and PyQt6 as part of a university Qt Framework lab.

## Features

- Clean, modern UI using `QVBoxLayout` / `QHBoxLayout`
- Three input fields: **Full Name**, **Age**, **Favorite Programming Language**
- **Age validation** — must be a whole number between 1 and 120
- **Language field** — editable `QComboBox` with a built-in list of popular languages (free-text input also allowed)
- Answers are **appended** to `survey_answers.txt` with a timestamp
- Success confirmation via `QMessageBox`; all fields clear after submission

## Requirements

- Python 3.10+
- PyQt6

Install dependencies:

```bash
pip install PyQt6
```

## Running

```bash
python main.py
```

## Output format (`survey_answers.txt`)

```
--- Submission [2026-04-27 02:30:46] ---
Full Name : Jane Doe
Age       : 21
Fav. Lang : Python
```

## Project structure

```
lab3/
├── main.py              # Application source
├── survey_answers.txt   # Generated on first submission
└── README.md
```
