import unittest
from peewee import SqliteDatabase
from models import Expense, Income, Limit, User, Category


test_db = SqliteDatabase(':memory:')


class BaseModelTestCase(unittest.TestCase):
    def setUp(self):
        test_db.bind([Expense, Income, Limit, User, Category])
        test_db.connect()
        test_db.create_tables([Expense, Income, Limit, User, Category])
        self.user = User.create(user_id='123', first_name='John', last_name='Doe', username='johndoe')
        self.category = Category.create(user=self.user, name='Food')
        self.limit = Limit.create(user=self.user, category=self.category, amount=500.0)

    def tearDown(self):
        test_db.drop_tables([Expense, Income, Limit, User, Category])
        test_db.close()


class UserModelTestCase(BaseModelTestCase):
    def test_create_user(self):
        self.assertEqual(self.user.user_id, '123')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.username, 'johndoe')


class ExpenseModelTestCase(BaseModelTestCase):
    def test_create_expense(self):
        expense = Expense.create(user=self.user, category=self.category, amount=50)

        self.assertEqual(expense.user, self.user)
        self.assertEqual(expense.category, self.category)
        self.assertEqual(expense.amount, 50)

    def test_delete_expense(self):
        expense = Expense.create(user=self.user, category=self.category, amount=50)

        Expense.delete().where(Expense.id == expense.id).execute()

        self.assertEqual(Expense.select().count(), 0)


class IncomeModelTestCase(BaseModelTestCase):
    def test_create_income(self):
        income = Income.create(user=self.user, category=self.category, amount=1000)

        self.assertEqual(income.user, self.user)
        self.assertEqual(income.category, self.category)
        self.assertEqual(income.amount, 1000)

    def test_delete_income(self):
        income = Income.create(user=self.user, category=self.category, amount=1000)

        Income.delete().where(Income.id == income.id).execute()

        self.assertEqual(Income.select().count(), 0)


class LimitModelTestCase(BaseModelTestCase):
    def test_create_limit(self):
        limit = Limit.create(user=self.user, category=self.category, amount=1000.0)

        self.assertEqual(limit.user, self.user)
        self.assertEqual(limit.category, self.category)
        self.assertEqual(limit.amount, 1000.0)

    def test_get_limit(self):
        limit = Limit.get(Limit.user == self.user, Limit.category == self.category)
        self.assertEqual(limit.amount, 500.0)

    def test_update_limit(self):
        self.limit.amount = 800.0
        self.limit.save()

        limit = Limit.get(Limit.user == self.user, Limit.category == self.category)
        self.assertEqual(limit.amount, 800.0)

    def test_delete_limit(self):
        self.limit.delete_instance()

        with self.assertRaises(Limit.DoesNotExist):
            Limit.get(Limit.user == self.user, Limit.category == self.category)

    def test_limit_category_relationship(self):
        self.assertEqual(len(self.category.limits), 1)
        self.assertEqual(self.category.limits[0].amount, 500.0)

    def test_limit_user_relationship(self):
        self.assertEqual(len(self.user.limits), 1)
        self.assertEqual(self.user.limits[0].amount, 500.0)
