import sqlite3
from config import *


def get_description(text):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        return cursor.execute("SELECT description FROM \'errors\' WHERE id = '%s'" % text).fetchall()[0][0]


def save_user(user):
    pass
