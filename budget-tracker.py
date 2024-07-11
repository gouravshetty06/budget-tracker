import json
BUDGET_FILE = "budget.json"


def load_budget():
        try:
         with open(BUDGET_FILE, "r") as file:
            return json.load(file)
        except FileNotFoundError:
            return []


def save_budget(budget):
    with open(BUDGET_FILE, "w") as file:
        json.dump(budget, file, indent=4)


def add_expense(budget, name, amount):
    
    budget.append({"name": name, "amount": amount})
    save_budget(budget)


def view_expenses(budget):
       if not budget:
        print("No expenses recorded.")
        return

       for i, expense in enumerate(budget, start=1):
        print(f"{i}. {expense['name']}: ${expense['amount']:.2f}")


def calculate_total(budget):
        total = sum(expense['amount'] for expense in budget)
        print(f"Total expenses: ${total:.2f}")


def main():
    budget = load_budget()

    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            add_expense(budget, name, amount)
        elif choice == '2':
            view_expenses(budget)
        elif choice == '3':
            calculate_total(budget)
        elif choice == '4':
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()