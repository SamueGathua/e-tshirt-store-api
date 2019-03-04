""" Local imports """
from ....utils.dbconnect import init_db
from psycopg2.extras import RealDictCursor


class BaseModels():
    ''' Constructor that creates a connection and initilizes an instant variable table_name'''
    def __init__(self, record):
        self.connection = init_db()
        self.table_name = record


    def get_data(self, key, value):
        ''' Find an item with a specific key and value'''
        query = """ SELECT * FROM {} WHERE {}='{}'""".format(self.table_name, key, value)
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        data = cur.fetchone()
        if data is not None:
            return data
        return None

    def get_all_records(self):
        ''' Returns all records'''
        query = """ SELECT * FROM {} """.format(self.table_name)
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        return cur.fetchall()

    def save(self, query, data):
        ''' Inserts data to the database'''
        save = self.connection
        cur = save.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        save.commit()
        return data


    def delete(self, key, value,):
        query = """ SELECT * FROM {} WHERE {}='{}'""".format(self.table_name, key, value)
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        delete_data =cur.fetchone()
        query = """ DELETE  FROM {} WHERE {}='{}'""".format(self.table_name, key, value)
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        self.connection.commit()
        return delete_data

    def check_exists(self, key, value):
        ''' Check if an item exists in the database '''
        query = """ SELECT EXISTS (SELECT * FROM {} WHERE {}='{}');""" \
                    .format(self.table_name, key, value)
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        found = cur.fetchone()
        return found
