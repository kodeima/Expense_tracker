# Expense Tracker

## Overview

This is a simple Python console application for tracking personal expenses. Users can continuously add expenses by entering an amount, category, note, and optional date. All expenses are stored in a list during the program session.

When the user exits the application, the program generates a summary showing:

* Total amount spent
* Spending by category
* A list of all recorded expenses

## Features

* Add multiple expenses in a loop
* Store expenses using dictionaries inside a list
* Track:

  * Amount
  * Category
  * Note
  * Date
* Calculate total spending
* Summarize spending by category
* Display all entered expenses
* Exit the program using a command

### Libraries Used

This project uses only Python built-in functionality and requires no external libraries.

## How to Run

1. Save the program.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the script.

## Usage

```text
Expense Tracker
Type 'exit' at any time when entering the amount to finish.

Enter expense amount: 25.50
Enter category: Food
Enter note: Lunch
Enter date (optional): 2026-06-10

Expense added successfully!

Enter expense amount: 15
Enter category: Transport
Enter note: Bus fare
Enter date (optional): 2026-06-10

Expense added successfully!

Enter expense amount: exit
```

### Summary

```text
Expense Summary
------------------------------
Total Expenses: $40.50

Spending by Category:
Food: $25.50
Transport: $15.00

All Expenses:
$25.50 | Food | Lunch | 2026-06-10
$15.00 | Transport | Fare | 2026-06-10
```

## Data Structure

Each expense is stored as a dictionary:

```python
{
    "amount": 25.50,
    "category": "Food",
    "note": "Lunch",
    "date": "2026-06-10"
}
```

All expense dictionaries are stored in a list:

```python
expenses = []
```
