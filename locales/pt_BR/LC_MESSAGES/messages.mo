��          �   %   �      P     Q     e     x     �     �     �     �     �               /     =     C     ]     y     �     �     �     �     �     �               4     C  �  U  B   �  F     "   `  '   �  )   �     �    �  "         #  !   A  +   c  u   �  .     &   4  %   [  V   �  ;   �  D     ,   Y  '   �  <   �  8   �  A   $  O   f  X   �                        	                                                                             
                        add_expense_command add_income_command categories_list category_already_exists category_deleted_notification category_not_found_error command_list expense_deleted_notification expense_for_the_month expense_not_found_error expenses_list hello income_added_notification income_deleted_notification income_not_found_error incomes_command invalid_value_error new_category no_categories_registered no_expenses_recorded remove_category_command remove_expense_command remove_income_command report_command set_limit_command Project-Id-Version: 1.0.0
Report-Msgid-Bugs-To: johnnatanwillian@hotmail.com
PO-Revision-Date: 2023-04-12 08:56-0400
Last-Translator: Johnnatan William de Oliveira Barros johnnatanwillian@hotmail.com
Language-Team: Brazilian Portuguese
Language: pt_BR
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n > 1);
 Use /add_expense <categoria> <valor> para adicionar um novo gasto. Use /add_income <categoria> <valor> para adicionar um novo rendimento. List of categories: 
 {categories} A categoria {category_name} já existe. A categoria {category.name} foi deletada. A categoria não existe. Lista de comandos disponíveis para este bot:
/start: Inicie uma conversa com o bot.
/help: Obtenha ajuda sobre como usar o bot e seus comandos disponíveis.
/categories: Visualize uma lista de suas categorias de despesas e receitas.
/add_category <category>: Adicione uma nova categoria de despesa ou receita.
/remove_category <category_id>: Remova uma categoria de despesa ou receita existente.
/set_limit <category> <limit_amount>: Defina um limite de gastos para uma categoria de despesas.
/expenses <month-year: Opcional>: Veja uma lista de suas despesas registradas, o padrão é o mês e ano atual.
/add_expense <category> <amount>: Adicione uma nova despesa.
/remove_expense <expense_id>: Remova uma despesa existente.
/incomes <month-year: Opcional>: Veja uma lista de seus rendimentos registrados, o padrão é o mês e ano atual.
/add_income <category> <amount>: Adicione uma nova renda.
/remove_income <income_id>: Remova uma renda existente.
/report <month-year: Opcional>: Mostra um relatório mensal de despesas por categoria. O gasto {expense_id} foi deletado. Gastos do mês {month}-{year} O gasto {expense_id} não existe. Lista de gastos ({mês}-{ano}): 
{expenses} Oi, {first_name}! Eu sou seu assistente pessoal de finanças. Digite /help para ver a lista de comandos disponíveis. Valor adicionado à categoria {category_name}. O rendimento {income_id} foi deletado. O rendimento {income_id} não existe. Use /incomes <mês-ano: Opcional> para mostrar os rendimentos registrados para o mês. Erro no valor fornecido, por favor digite um valor válido. Utilize /add_category <categoria> para adicionar uma nova categoria. Você não tem nenhuma categoria registrada. Você não tem nenhum gasto registrado. Use /remove_category <categoria> para deletar uma categoria. Use /remove_expense <id_do_gasto> para deletar um gasto. Use /remove_income <id_do_rendimento> para deletar um rendimento. Use /report <mês-ano: Opcional> para gerar o relatório de gastos para o mês. Use /set_limit <categoria> <limite> para definir um limite de gastos para uma categoria. 