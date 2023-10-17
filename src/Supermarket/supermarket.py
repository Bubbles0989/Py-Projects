import datetime
from flask import Flask
from flask_bootstrap import Bootstrap
from flask import flash, redirect, render_template, request, url_for
from config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.secret_key = SECRET_KEY
cart_items = []

@app.route("/", methods=['GET', 'POST'])
def index():
    shop_items = { 'Cheese':4.99, 'Bread':6.99, 'Soup':3.99, 'Water':8.99 }

    if request.method == 'POST':
        item = request.form.get('cart-button')
        split_items = item.split(',')
        for string in split_items:
            cart_items.append(string)

        flash(f'{split_items[0]} added to cart!', 'success')

    return render_template("index.html", shop_items=shop_items)

@app.route("/cart")
def cart():
    return render_template("cart.html", cart_items=cart_items)

@app.route("/about")
def about():
    return render_template(
        "about.html",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow()
    )