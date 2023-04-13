from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    FloatField,
    ForeignKeyField,
    DateTimeField,
)
import datetime

db = SqliteDatabase("persistence.db")


class User(Model):
    user_id = CharField(unique=True)
    first_name = CharField()
    last_name = CharField(null=True)
    username = CharField(null=True)

    class Meta:
        database = db


class Category(Model):
    user = ForeignKeyField(User, backref="categories")
    name = CharField()

    class Meta:
        database = db


class Expense(Model):
    user = ForeignKeyField(User, backref="expenses")
    category = ForeignKeyField(Category, backref="expenses")
    amount = FloatField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Income(Model):
    user = ForeignKeyField(User, backref="incomes")
    category = ForeignKeyField(Category, backref="incomes")
    amount = FloatField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Limit(Model):
    user = ForeignKeyField(User, backref="limits")
    category = ForeignKeyField(Category, backref="limits")
    amount = FloatField()

    class Meta:
        database = db


db.create_tables([User, Category, Expense, Income, Limit])
