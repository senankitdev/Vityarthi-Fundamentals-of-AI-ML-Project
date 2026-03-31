# 💰 Where Is My Money Going?

> **A command-line expense tracking system powered by classical AI search algorithms.**

---

## 📖 Overview
**Where Is My Money Going ?** is a Python-based CLI application designed to help users efficiently track, manage, and analyze daily expenses. 

Beyond basic tracking, this project demonstrates the practical application of foundational AI algorithms—**Breadth-First Search (BFS)**, **Depth-First Search (DFS)**, and **Greedy algorithms**—on real-world financial data. It bridges the gap between algorithmic theory and practical software development.

---

## 🎯 Key Objectives
* **Efficient Tracking:** Build a streamlined system for daily financial logging.
* **Structured Organization:** Categorize expenses for better visibility.
* **Algorithmic Analysis:** Apply AI search techniques to analyze spending behavior.
* **Modular Architecture:** Ensure high maintainability and clean code principles.

---

## ✨ Core Features

### 🧾 Expense Management
* **Detailed Logging:** Add expenses with Amount, Category, and Notes.
* **Chronological View:** Display records in the order they occurred.
* **Persistence:** Uses JSON for lightweight, reliable data storage.

### 🔍 Intelligent Search System
* **Breadth-First Search (BFS):** Traverses records level-by-level using a **Queue (FIFO)** to ensure uniform exploration.
* **Depth-First Search (DFS):** Explores deeply before backtracking using a **Stack (LIFO)** for targeted searches.
* **Flexible Queries:** Search by category or keywords with case-insensitive matching.
* **Traversal Insights:** Displays the number of nodes explored during the search process.

### 📊 Analytics Engine
* **Greedy Algorithm:** Locally optimal decision-making to rapidly identify the highest spending categories.
* **Financial Insights:** * Category-wise expenditure breakdowns.
    * Daily and monthly spending summaries.
    * 7-day rolling expense analysis.

---

## 🧠 Algorithms Implemented

| Algorithm | Purpose | Approach |
| :--- | :--- | :--- |
| **BFS** | Level-wise search | Queue (FIFO) |
| **DFS** | Deep traversal search | Stack (LIFO) |
| **Greedy** | Maximum spending detection | Local optimization |

---

## ⏱️ Complexity Analysis

*Let $n$ = number of expense records.*

| Operation | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Add Expense** | $O(1)$ | $O(1)$ |
| **View Expenses** | $O(n)$ | $O(1)$ |
| **BFS/DFS Search** | $O(n)$ | $O(n)$ |
| **Category Breakdown** | $O(n)$ | $O(k)$ (where $k$ is categories) |
| **Top Spending (Greedy)** | $O(n)$ | $O(1)$ |

---

## 🏗️ Project Architecture

```text
where_is_my_money_going/
│
├── main.py                # Entry point & CLI Menu
├── data/
│   ├── expenses.json     # Expense records storage
│   └── categories.json   # Predefined valid categories
│
├── core/
│   ├── expense_manager.py  # CRUD operations
│   ├── search_engine.py    # BFS & DFS logic
│   └── analytics.py        # Greedy algorithm & insights
│
├── utils/
│   ├── file_handler.py     # JSON I/O operations
│   └── helpers.py          # Input validation & formatting
│
└── README.md
```

---


## 📦 How to Run

## 1️⃣ Clone the repository
```bash

git clone https://github.com/your-username/where_is_my_money_going.git
cd where_is_my_money_going

```

## 2️⃣ Run the application
```bash
python main.py

```


## ⚠️ Important Notes

Before running the application, make sure the following files exist:

- `data/expenses.json`
- `data/categories.json`

These files are required for storing and retrieving expense data.

---

---

## 🔍 Key Insights

* **Algorithmic Traversal:** BFS and DFS provide different traversal strategies (layer-by-layer vs. deep-dive) but maintain similar time complexity for category exploration.
* **Trend Analysis:** A **Greedy algorithm** is implemented to efficiently identify and prioritize dominant spending trends.
* **Data Management:** Uses **JSON** for lightweight, flexible, and human-readable data persistence.
* **Architecture:** A **Modular design** approach was used to ensure the codebase remains scalable and easy to maintain.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Format:** JSON
* **Algorithms:** Breadth-First Search (BFS), Depth-First Search (DFS), Greedy Search

---

## 🚀 Future Enhancements

 * **GUI-based Interface:** Transition from CLI to Tkinter or a Web App (Flask/FastAPI).
 * **Data Visualization:** Integration of Matplotlib/Seaborn for charts and graphs.
 * **Proactive Budgeting:** Implementation of budget planning and automated alerts.
 * **Report Export:** Ability to export financial summaries as CSV or PDF.
 * **Database Integration:** Moving from JSON to SQLite or MongoDB for robust data handling.

---

## 📌 Conclusion

This project showcases how classical AI algorithms can be effectively applied to everyday problems like expense tracking. It bridges the gap between theoretical data structures and practical software design, delivering an extensible solution for personal finance management.

---
### PROJECT OUTPUT

<p align="center">
  <img src="images/budget_projection.png" width="85%">
</p>
<p align="center">
  <img src="images/budget_projection.png" width="85%">
</p>
<p align="center">
  <img src="images/budget_projection.png" width="85%">
</p>
---
## 📬 Contact

*For suggestions or collaboration, feel free to reach out!*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github)](https://github.com/senankitdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/ankit-sen00)
