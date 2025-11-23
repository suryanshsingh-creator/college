import csv
import os

class StorageManager:
    def __init__(self, filename):
        self.filename = filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    def save(self, expense):
        write_header = not os.path.exists(self.filename)
        with open(self.filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "description", "amount", "category"])
            if write_header:
                writer.writeheader()
            writer.writerow(expense)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return list(csv.DictReader(f))

    def delete(self, expense_id):
        data = self.load()
        new_data = [d for d in data if d["id"] != expense_id]

        if len(new_data) == len(data):
            return False

        with open(self.filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "description", "amount", "category"])
            writer.writeheader()
            writer.writerows(new_data)

        return True
