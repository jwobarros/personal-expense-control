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

## Configuration

1. Create a new bot using the [BotFather](https://t.me/botfather) on Telegram.
2. Copy the API token provided by the BotFather.
3. Create a new file named `.env` in the project directory.
4. Inside the `.env` file, add the following line: `TELEGRAM_API_KEY=<your-API-token>`
5. Create a new database using SQLite or another database management system.

## Usage

1. Start the bot: `python bot.py`
2. Open Telegram and search for the bot by its username. You should see the bot's profile picture and the name of the bot.
3. Start a conversation with the bot by clicking on the "Start" button or sending the "/start" command.
4. Use the available commands to interact with the bot.

## Available Commands

* `/start`: Start a conversation with the bot.
* `/help`: Get help on how to use the bot and its available commands.
* `/categories`: View a list of your expense and income categories.
* `/add_category <category>`: Add a new expense or income category.
* `/remove_category <category_id>`: Remove an existing expense or income category.
* `/set_limit <category> <limit_amount>`: Set a spending limit for an expense category.
* `/expenses <month-year: Optional>`: View a list of your recorded expenses, default current month-year.
* `/add_expense <category> <amount>`: Add a new expense.
* `/remove_expense <expense_id>`: Remove an existing expense.
* `/incomes <month-year: Optional>`: View a list of your recorded incomes, default current month-year.
* `/add_income <category> <amount>`: Add a new income.
* `/remove_income <income_id>`: Remove an existing income.

<categoria>


<categoria>


<categoria>


<categoria>


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
