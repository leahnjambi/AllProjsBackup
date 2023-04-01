from peewee import *
from os import path

db_connection = path.dirname(path.relpath(__file__))
db = SqliteDatabase(path.join(db_connection, "eMobilis"))


# create a table called users in the database
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


# create a table called users in the database
class Product(Model):
    name = CharField()
    qtty = CharField(unique=True)
    price = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)





# create a table called employees in the database

class Employee(Model):
    name = CharField()
    gender = CharField()
    age = CharField()
    career = CharField()
    department = CharField()
    salary = CharField()

    class Meta:
        database = db


Employee.create_table(fail_silently=True)

# create a table called students in the database

class Student(Model):
    name = CharField()
    email = CharField()
    gender = CharField()
    age = CharField()
    course = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)