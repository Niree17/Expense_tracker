import requests

from currency import get_rate
from tracker import ExpenseTracker

def add_menu(tracker):
    title = input("What did you spend on? ")
    category = input("Category (food/travel/study/fun/other): ")
    try:
        amount = float(input("How much (in rupees)? "))
        expense = tracker.add(title, category, amount)
    except ValueError as error:
        print(f"Could not add: {error}")
        return
    print(f"Added: {expense}")


def view_menu(tracker):
    if not tracker.expenses:
        print("No expenses yet.")
        return
    for number, expense in enumerate(tracker.expenses, start=1):
        print(f"{number}. {expense}")


def summary_menu(tracker):
    if not tracker.expenses:
        print("No expenses yet.")
        return
    print(f"Total spent: Rs {tracker.total():.2f}")
    for category, amount in tracker.totals_by_category().items():
        print(f"  {category}: Rs {amount:.2f}")
    try:
        rate = get_rate("INR", "USD")
        print(f"In US dollars: about ${tracker.total() * rate:.2f}")
    except requests.RequestException:
        print("(Could not fetch the dollar rate. Check your internet.)") 

def search_menu(tracker):
    word = input("Search for: ")
    matches = tracker.search(word)
    if not matches:
        print("Nothing found.")
        return
    for expense in matches:
        print(f"- {expense}")


def delete_menu(tracker):
    view_menu(tracker)
    if not tracker.expenses:
        return
    try:
        number = int(input("Enter the number to delete: "))
        removed = tracker.delete(number)
    except (ValueError, IndexError) as error:
        print(f"Could not delete: {error}")
        return
    print(f"Deleted: {removed.title}")


def main():
    tracker = ExpenseTracker()
    print("Welcome to Expense Tracker v2!")

    while True:
        print("\n1. Add  2. View  3. Summary  4. Search  5. Delete  6. Quit")
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            add_menu(tracker)
        elif choice == "2":
            view_menu(tracker)
        elif choice == "3":
            summary_menu(tracker)
        elif choice == "4":
            search_menu(tracker)
        elif choice == "5":
            delete_menu(tracker)
        elif choice == "6":
            print("Bye! Your data is saved.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()