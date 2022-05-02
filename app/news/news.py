"""Product pages."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template
from app.database.db import db_con

# Blueprint Configuration
news_bp = Blueprint(
    "news_bp", __name__, template_folder="templates", static_folder="static"
)


@news_bp.route("/news/<int:product_id>/", methods=["GET"])
def product_page(product_id):

    # print(product_id)
    mydb=db_con()
    mycursor = mydb.cursor()
    mycursor.execute("select * from admin_news where id='" +
                                str(product_id)+"'")
    myresult=mycursor.fetchall()
    print(myresult)
    if myresult:
        return render_template("news_desc.html",news=myresult)
    
    