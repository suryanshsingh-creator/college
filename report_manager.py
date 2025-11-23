class ReportManager:
    def __init__(self, storage):
        self.storage = storage

    def show_summary(self):
        data = self.storage.load()

        if not data:
            print("No data to summarize.")
            return

        total = sum(float(x["amount"]) for x in data)

        print("\n=== SUMMARY REPORT ===")
        print(f"Total Spending: {total}")

        # Category-wise spending
        category_map = {}
        for d in data:
            category_map[d["category"]] = category_map.get(d["category"], 0) + float(d["amount"])

        print("\nCategory-wise Breakdown:")
        for cat, amt in category_map.items():
            print(f"{cat}: {amt}")
