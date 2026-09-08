from flask import Blueprint, render_template, request
from services.scraper_service import scrape_products
from services.product_service import upsert_offer, upsert_product
from repositories.product_repo import all_products, nr_products
import traceback

product_bp = Blueprint("products", __name__)



@product_bp.route("/dbproducts")
def dbproducts_page():
    products = all_products()
    nr = nr_products()
    return render_template("allproducts.html", products=products, nr_products = nr)

@product_bp.route("/search")
def search_page():
    try:
        q = request.args.get("q")
        print(f'search: {q}')
        products = []
        html_products = []

        if q:
            products = scrape_products(q)["products"]

            for product_data in products:
                product = None

                if "pid" in product_data or "gpcid" in product_data:
                    product = upsert_product(product_data)

                if product:
                    # Adaugă produsul în lista pentru HTML
                    html_products.append(product)
    except Exception as e:
        print("Exception in ProductRoutes: ",e)
        traceback.print_exc()

    return render_template("search.html", products=html_products)

    return render_template("search.html", products=products)
#return render_template("error.html", message="Product not found")


