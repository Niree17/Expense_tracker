import json
import os

from models import Expense


class ExpenseTracker:
    def __init__(self, file_name="expenses.json"):
        self.file_name = file_name
        self.expenses = self.load()

    def load(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            return []
        return [Expense(d["title"], d["category"], d["amount"], d["date"]) for d in data]

    def save(self):
        data = [expense.to_dict() for expense in self.expenses]
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def add(self, title, category, amount):
        if amount <= 0:
            raise ValueError("Amount must be more than 0")
        expense = Expense(title.strip().title(), category.strip().lower(), amount)
        self.expenses.append(expense)
        self.save()
        return expense

    def total(self):
        return sum([expense.amount for expense in self.expenses])

    def totals_by_category(self):
        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

    def search(self, word):
        word = word.strip().lower()
        return [expense for expense in self.expenses if word in expense.title.lower()]

    def delete(self, number):
        if not 1 <= number <= len(self.expenses):
            raise IndexError("That number is not in the list")
        removed = self.expenses.pop(number - 1)
        self.save()
        return removed


if __name__ == "__main__":
    if os.path.exists("practice.json"):
        os.remove("practice.json")

    tracker = ExpenseTracker("practice.json")
    tracker.add("Pizza", "food", 100)
    tracker.add("Burger", "food", 50)
    tracker.add("Bus", "travel", 30)
    print("Added 3 expenses")

    try:
        tracker.add("Free", "other", -5)
    except ValueError as error:
        print("Caught:", error)

    print("Total:", tracker.total())
    print("By category:", tracker.totals_by_category())
    print("Search 'PIZ':", [str(expense) for expense in tracker.search("PIZ")])

    removed = tracker.delete(1)
    print("Deleted:", removed.title)
    print("Left:", len(tracker.expenses))

    try:
        tracker.delete(9)
    except IndexError as error:
        print("Caught:", error)