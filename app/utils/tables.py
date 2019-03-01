class Tables():
    """ Class to create tables """
    def table_queries(self):
        users="""CREATE TABLE IF NOT EXISTS users
        (
        Id  SERIAL PRIMARY KEY ,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR (50) NOT NULL,
        OtherName VARCHAR(50) NOT NULL,
        Email VARCHAR(50) NOT NULL,
        Password VARCHAR(250) NOT NULL,
        PhoneNumber VARCHAR(10) NOT NULL,
        IsAdmin  BOOL ,
        RegisteredOn TIMESTAMP
        )"""
        products="""CREATE TABLE IF NOT EXISTS products
        (
        id  SERIAL NOT NULL UNIQUE ,
        u_id INTEGER REFERENCES users(Id),
        title VARCHAR(50) NOT NULL,
        info VARCHAR(50) NOT NULL,
        img VARCHAR(32) NOT NULL,
        price VARCHAR(32) NOT NULL,
        posted_on TIMESTAMP,
        company VARCHAR (25) NOT NULL,
        quantity VARCHAR (25) NOT NULL,
        PRIMARY KEY (Id, U_id)
        )"""

        self.query = [users,products]
        return self.query
