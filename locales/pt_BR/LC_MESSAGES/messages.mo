��    &      L  5   |      P     Q     ^     j  
   ~     �  
   �     �     �     �     �               0     F     ^     g     u     {     �     �     �     �     �     �     �               4     D     \     k     �     �     �     �  	   �     �  �  �     Y     m  B        �  F   �  
     #   &  '   J  )   r     �    �  "   �     �  !        *  +   3  u   _     �  .   �  &   
  %   1     W  V   `  ;   �  D   �  ,   8  '   e     �  <   �     �  8   �     %  A   5  	   w  O   �     �  X   �                  $         	      
                         #                                                  %      "                                     !                       &    add_category add_expense add_expense_command add_income add_income_command categories categories_list category_already_exists category_deleted_notification category_not_found_error command_list expense_deleted_notification expense_for_the_month expense_not_found_error expenses expenses_list hello help income_added_notification income_deleted_notification income_not_found_error incomes incomes_command invalid_value_error new_category no_categories_registered no_expenses_recorded remove_category remove_category_command remove_expense remove_expense_command remove_income remove_income_command report report_command set_limit set_limit_command Project-Id-Version: 1.0.0
Report-Msgid-Bugs-To: johnnatanwillian@hotmail.com
PO-Revision-Date: 2023-04-12 08:56-0400
Last-Translator: Johnnatan William de Oliveira Barros johnnatanwillian@hotmail.com
Language-Team: Brazilian Portuguese
Language: pt_BR
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n > 1);
 adicionar_categoria adicionar_despesa Use /add_expense <categoria> <valor> para adicionar um novo gasto. adicionar_receita Use /add_income <categoria> <valor> para adicionar um novo rendimento. categorias Lista de categorias: 
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
/report <month-year: Opcional>: Mostra um relatório mensal de despesas por categoria. O gasto {expense_id} foi deletado. Gastos do mês {month}-{year} O gasto {expense_id} não existe. despesas Lista de gastos ({mês}-{ano}): 
{expenses} Oi, {first_name}! Eu sou seu assistente pessoal de finanças. Digite /help para ver a lista de comandos disponíveis. ajuda Valor adicionado à categoria {category_name}. O rendimento {income_id} foi deletado. O rendimento {income_id} não existe. receitas Use /incomes <mês-ano: Opcional> para mostrar os rendimentos registrados para o mês. Erro no valor fornecido, por favor digite um valor válido. Utilize /add_category <categoria> para adicionar uma nova categoria. Você não tem nenhuma categoria registrada. Você não tem nenhum gasto registrado. remover_categoria Use /remove_category <categoria> para deletar uma categoria. remover_despesa Use /remove_expense <id_do_gasto> para deletar um gasto. remover_receita Use /remove_income <id_do_rendimento> para deletar um rendimento. relatorio Use /report <mês-ano: Opcional> para gerar o relatório de gastos para o mês. definir_limite Use /set_limit <categoria> <limite> para definir um limite de gastos para uma categoria. 