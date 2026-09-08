from flask import Flask, render_template, redirect, url_for
from routes.product_routes import product_bp
from routes.offer_routes import offer_bp
from routes.history_routes import history_bp
from routes.alert_routes import alert_bp
from routes.scrape_routes import scrape_bp

app = Flask(__name__)

app.register_blueprint(product_bp)
app.register_blueprint(offer_bp)
app.register_blueprint(history_bp)
app.register_blueprint(alert_bp)
app.register_blueprint(scrape_bp)


@app.errorhandler(Exception)
def handle_exception(e):
    return render_template("error.html", message=str(e)), 500

@app.route("/")
def index():
    return redirect(url_for("products.search_page"))

if __name__ == "__main__":
    app.run(debug=True)
