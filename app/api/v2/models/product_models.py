import datetime
from .base_models import BaseModels

class ProductRecord(BaseModels):
    """ Constructor that calls the Constructor in BaseModels"""
    def __init__(self):
        self.records = BaseModels('products')
        self.check = BaseModels('users')


    def add_product(self, data, author):
        """ create a new product record """
        user_data = self.check.get_data("email",author)
        data = {
            "u_id" :user_data['id'],
            "title": data['title'],
            "info": data['info'],
            "img" : data['img'],
            "price" : data['price'],
            "posted_on" : datetime.datetime.now(),
            "company" : data['company'],
            "quantity" : data['quantity']
            }
        query = """INSERT INTO products(u_id, title, info, img, price,posted_on,\
        company,quantity)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % \
        (data['u_id'], data['title'], data['info'], data['img'], data['price'],\
        data['posted_on'],data['company'],data['quantity'])
        record = self.records.save(query, data)
        return record


    def get_all_products(self):
       return self.records.get_all_records()

    def get_specific_product(self,id):
        return self.records.get_data("id",id)


    def delete_product(self,id):
        return self.records.delete("id",id)
