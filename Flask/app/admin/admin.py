from flask import Blueprint, render_template,request
from werkzeug.utils import secure_filename
from datetime import datetime
from app.database.db import connect

from app.schemas.admin_news import Admin_News
from app.schemas.users import Users
admin_bp = Blueprint(
    "admin_bp", __name__, template_folder="templates", static_folder="static"
)


UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# conn = db_engine.connect()  
@admin_bp.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method=='POST':
        email=request.form.get("email")
        password=request.form.get("pass")
        
        myresult=connect.execute(Users.select().where(Users.c.mail == email and Users.c.password == password)).fetchall()
        print(myresult)
        if myresult:
            return render_template("admin_index.html")
        else:
            return render_template("login.html")
    return render_template("login.html")

@admin_bp.route('/admin',methods = ['POST', 'GET'])
def admin():
    return render_template("admin_index.html")

@admin_bp.route('/save',methods = ['POST', 'GET'])
def save():
    if request.method=='POST':
        if request.form.get("button") == "value":
            file = request.files['file']
            yazar_Ad_soyad=request.form.get("isim_soyisim")
            konu=request.form.get("konu")
            baslik=request.form.get("baslik")
            mesaj=request.form.get("mesaj")
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save("./app/static/uploads/"+str(filename))
                file_url = "/static/uploads/"+filename
                datenow = datetime.now()
                connect.execute(Admin_News.insert().values(
                    isim_soyisim = yazar_Ad_soyad,
                    konu = konu,
                    baslik = baslik,
                    mesaj = mesaj,
                    image = file_url,
                    datetime = str(datenow)
                ))
            return render_template("admin_index.html")
    return render_template("admin_index.html")


@admin_bp.route('/news',methods = ['POST', 'GET'])
def news():
    myresult=connect.execute(Admin_News.select()).fetchall()
    print(myresult)
    if myresult:
        return render_template("news.html",myresult=myresult)
    return render_template("news.html")
