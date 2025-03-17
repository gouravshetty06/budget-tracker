def menu():
    """Display the menu options."""
    budget = load_budget()
    options = {
        "1": lambda: add_expense(budget),
        "2": lambda: view_expenses(budget),
        "3": lambda: calculate_total(budget),
        "4": lambda: print("Goodbye!")
    }

    while True:
        print("\nBudget Tracker")
        print("=" * 30)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in options:
            options[choice]()
            if choice == "4":
                break
        else:
            print("Invalid choice. Please try again.")
