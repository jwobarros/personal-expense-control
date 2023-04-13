import telebot, os, datetime
from models import User, Category, Limit, Income, Expense
from helpers import snake_case, monthly_report
import gettext

LANG = os.getenv("LOCALE_LANG")
lang = gettext.translation("messages", localedir="locales", languages=[LANG])
_ = lang.gettext

APY_KEY = os.getenv("TELEGRAM_API_KEY")
bot = telebot.TeleBot(APY_KEY)


@bot.message_handler(commands=[_("categories")])
def show_categories(message):
    categories = ""
    for category in Category.select().where(Category.user == message.from_user.id):
        categories += f"{category.name}\n"

    if categories:
        response = _("categories_list").format(categories=categories)
    else:
        response = _("no_categories_registered")

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("add_category")])
def add_category(message):
    if len(message.text.split()) < 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("new_category"),
        )
        return None

    category_name = snake_case(" ".join(message.text.split()[1:]))

    try:
        Category.get(name=category_name, user_id=message.from_user.id)
        response = _("category_already_exists").format(category_name=category_name)
    except Category.DoesNotExist:
        Category.create(user_id=message.from_user.id, name=category_name)
        response = _("category_added").format(category_name=category_name)

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("remove_category")])
def remove_category(message):
    if len(message.text.split()) < 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("remove_category_command"),
        )
        return None

    category_name = snake_case(" ".join(message.text.split()[1:]))

    try:
        category = Category.get(name=category_name, user_id=message.from_user.id)
        response = _("category_deleted_notification").format(category.name)
        category.delete_instance()
    except Category.DoesNotExist:
        response = _("category_not_found_error")

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("set_limit")])
def set_limit(message):
    if len(message.text.split()) < 3:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("set_limit_command"),
        )
        return None

    category_name = snake_case(" ".join(message.text.split()[1:-1]))

    try:
        limit_amount = float(message.text.split()[-1])
    except ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("invalid_value_error"),
        )
        return None

    try:
        # Save limit to database
        limit = Limit.get(category=category_name, user_id=message.from_user.id)
        limit.amount = limit_amount
        limit.save()
    except Limit.DoesNotExist:
        Limit.create(
            user_id=message.from_user.id, category=category_name, amount=limit_amount
        )

    response = f"Novo limite definido para a categoria {category_name}."
    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("incomes")])
def show_incomes(message):
    msg = message.text.split()
    if len(msg) > 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("incomes_command"),
        )
        return None
    if len(msg) == 2:
        month = int(msg[1].split("-")[0])
        year = int(msg[1].split("-")[1])
    else:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

    incomes = ""
    for income in Income.select().where(
        Income.user == message.from_user.id,
        Income.created_date.month == month,
        Income.created_date.year == year,
    ):
        incomes += f"{income.id} - {income.category.name} - {income.amount} - {income.description}\n"

    if incomes:
        response = f"Lista de entradas ({month}-{year}): \n {incomes}"
    else:
        response = "Voce nao tem nenhuma entrada cadastrada."

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("add_income")])
def add_income(message):
    msg = message.text.split()
    if len(msg) <= 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("add_income_command"),
        )
        return None

    category_name = snake_case(" ".join(message.text.split()[1:-1]))

    try:
        category_id = Category.get(name=category_name, user_id=message.from_user.id)
    except Category.DoesNotExist:
        bot.send_message(chat_id=message.chat.id, text=_("category_not_found_error"))
        return None

    try:
        amount = float(msg[-1])
        Income.create(
            user=message.from_user.id,
            amount=amount,
            category=category_id,
        )
        response = _("income_added_notification").format(category_name=category_name)
        bot.send_message(chat_id=message.chat.id, text=response)

    except ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("invalid_value_error"),
        )


@bot.message_handler(commands=[_("remove_income")])
def remove_income(message):
    if len(message.text.split()) != 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("remove_income_command"),
        )
        return None

    income_id = snake_case(message.text.split()[1])

    try:
        income = Income.get(id=income_id)
        income.delete_instance()
        response = _("income_deleted_notification").format(income_id=income_id)
    except Income.DoesNotExist:
        response = _("income_not_found_error").format(income_id=income_id)

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("expenses")])
def show_expenses(message):
    msg = message.text.split()
    if len(msg) > 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("incomes_command"),
        )
        return None
    if len(msg) == 2:
        month = int(msg[1].split("-")[0])
        year = int(msg[1].split("-")[1])
    else:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

    expenses = ""
    for expense in Expense.select().where(
        Expense.user == message.from_user.id,
        Expense.created_date.month == month,
        Expense.created_date.year == year,
    ):
        expenses += f"{expense.id} - {expense.category.name} - {expense.amount}\n"

    if expenses:
        response = _("expenses_list").format(month, year, expenses)
    else:
        response = _("no_expenses_recorded")

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("add_expense")])
def add_expense(message):
    msg = message.text.split()
    if not (2 < len(msg) < 5):
        bot.send_message(
            chat_id=message.chat.id,
            text=_("add_expense_command"),
        )
        return None

    category_name = snake_case(" ".join(message.text.split()[1:-1]))

    try:
        category_id = Category.get(name=category_name, user_id=message.from_user.id)
    except Category.DoesNotExist:
        bot.send_message(chat_id=message.chat.id, text=_("category_not_found_error"))
        return None

    try:
        amount = float(msg[-1])
        Expense.create(
            user=message.from_user.id,
            amount=amount,
            category=category_id,
        )
        response = _("income_added_notification").format(category_name=category_name)
        bot.send_message(chat_id=message.chat.id, text=response)

    except ValueError:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("invalid_value_error"),
        )


@bot.message_handler(commands=[_("remove_expense")])
def remove_expense(message):
    if len(message.text.split()) != 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("remove_expense_command"),
        )
        return None

    expense_id = snake_case(message.text.split()[1])

    try:
        expense = Expense.get(id=expense_id)
        expense.delete_instance()
        response = _("expense_deleted_notification").format(expense_id=expense_id)
    except Expense.DoesNotExist:
        response = _("expense_not_found_error").format(expense_id=expense_id)

    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(commands=[_("report")])
def show_monthly_report(message):
    msg = message.text.split()
    if len(msg) > 2:
        bot.send_message(
            chat_id=message.chat.id,
            text=_("report_command"),
        )
        return None
    if len(msg) == 2:
        month = int(msg[1].split("-")[0])
        year = int(msg[1].split("-")[1])
    else:
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
    response = monthly_report(message.from_user.id, month, year)
    bot.send_message(chat_id=message.chat.id, text=response)
    # sendPhoto
    with open(f"temp/{message.from_user.id}-{month}-{year}.png", "rb") as photo:
        bot.send_photo(chat_id=message.chat.id, photo=photo)


@bot.message_handler(commands=[_("help")])
def show_commands(message):
    response = _("command_list")
    bot.send_message(chat_id=message.chat.id, text=response)


@bot.message_handler(func=lambda message: True)
def start(message):
    # Get user info
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    try:
        User.get(user_id=user_id)
    except User.DoesNotExist:
        User.create(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )

    # Send welcome message
    response = _("hello").format(first_name=first_name)

    bot.send_message(chat_id=message.chat.id, text=response)


if __name__ == "__main__":
    bot.polling()
