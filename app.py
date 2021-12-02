dummy_data = [
    {"id": 1, "name": "Cloth A", "description": "Sample Description Text", "price": 100000, "img": "clothes.jpg"},
    {"id": 2, "name": "Food B", "description": "Sample Description Text", "price": 50000, "img": "foods.jpg"},
    {"id": 3, "name": "Gadget C", "description": "Sample Description Text", "price": 500000, "img": "gadgets.jpg"}
]

from flask import Flask
from flask import render_template, url_for, make_response, request

app = Flask(__name__)

def get_utm(response):
    args = request.args
    if ("utm_source" in args) or ("utm_medium" in args) or ("utm_campaign" in args):
        source = args.get("utm_source", "")
        response.set_cookie("utm_source", source)

        medium = args.get("utm_medium", "")
        response.set_cookie("utm_medium", medium)

        campaign = args.get("utm_campaign", "")
        response.set_cookie("utm_campaign", campaign)
        
    return response

@app.route("/")
def home():
    response = make_response(render_template("home.html", products = dummy_data))
    response = get_utm(response)

    return response

@app.route("/product/<product_id>")
def product(product_id):
    product = list(filter(lambda prd: prd["id"] == int(product_id), dummy_data))
    product = product[0] if (product) else None
    return render_template("product.html", product = product)

@app.route("/cookie")
def get_cookie():
    cookie = request.cookies
    return cookie


if __name__ == "__main__":
    app.run(debug=True)
