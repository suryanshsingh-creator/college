import uuid

class ExpenseManager:
    def __init__(self, storage):
        self.storage = storage

    def add_expense(self, desc, amount, category):
        expense = {
            "id": str(uuid.uuid4())[:8],
            "description": desc,
            "amount": amount,
            "category": category
        }
        self.storage.save(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        expenses = self.storage.load()
        if not expenses:
            print("No expenses found.")
            return

        print("\nID\tDescription\tAmount\tCategory")
        for e in expenses:
            print(f"{e['id']}\t{e['description']}\t{e['amount']}\t{e['category']}")

    def delete_expense(self, exp_id):
        if self.storage.delete(exp_id):
            print("Expense deleted.")
        else:
            print("ID not found.")
