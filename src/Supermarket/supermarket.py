import datetime
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import flash, redirect, render_template, request, url_for

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()

@app.route("/")
def index():
    shop_items = { 'Cheese':4.99, 'Bread':6.99, 'Soup':3.99, 'Water':8.99 }

    return render_template(
        "index.html",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow(),
        shop_items=shop_items
    )

@app.route("/cart")
def cart():
    cart_items = { 'Cheese':4.99, 'Bread':6.99 }

    return render_template(
        "cart.html",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow(),
        cart_items=cart_items
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow()
    )