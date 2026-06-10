expenses = []

print('Expense Tracker')
print('Type "exit" at any time when entering the amount to finish session')

while True:
    amount = input('\nEnter expense amount: ')

    if amount.lower() == 'exit':
        break

    try:
        amount = float(amount)
    except ValueError:
        print('Enter a valid number: ')
        continue

    category = input('Enter category: ')
    note = input('Enter note: ')
    date = input('Enter date: ')

    expense = {
        'amount': amount,
        'category': category,
        'note': note,
        'date': date
    }

    expenses.append(expense)
    print('Expense added successfully!')

# Summary section
print ('\nExpense Summary')
print('-' * 30)

total_spent = 0

for expense in expenses:
    total_spent += expense['amount']

print(f'Total Expense: ${total_spent:.2f}')

# Category Total
category_total = {}

for expense in expenses:
    category = expense['category']

    if category not in category_total:
        category_total[category] = 0

    category_total[category] += expense['amount']

print('\nSpending by Category:')

for category, total in category_total.items():
    print(f'{category}: ${total:.2f}')

# Print all expenses
print('\nAll Expenses:')

for expense in expenses:
    print(
        f'${expense['amount']:.2f} | '
        f'{expense['category']} | '
        f'{expense['note']} | '
        f'{expense['date']}'
    )
