
---

### 🧠 `expense_tracker.py`
```python
def add_expense(amount, category, note):
    with open("expenses.txt", "a") as file:
        file.write(f"{amount},{category},{note}\n")

def view_expenses():
    print("\nYour Expenses:\n")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount, category, note = line.strip().split(",")
                print(f"₹{amount} | {category} | {note}")
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = input("Amount: ")
            category = input("Category: ")
            note = input("Note: ")
            add_expense(amount, category, note)
            print("Expense added successfully!")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
