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
cart_items = {}
shop_registry = { 'Cheese':0, 'Bread':0, 'Soup':0, 'Water':0 }
shop_total = 0

@app.route("/", methods=['GET', 'POST'])
def index():
    shop_items = { 'Cheese':4.99, 'Bread':6.99, 'Soup':3.99, 'Water':8.99 }

    if request.method == 'POST':
        item = request.form.get('cart-button')
        split_items = item.split(',')
        cart_items[split_items[0]] = float(split_items[1])
        
        item_name = split_items[0]
        shop_registry[item_name] = shop_registry.get(item_name, 0) + 1

        flash(f'{split_items[0]} added to cart!', 'success')

    return render_template("index.html", shop_items=shop_items, shop_registry=shop_registry)

@app.route("/cart")
def cart():
    if len(cart_items) == 0:
        shop_total = 0
    else:
        shop_total = sum(cart_items.get(item, 0) * quantity for item, quantity in shop_registry.items())

    return render_template("cart.html", cart_items=cart_items, shop_registry=shop_registry, shop_total=shop_total)

@app.route("/about")
def about():
    return render_template(
        "about.html",
        greeting_name="Guest",
        datetime_object=datetime.datetime.utcnow()
    )