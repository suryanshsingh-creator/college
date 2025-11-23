import unittest
from storage_manager import StorageManager
from expense_manager import ExpenseManager

class TestExpenseTracker(unittest.TestCase):
    def test_add_expense(self):
        storage = StorageManager("data/test_expenses.csv")
        manager = ExpenseManager(storage)
        manager.add_expense("Tea", 10, "Food")
        data = storage.load()
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
