#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

from unicodedata import category
from flask import Flask,render_template,request,flash
import sqlite3

app = Flask (__name__) # name of the file
app.config['SECRET_KEY'] = 'oFNboLHe3HIO7GgUI4Vf' # config variable encrypt data

def notification(content,categroy):
    return flash(content,category=category)


@app.route('/')

@app.route('/home')
def home():
    return render_template("home.html",content = "home")

@app.route('/products', methods=['GET','POST'])
def search():
    conn =  sqlite3.connect('products.db')
    c = conn.cursor()

    products = c.execute("SELECT * FROM products").fetchall()
    #print(products)
    if request.method == 'POST':
        for product in products:
            if product[0] == request.form["search"]:
                return render_template("products.html",result = [product[0],product[1]])
        notification('Product doesn\'t exist','error')
    return render_template("products.html", products = products,result=None)

@app.route('/add',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        if request.form["product"] == "":
            notification('Name of the product cannot be empty !','error')
        elif request.form["price"].isnumeric() == False:
            notification('You must give a price to your product !','error')
        else:
            exec(open("website/database.py").read())
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)

    


