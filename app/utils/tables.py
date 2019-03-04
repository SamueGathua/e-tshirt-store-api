class Tables():
    """ Class to create tables """
    def table_queries(self):
        users="""CREATE TABLE IF NOT EXISTS users
        (
        id SERIAL PRIMARY KEY ,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR (50) NOT NULL,
        othername VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(250) NOT NULL,
        phonenumber VARCHAR(10),
        isadmin  BOOL ,
        registered_on TIMESTAMP
        )"""
        products="""CREATE TABLE IF NOT EXISTS products
        (
        id  SERIAL NOT NULL UNIQUE ,
        u_id INTEGER REFERENCES users(id),
        title VARCHAR(50) NOT NULL,
        info VARCHAR(50) NOT NULL,
        img VARCHAR(32) NOT NULL,
        price INT NOT NULL,
        posted_on TIMESTAMP,
        company VARCHAR (25) NOT NULL,
        quantity INT NOT NULL,
        PRIMARY KEY (Id, U_id)
        )"""

        self.query = [users,products]
        return self.query
