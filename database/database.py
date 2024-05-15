import os
from peewee import MySQLDatabase
from dotenv import load_dotenv

load_dotenv()

db = MySQLDatabase(os.getenv('DATABASE_URL'))