
from flask import Blueprint
from flask import current_app as app
from flask import request,make_response,jsonify
from flask_restful import Resource, Api
from app.database.db import connect
from app.schemas.admin_news import Admin_News
from app.schemas.users import Users


rest_api = Blueprint(
    "api", __name__, template_folder="templates", static_folder="static"
)


api = Api(app)

class Boraq_New(Resource):
    def get(self):
        myresult=connect.execute(Admin_News.select()).fetchall()
        return jsonify({'daily':myresult})
  
class Register(Resource):
    def post(self):
        data = request.form.to_dict()
        if len(data['name-surname']) > 1 and len(data['mail']) > 1 and len(data['password']) > 1 :
            connect.execute(Users.insert().values(
                    name_surname = str(data['name-surname']),
                    mail = str(data['mail']),
                    password = str(data['password']),
                ))
            return make_response(jsonify({'status': 'success'}), 200)
        else :
            return make_response(jsonify({'status': 'username , mail and password cannot be empty'}), 400)

api.add_resource(Boraq_New, '/v1/boraq/news/')
api.add_resource(Register, '/challange/register/')

