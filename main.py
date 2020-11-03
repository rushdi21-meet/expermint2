from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
from database import *


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
#trying()
product_dict = {}
for u in session.query(Product).all():
    pro_dict = u.__dict__
    product_dict[u] = pro_dict
print(product_dict)



@app.route('/login', methods=['GET', 'POST'])
def login():
    # return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == exist(username, password):
            return redirect(url_for('admin'))
        else:
             return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('login'))
    else:
        return render_template('home.html')#,show_product=show_product())


@app.route('/store', methods=['GET', 'POST'])
def store():
    some_product_id = {}
    some_product_cost = 0
    if request.method == 'POST':
        new_id = request.form['ALEXANDER']
        new_id = int(new_id)
        #query_by_id(int(new_id))
        #print(query_by_id(new_id))
        #print(get_Cart())
        add_to_cart(new_id)
        some_product_id = get_Cart()
        some_product_cost = get_Cart_cost()
        print(some_product_id)
        print(some_product_cost)
        return render_template('store.html', product_dict=product_dict, ca_id=some_product_id, ca_co=some_product_cost)
        #get_Cart()
    if request.method == 'GET':
        delete_from_cart()
        #query_by_id()
        #get_Cart()
        return render_template('store.html', product_dict=product_dict, ca_id=some_product_id, ca_co=some_product_cost)
    else:
        return render_template('store.html', product_dict=product_dict, ca_id=some_product_id, ca_co=some_product_cost)


@app.route('/admin')
def admin():
    return render_template('admin.html', product_dict=product_dict)

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )