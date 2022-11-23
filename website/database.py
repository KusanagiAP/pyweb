import sqlite3
from main import *
from flask import flash

conn =  sqlite3.connect('products.db')

c = conn.cursor()

'''
c.execute(""" CREATE TABLE  products (
            name text,
            price integer
        )  """)
'''
c.execute("SELECT * FROM products")

if request.method == 'POST':
    existence = False

    for name in c:
        if name[0] == request.form["product"]:
            existence = True

    if existence:
        notification('This item already exist !! ','error')
    else:
        notification('Item added successfully','success')
        # command = "INSERT... " % username  # <-- Vulnerable
        # c.execute(command)
        c.execute (" INSERT INTO products VALUES (?,?)",[request.form["product"],request.form["price"]]) # dynamic query prepared statement 

#products = c.execute("SELECT * FROM products").fetchall()

    

conn.commit()

conn.close()


