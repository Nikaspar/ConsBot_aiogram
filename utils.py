import sqlite3
from config import *


def get_description(text):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        try:
            return cursor.execute("SELECT description FROM \'errors\' WHERE id = '%s'" % text).fetchall()[0][0]
        except IndexError:
            return 'Ошибки с таким кодом нет в базе.\nОтправьте фото ошибки в следующем сообщении.'
