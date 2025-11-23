from expense_manager import ExpenseManager
from report_manager import ReportManager
from storage_manager import StorageManager

def main():
    storage = StorageManager("data/expenses.csv")
    expense_manager = ExpenseManager(storage)
    report_manager = ReportManager(storage)

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Delete Expense")
        print("4. View Summary Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            desc = input("Description: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            expense_manager.add_expense(desc, amount, category)

        elif choice == "2":
            expense_manager.view_expenses()

        elif choice == "3":
            id_to_delete = input("Enter Expense ID to delete: ")
            expense_manager.delete_expense(id_to_delete)

        elif choice == "4":
            report_manager.show_summary()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()
