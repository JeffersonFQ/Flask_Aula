from peewee import CharField,Model,DateTimeField
from database.database import db
import datetime



class Clientes(Model):
    nome = CharField()
    email = CharField()
    log_registro = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db