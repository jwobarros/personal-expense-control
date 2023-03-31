
# Expense Tracker Bot

This is a Telegram bot that helps you keep track of your expenses and incomes. You can create categories for your expenses and incomes, set spending limits for each category, and record your expenses and incomes.

## Installation

1. Clone this repo
2. Navigate to the cloned directory: `cd repo`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   * Windows: `venv\Scripts\activate`
   * Linux/MacOS: `source venv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Create the database: `python create_db.py`

## Usage

1. Start the bot: `python bot.py`
2. Open Telegram and search for the bot by its username. You should see the bot's profile picture and the name of the bot.
3. Start a conversation with the bot by clicking on the "Start" button or sending the "/start" command.
4. Use the available commands to interact with the bot.

## Available Commands

* `/start`: Start a conversation with the bot.
* `/help`: Get help on how to use the bot and its available commands.
* `/categories`: View a list of your expense and income categories.
* `/add_category`: Add a new expense or income category.
* `/remove_category`: Remove an existing expense or income category.
* `/set_limit`: Set a spending limit for an expense category.
* `/expenses`: View a list of your recorded expenses.
* `/add_expense`: Add a new expense.
* `/remove_expense`: Remove an existing expense.
* `/incomes`: View a list of your recorded incomes.
* `/add_income`: Add a new income.
* `/remove_income`: Remove an existing income.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
