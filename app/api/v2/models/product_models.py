import datetime
from psycopg2.extras import RealDictCursor

from ....utils.dbconnect import init_db
from .base_models import User

class ProductRecord():
    def __init__(self):
        self.db = init_db()
        self.get_data = User()

    def add_product(self, data,author):
         data = {
         "posted_on":datetime.datetime.now(),
         "user_id": self.get_data.get_user_details(author),
         "title": data['title'],
         "info": data['info'],
         "img": data['img'],
         "price" : data['price'],
         "company": data['company'],
         "quantity":data['quantity']
         }

         query = """INSERT INTO products(posted_on,u_id, title, \
         info,img,price,company,quantity)
         VALUES ('%s', '%s','%s', '%s', '%s','%s','%s','%s');""" % \
         (data['posted_on'],data['user_id'], data['title'], data['info'], data['img'],\
         data['price'], data['company'],data['quantity'])

         cur = self.db.cursor()
         cur.execute(query)
         self.db.commit()
         return data

    def get_all_products(self):
       query = """ SELECT * FROM products ORDER BY id DESC"""
       cur = self.db.cursor(cursor_factory=RealDictCursor)
       cur.execute(query)
       return cur.fetchall()

    def get_specific_product(self, id):
         query = "SELECT * FROM products WHERE id = '{}'".format(id)
         cur = self.db.cursor(cursor_factory=RealDictCursor)
         cur.execute(query)
         data =cur.fetchall()
         if data:
             return data
         else:
             return None

    def delete_product(self,id):
        query = " DELETE FROM products WHERE id={};".format(id)
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        return True
