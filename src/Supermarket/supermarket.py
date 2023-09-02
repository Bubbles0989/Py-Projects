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
def start_up():
    return render_template(
        "base.html",
        title="Link Start",
    )   

@app.route("/supermarket")
def index():
    shop_items = { 'Cheese':4.99, 'Bread':6.99, 'Soup':3.99, 'Water':8.99 }

    return render_template(
        "index.html",
        title="Supermarket",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow(),
        shop_items=shop_items
    )

@app.route("/cart")
def cart():
    return render_template(
        "cart.html",
        title="Cart",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow()
    )

@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow()
    )