��          �   %   �      p     q     �  
   �     �     �     �     �     �               ;     Q     i     w     }     �     �     �     �     �     �          )     A     X     n     }  t  �  :     8   ?  
   x  #   �  ,   �  ,   �  .        0  �  M  *   �
     (  (   H  .   q  i   �  ,   
  (   7  &   `  O   �  8   �  9     )   J  $   t  5   �  5   �  3     T   9  P   �           	                                                                               
                                 add_expense_command add_income_command categories categories_list category_added category_already_exists category_deleted_notification category_not_found_error command_list expense_deleted_notification expense_for_the_month expense_not_found_error expenses_list hello income_added_notification income_deleted_notification income_not_found_error incomes_command invalid_value_error new_category no_categories_registered no_expenses_recorded remove_category_command remove_expense_command remove_income_command report_command set_limit_command Project-Id-Version: 1.0.0
Report-Msgid-Bugs-To: johnnatanwillian@hotmail.com
PO-Revision-Date: 2023-04-12 08:56-0400
Last-Translator: Johnnatan William de Oliveira Barros johnnatanwillian@hotmail.com
Language-Team: English
Language: en_US
MIME-Version: 1.0
Content-Type: text/plain; charset=ASCII
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
 Use /add_expense <category> <amount> to add a new expense. Use /add_income <category> <amount> to add a new income. categories Lista de categorias: 
 {categories} Category {category_name} successfully added. The category {category_name} already exists. The category {category.name} has been deleted. The category does not exist. List of available commands for this bot:
/start: Start a conversation with the bot.
/help: Get help on how to use the bot and its available commands.
/categories: View a list of your expense and income categories.
/add_category <category>: Add a new expense or income category.
/remove_category <category_id>: Remove an existing expense or income category.
/set_limit <category> <limit_amount>: Set a spending limit for an expense category.
/expenses <month-year: Optional>: View a list of your recorded expenses, default is current month-year.
/add_expense <category> <amount>: Add a new expense.
/remove_expense <expense_id>: Remove an existing expense.
/incomes <month-year: Optional>: View a list of your recorded incomes, default is current month-year.
/add_income <category> <amount>: Add a new income.
/remove_income <income_id>: Remove an existing income.
/report <month-year: Optional>: Shows a monthly report to expenses by category. The expense {expense_id} has been deleted. Expenses for the {year}-{month} The expense {expense_id} does not exist. List of expenses ({month}-{year}): 
{expenses} Hi, {first_name}! I am your personal finance assistant. Type /help to see the list of available commands. Value added to the category {category_name}. The income {income_id} has been deleted. The income {income_id} does not exist. Use /incomes <month-year: Optional> to show the recorded incomes for the month. Error in the value provided, please enter a valid value. Use /add_category <categorie_name> to add a new category. You don't have any categories registered. You don't have any expense recorded. Use /remove_category <category> to delete a category. Use /remove_expense <income_id> to delete an expense. Use /remove_income <income_id> to delete an income. Use /report <month-year: Optional> to generate the report of expenses for the month. Use /set_limit <category> <limit_amount> to set a spending limit for a category. 