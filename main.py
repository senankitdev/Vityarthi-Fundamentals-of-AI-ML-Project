from core.expense_manager import add_expense, view_expenses
from core.search_engine import bfs_search, dfs_search

from core.analytics import (
    get_top_spending,
    category_breakdown,
    total_by_date,
    total_by_month,
    total_last_7_days
)


def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses (BFS / DFS)")
        print("4. Show Top Spending (Greedy)")
        print("5. Category-wise Breakdown")
        print("6. Total Analytics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # OPTION 1: Add Expense
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))

                from utils.file_handler import load_data

                category_data = load_data("data/categories.json")
                valid_categories = category_data.get("categories", [])

                print("\nAvailable categories:")
                for cat in valid_categories:
                    print(f"- {cat}")

                category = input("\nEnter category: ")

                note = input("Enter note: ")

                add_expense(amount, category, note)

            except:
                print("Invalid input! Please try again.")

        # OPTION 2: View Expenses
        elif choice == "2":
            view_expenses()

        # OPTION 3: Search (AI PART 🔥)
        elif choice == "3":
            keyword = input("Enter keyword to search: ")

            print("\nChoose Search Algorithm:")
            print("1. BFS")
            print("2. DFS")

            algo_choice = input("Enter choice: ")

            if algo_choice == "1":
                bfs_search(keyword)

            elif algo_choice == "2":
                dfs_search(keyword)

            else:
                print("Invalid algorithm choice!")

        # OPTION 4: Greedy Algorithm
        elif choice == "4":
            get_top_spending()

        # OPTION 5: category breakdown
        elif choice == "5":
            category_breakdown()

        # OPTION 6: Total Analytics
        elif choice == "6":
            while True:
                print("\n=== Total Analytics ===")
                print("1. Date-wise total")
                print("2. Monthly total")
                print("3. Last 7 days total")
                print("4. Back")

                sub_choice = input("Enter choice: ")

                if sub_choice == "1":
                    date = input("Enter date (YYYY-MM-DD): ")
                    total_by_date(date)

                elif sub_choice == "2":
                    month = input("Enter month (YYYY-MM): ")
                    total_by_month(month)

                elif sub_choice == "3":
                    total_last_7_days()

                elif sub_choice == "4":
                    break

                else:
                    print("Invalid choice!")

        # OPTION 7: EXIT
        elif choice == "7":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    main()
