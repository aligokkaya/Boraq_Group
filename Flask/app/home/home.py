
from flask import Blueprint
from flask import current_app as app
from flask import render_template
from app.news_api import fetch_products
import json 
from app.database.db import con
from app.schemas.admin_news import Admin_News




home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    news = fetch_products(app)
    news=json.loads(news)
    # print((news['result'][0]))


    return render_template(
        "index.html",
        news=news['result'],
    )


@home_bp.route("/adminnews", methods=["GET"])
def adminnews():
    try:
        connect=con()
        myresult=connect.execute(Admin_News.select()).fetchall()
        # print(myresult)
        if myresult:
            return render_template("admin_newlist.html",news=myresult)
    except:
        return render_template("admin_newlist.html")
