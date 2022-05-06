"""Product pages."""
from flask import Blueprint
from flask import render_template
from app.database.db import con
from app.schemas.admin_news import Admin_News
# Blueprint Configuration
news_bp = Blueprint(
    "news_bp", __name__, template_folder="templates", static_folder="static"
)

@news_bp.route("/news/<int:product_id>/", methods=["GET"])
def product_page(product_id):
    connect=con()
    myresult=connect.execute(Admin_News.select().where(Admin_News.c.id == str(product_id))).fetchall()
    if myresult:
        return render_template("news_desc.html",news=myresult)
    return render_template("news_desc.html")
    