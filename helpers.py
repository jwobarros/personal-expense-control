import matplotlib.pyplot as plt
from re import sub
from models import Expense


def snake_case(text):
    """
    Converts a string to snake case.
    """

    # Remove whitespace, hyphens and underscores at the beginning and end of the string
    text = text.strip().strip("-").strip("_")

    # Replace special characters with underscores
    text = sub(r"[^a-zA-Z0-9]+", "_", text)

    # Replace lower case letters (except the first letter)
    text = sub(r"([a-z0-9])([A-Z])", r"\1_\2", text).lower()

    return text


def monthly_report(user_id, month, year):
    expenses = Expense.select().where(
        Expense.user == user_id,
        Expense.created_date.month == month,
        Expense.created_date.year == year,
    )

    if not expenses:
        return f"Não há despesas registradas para o mês {month} de {year}."

    # Groups expenses by category and sums their corresponding values
    categories = {}
    for expense in expenses:
        category = expense.category.name
        value = expense.amount
        if category not in categories:
            categories[category] = value
        else:
            categories[category] += value

    # Create the pie chart
    fig, ax = plt.subplots()
    ax.pie(list(categories.values()), labels=list(categories.keys()), autopct="%1.1f%%")
    ax.set_title(f"Gastos do mês {month} de {year}")
    plt.savefig(f"temp/{user_id}-{month}-{year}.png")

    total = sum(categories.values())
    report = f"Gastos do mês {month} de {year}:\n"
    for category, value in categories.items():
        report += f"\n- {category}: R${value:.2f} ({(value/total)*100:.1f}%)"
    report += f"\n\nTotal: R${total:.2f}"
    return report
