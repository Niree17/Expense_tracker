from models import Expense


def test_expense_str():
    expense = Expense("Pizza", "food", 250, "2026-10-22")
    assert str(expense) == "2026-10-22 | Pizza | food | Rs 250"