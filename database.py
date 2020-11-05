from sqlalchemy.testing import db
from flask import Flask, jsonify, request, render_template, redirect, url_for
from sqlalchemy.sql import exists

from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///Product_DB.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def query_all():
    """
    Print all the students
    in the database.
    """
    products = session.query(Product).all()
    return products


#print(query_all())

def query_by_name(their_name):
    """
    Find the first student
    in the database, by their name
    """
    try :
        product = session.query(Product).filter_by(name=their_name).first()
        return product.name
    except:
        return ("no such product")

#print(query_by_name("Milk"))

def query_by_desc(their_describtion):
    """
    Find the first student
    in the database, by their name
    """
    try :
        product = session.query(Product).filter_by(describtion=their_describtion).first()
        return product.describtion
    except:
        return ("no such product")


def query_by_img(their_image):
    """
    Find the first student
    in the database, by their name
    """
    try :
        product = session.query(Product).filter_by(img=their_image).first()
        return product.img
    except:
        return ("no such product")


def query_by_id(thier_id):
   # try:
    product = session.query(Product).filter_by(id=thier_id).first()
    return product.name
    #except:
        #return print("no such id")
#newid=3
#print(type(newid))
#query_by_id(newid)


def query_by_id_price(thier_id):
   # try:
    product = session.query(Product).filter_by(id=thier_id).first()
    return product.price


def add_product(name, describtion, img, price, release_date, company, discount, available):
    try:
        """
        Add a student to the database, given
        their name, year, and whether they have
        finished the lab.
        """
        if name != query_by_name(name):
            if describtion != query_by_desc(describtion):
                if img != query_by_img(img):
                    if available == 'True':
                        new_product = Product(name=name, describtion=describtion, img=img, price=price, release_date=release_date, company=company, discount=discount, available=True)
                        session.add(new_product)
                        session.commit()
                        return print("new product added!")
                    elif available == 'False':
                        new_product = Product(name=name, describtion=describtion, img=img, price=price,
                                              release_date=release_date, company=company, discount=discount,
                                              available=False)
                        session.add(new_product)
                        session.commit()
                        return print("new product added!")
                    else:
                        return print("error!")
                else:
                    return print("an existing product has the same image!")
            else:
                return print("an existing product has the same description!")
        else:
            return print("an existing product has the same name!")
    except:
        print("Coudln't add product")


add_product("Milk", "quality milk by Tnuva.", "https://bestandkosher.com/wp-content/uploads/2018/03/1-liter-milk-tnuva.jpg", 8, "27-10-2020", "Tnuva", 15.5, True)
#print(query_by_name("Milk"))
add_product("Water", "quality water by san benedetto.", "https://cdn11.bigcommerce.com/s-4yzmyxd47t/images/stencil/2048x2048/products/3132/3198/833982__08374.1586270797.jpg?c=1", 6, "27-10-2020", "san benedetto", 15.5, True)
add_product("Bread", "Crunchy hot bread from our bakery.", "https://i1.wp.com/gatherforbread.com/wp-content/uploads/2015/08/Easiest-Yeast-Bread.jpg?resize=500%2C500&ssl=1", 4, "27-10-2020", "Meet's Bakery", None, True)
add_product("Cereal", "The most delicious cereal made by Cornflakes", "https://target.scene7.com/is/image/Target/GUEST_61638d6a-b11c-4f1c-ab3f-9d9cff905ac3?wid=488&hei=488&fmt=pjpeg", 12, "27-10-2020", "Cornflakes", None, False)
#add_product("hi", "The most delicious cereal made by Cornflakes", "https://target.scene7.com/is/image/Target/GUEST_61638d6a-b11c-4f1c-ab3f-9d9cff905ac3?wid=488&hei=488&fmt=pjpeg", 12, "27-10-2020", "Cornflakes", None, False)
def dict_a_product():
    product_dict = {}
    for u in session.query(Product).all():
        pro_dict = u.__dict__
        product_dict[u] = pro_dict
    print(product_dict)
    return product_dict


def update_products_availability(name, available):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        if available == "True":
            product.available = True
            session.commit()
        elif available == "False":
            product.available = False
            session.commit()
        else:
            return print("Couldn't update availbilty even after passing the try")
    except:
        #session.rollback()
        return print("Could't Update Availabity")

def update_products_release_date(name, release_date):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.release_date = release_date
        session.commit()
    except:
        return print("couldn't update release_date")

def update_products_discount(name, discount):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.discount = discount
        session.commit()
    except:
        return print("couldn't update discount")

def update_products_company(name, company):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.company = company
        session.commit()
    except:
        return print("Couldn't update company")

def update_products_price(name, price):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.price = price
        session.commit()
    except:
        return print("Couldn't update price")

def update_products_img(name, img):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.img = img
        session.commit()
    except:
        return print("Couldn't update image")

def update_products_describtion(name, describtion):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.describtion = describtion
        session.commit()
    except:
        return print("Couldn't update description")

def update_products_name(name, new_name):
    try:
        """
        Update a student in the database, with
        whether or not they have finished the lab
        """
        product = session.query(Product).filter_by(name=name).first()
        product.name = new_name
        session.commit()
    except:
        return print("Couldn't update name")

#update_products_availability("Milk", False)


def delete_product(their_name):
    try:
        """
        Delete all students with a
        certain name from the database.
        """
        session.query(Product).filter_by(name=their_name).delete()
        session.commit()
    except:
        return print("Couldn't delete product")


#delete_product("try")
#delete_product("Water")
#delete_product("Bread")

def add_to_cart(productID):
    new_to_cart = Cart(productID=productID)
    session.add(new_to_cart)
    session.commit()
#add_to_cart(2)

def get_Cart():
    cart_dict={}
    for u in session.query(Cart).all():
        car_dict = u.__dict__
        its_name = car_dict['productID']
        is_name = query_by_id(its_name)
        cart_dict[u] = is_name
    return cart_dict
print(get_Cart())


def get_Cart_cost():
    sum=0
    for u in session.query(Cart).all():
        car_dict = u.__dict__
        its_id = car_dict['productID']
        is_id = query_by_id_price(its_id)
        sum+=is_id
    return sum
#print(get_Cart())


def delete_from_cart():
    for u in session.query(Cart).all():
        session.query(Cart).delete()
        session.commit()
#delete_from_cart()

def query_by_name_admin(their_name):
    """
    Find the first student
    in the database, by their name
    """
    try :
        admin = session.query(Admin).filter_by(username=their_name).first()
        return admin.username
    except:
        return print("no such Admin")


def query_by_pass_admin(thier_pass):
    try:
        admin = session.query(Admin).filter_by(password=thier_pass).first()
        return admin.password
    except:
        return print("no such password")


def add_admin(user, passw):
    if (user != query_by_name_admin(user)) and (passw != query_by_pass_admin(passw)):
        new_user = Admin(username=user, password=passw)
        session.add(new_user)
        session.commit()
        return print("new Admin added!")
    else:
        return print("Admin already exist")


def delete_Admin(their_user):
    """
    Delete all students with a
    certain name from the database.
    """
    session.query(Admin).filter_by(username=their_user).delete()
    session.commit()

#delete_Admin("rushdid")
#query_by_name_admin("rushdid")


def problem (username, password):
    if username == query_by_name_admin(username):
        delete_Admin(username)
        add_admin(username, password)
    else:
        add_admin(username, password)

problem("rushdid", "1442004r")
problem("daqar", "rushdid")
def exist(username, password):
    #q = session.query(Admin).filter(Admin.username == username)
    #p = session.query(Admin).filter(Admin.password == password)
    try:
        admins_dict = {}
        for u in session.query(Admin).all():
            ad_dict = u.__dict__
            if username == ad_dict['username'] and password == ad_dict['password']:
                return username
            admins_dict[u] = ad_dict
        return admins_dict
        '''print(session.query(Admin).filter_by(username=username).first())
        if username == session.query(Admin).filter_by(username=username).first():
            if password == session.query(Admin).filter_by(password=password).first():
                return username
            else:
                return print("no such password")
        else:
            return print("no such Admin")'''
    except:
        return print("didn't work")


def show_product():
    obj = session.query(Product).all()
    return str(obj[-1].name)


def show_product2():
    obj = session.query(Product).all()
    return str(obj[-2].name)

def show_product3():
    obj = session.query(Product).all()
    return str(obj[-3].name)

def trying():
    for u in session.query(Product).all():
        i = u.__dict__
        print(i)
