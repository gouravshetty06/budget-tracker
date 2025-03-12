import json

BUDGET_FILE = "budget.json"

def load_budget():
    """Load the budget from a JSON file."""
    try:
        with open(BUDGET_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Could not decode the budget file. Starting with an empty budget.")
        return []

def save_budget(budget):
    """Save the budget to a JSON file."""
    with open(BUDGET_FILE, "w") as file:
        json.dump(budget, file, indent=4)

def add_expense(budget):
    """Add a new expense to the budget."""
    name = input("Enter expense name: ").strip()
    try:
        amount = float(input("Enter expense amount: ").strip())
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        budget.append({"name": name, "amount": amount})
        save_budget(budget)
        print(f"Expense '{name}' of ${amount:.2f} added successfully.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def view_expenses(budget):
    """View all recorded expenses."""
    if not budget:
        print("No expenses recorded.")
        return

    print("\nRecorded Expenses:")
    print("=" * 30)
    for i, expense in enumerate(budget, start=1):
        print(f"{i}. {expense['name']}: ${expense['amount']:.2f}")
    print("=" * 30)

def calculate_total(budget):
    """Calculate and display the total expenses."""
    total = sum(expense['amount'] for expense in budget)
    print(f"\nTotal expenses: ${total:.2f}")

def menu():
    """Display the menu options."""
    print("\nBudget Tracker")
    print("=" * 30)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit"
