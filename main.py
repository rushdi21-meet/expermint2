from flask import Flask, jsonify, request, render_template, redirect, url_for
import random
from database import *


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
#trying()




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
    product_dict = dict_a_product()
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


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    product_dict = dict_a_product()
    if request.method == 'POST':
        try:
            deleted_pro = request.form['deleted_pro']
            delete_product(deleted_pro)
            product_dict = dict_a_product()
            print("exuted")
        except:
            try:
                former_name = request.form['former_name']
                new_name = request.form['new_name']
                former_description = request.form['former_description']
                new_description = request.form['new_description']
                former_img = request.form['former_img']
                new_img = request.form['new_img']
                former_price = request.form['former_price']
                new_price = request.form['new_price']
                former_release_date = request.form['former_release_date']
                new_release_date = request.form['new_release_date']
                former_company = request.form['former_company']
                new_company = request.form['new_company']
                former_discount = request.form['former_discount']
                new_discount = request.form['new_discount']
                former_available = request.form['former_available']
                new_available = request.form['new_available']
                update_products_name(former_name, new_name)
                update_products_describtion(former_description, new_description)
                update_products_img(former_img, new_img)
                update_products_price(former_price, new_price)
                update_products_release_date(former_release_date, new_release_date)
                update_products_company(former_company, new_company)
                update_products_discount(former_discount, new_discount)
                update_products_availability(former_available, new_available)
                product_dict = dict_a_product()
            except:
                its_name = request.form['its_name']
                its_description = request.form['its_description']
                its_img = request.form['its_img']
                its_price = request.form['its_price']
                its_release_date = request.form['its_release_date']
                its_company = request.form['its_company']
                its_discount = request.form['its_discount']
                its_availability = request.form['its_availability']
                add_product(its_name, its_description, its_img, its_price, its_release_date, its_company, its_discount, its_availability)
                product_dict = dict_a_product()
        return render_template('admin.html', product_dict=product_dict)
    else:
        return render_template('admin.html', product_dict=product_dict)

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
        port=random.randint(2000, 9000),  # Randomly select the port the machine hosts on.
        debug=True
    )