import sqlite3


class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()


    def save_data(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER,
          is_bot TEXT,
          first_name TEXT,
          username TEXT,
          language_code TEXT
        );
        """


    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM sound').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum"""
        with self.connection:
            return self.cursor.execute('SELECT * FROM sound WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM sound').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение"""
        self.connection.close()