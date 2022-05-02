
from flask import Blueprint
from flask import current_app as app
from flask import request,make_response,jsonify
from app.database.db import db_con
from flask_restful import Resource, Api

rest_api = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static"
)


api = Api(app)

class Boraq_New(Resource):
    def get(self):
        myresult=db_con()
        mycursor = myresult.cursor(dictionary=True)
        mycursor.execute("SELECT * FROM admin_news")
        myresult = mycursor.fetchall()
        return jsonify({'daily':myresult})
  
class Register(Resource):
    def post(self):
        data = request.form.to_dict()
        if len(data['name-surname']) > 1 and len(data['mail']) > 1 and len(data['password']) > 1 :
            mydb=db_con()
            mycursor = mydb.cursor()
            sql = "INSERT INTO users (name_surname,mail, password) VALUES (%s, %s,%s)"
            val = (str(data['name-surname']), str(data['mail']),str(data['password']))
            mycursor.execute(sql, val)
            mydb.commit()
            return make_response(jsonify({'status': 'success'}), 200)
        else :
            return make_response(jsonify({'status': 'username , mail and password cannot be empty'}), 400)

api.add_resource(Boraq_New, '/v1/boraq/news/')
api.add_resource(Register, '/challange/register/')

