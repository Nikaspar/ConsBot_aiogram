import sqlite3
from datetime import datetime
from config import *


def get_description(text):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    with connection:
        try:
            return cursor.execute("SELECT description FROM \'errors\' WHERE id = '%s'" % text).fetchall()[0][0]
        except IndexError:
            return 'Ошибки с таким кодом нет в базе.'


def get_photo(photo):
    current_datetime = datetime.now()
    with open("storage/{}.jpg".format(current_datetime.strftime("%d_%m_Y__%H_%M")), "wb") as file:
        file.write(photo)

def save_user(user):
    pass
