from datetime import datetime
from utils.file_handler import load_data

FILE_PATH = "data/expenses.json"


def get_top_spending():
    data = load_data(FILE_PATH)

    if not data:
        print("No data available.")
        return

    category_totals = {}

    # Step 1: Calculate total per category
    for date in data:
        for exp in data[date]:
            category = exp["category"]
            amount = exp["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    # Step 2: Find max (Greedy step)
    max_category = None
    max_amount = 0

    for category in category_totals:
        if category_totals[category] > max_amount:
            max_amount = category_totals[category]
            max_category = category

    # Step 3: Display result
    print("\n=== Top Spending Category (Greedy) ===")

    if max_category:
        print(f"Category: {max_category}")
        print(f"Total Spending: ₹{max_amount}")
    else:
        print("No expenses found.")


def category_breakdown():
    data = load_data(FILE_PATH)

    if not data:
        print("No data available.")
        return

    category_totals = {}

    # Calculate totals
    for date in data:
        for exp in data[date]:
            category = exp["category"]
            amount = exp["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    # Display result
    print("\n=== Category-wise Breakdown ===")

    for category, total in category_totals.items():
        print(f"{category}: ₹{total}")


def total_by_date(target_date):
    data = load_data(FILE_PATH)

    if target_date not in data:
        print("No data for this date.")
        return

    total = sum(exp["amount"] for exp in data[target_date])

    print(f"\n=== Total for {target_date} ===")
    print(f"Total: ₹{total}")


def total_by_month(year_month):
    data = load_data(FILE_PATH)

    total = 0

    for date in data:
        if date.startswith(year_month):
            for exp in data[date]:
                total += exp["amount"]

    print(f"\n=== Total for {year_month} ===")
    print(f"Total: ₹{total}")


def total_last_7_days():
    data = load_data(FILE_PATH)

    total = 0
    today = datetime.today()

    for date in data:
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            if (today - date_obj).days <= 7:
                for exp in data[date]:
                    total += exp["amount"]
        except:
            continue

    print("\n=== Last 7 Days Spending ===")
    print(f"Total: ₹{total}")
