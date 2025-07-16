from flask import Flask, jsonify, request, make_response
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message='welcome')

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    return ''  # TODO: Return all products or filter by ?category=

# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404

@app.route("/products/<int:id>")
def get_product_by_id(id):
    return ''  # TODO: Return product by ID or 404

if __name__ == "__main__":
    app.run(debug=True)
