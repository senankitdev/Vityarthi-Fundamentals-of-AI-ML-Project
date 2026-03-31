from utils.file_handler import load_data, save_data
from datetime import datetime

FILE_PATH = "data/expenses.json"

EXPENSE_FILE = "data/expenses.json"
CATEGORY_FILE = "data/categories.json"


# Add a new expense
def add_expense(amount, category, note):
    data = load_data(EXPENSE_FILE)
    category_data = load_data(CATEGORY_FILE)

    valid_categories = category_data.get("categories", [])

    # Validate category
    if category.lower() not in valid_categories:
        print("❌ Invalid category!")
        print("Valid categories are:")
        for cat in valid_categories:
            print(f"- {cat}")
        return

    # Get today's date
    today = str(datetime.today().date())

    if today not in data:
        data[today] = []

    expense = {
        "amount": amount,
        "category": category.lower(),
        "note": note
    }

    data[today].append(expense)

    save_data(EXPENSE_FILE, data)

    print("✅ Expense added successfully!")





# View all expenses
def view_expenses():
    data = load_data(FILE_PATH)

    if not data:
        print("No expenses found.")
        return

    for date, expenses in data.items():
        print(f"\nDate: {date}")
        for exp in expenses:
            print(f"  Amount: ₹{exp['amount']}, Category: {exp['category']}, Note: {exp['note']}")