from utils.file_handler import load_data

FILE_PATH = "data/expenses.json"


def bfs_search(keyword):
    data = load_data(FILE_PATH)

    if not data:
        print("No data found.")
        return

    queue = []
    visited_nodes = 0
    results = []

    # Add all dates to queue
    for date in data:
        queue.append((date, data[date]))

    # BFS traversal
    while queue:
        current_date, expenses = queue.pop(0)

        for exp in expenses:
            visited_nodes += 1   # count each expense

            if (keyword.lower() in exp["category"].lower() or
                keyword.lower() in exp["note"].lower()):
                results.append((current_date, exp))

    # Show results
    print("\n=== BFS Search Results ===")

    if not results:
        print("No matching expenses found.")
    else:
        for date, exp in results:
            print(f"Date: {date} | Amount: ₹{exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")

    print(f"\nNodes explored: {visited_nodes}")



def dfs_search(keyword):
    data = load_data(FILE_PATH)

    if not data:
        print("No data found.")
        return

    stack = []
    visited_nodes = 0
    results = []

    # Add all dates to stack
    for date in data:
        stack.append((date, data[date]))

    # DFS traversal
    while stack:
        current_date, expenses = stack.pop()

        for exp in expenses:
            visited_nodes += 1   # count each expense

            if (keyword.lower() in exp["category"].lower() or
                keyword.lower() in exp["note"].lower()):
                results.append((current_date, exp))

    # Show results
    print("\n=== DFS Search Results ===")

    if not results:
        print("No matching expenses found.")
    else:
        for date, exp in results:
            print(f"Date: {date} | Amount: ₹{exp['amount']} | Category: {exp['category']} | Note: {exp['note']}")

    print(f"\nNodes explored: {visited_nodes}")