import os
from peewee import MySQLDatabase, SqliteDatabase
from dotenv import load_dotenv

load_dotenv()


db = SqliteDatabase('Clientes.db')
# db = MySQLDatabase(os.getenv('DATABASE_URL'))