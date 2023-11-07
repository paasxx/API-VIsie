from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from data import seed_data
from flask_marshmallow import Marshmallow
from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rg = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    date_birth = db.Column(db.DateTime, default=datetime.now)
    date_admission = db.Column(db.DateTime, default=datetime.now)
    role = db.Column(db.String(100))

    def __init__(self, name, rg, cpf, date_birth, date_admission, role):
        self.name = name
        self.rg = rg
        self.cpf = cpf
        self.date_birth = date_birth
        self.date_admission = date_admission
        self.role = role

    def create(self):
        new_user = Users(
            self.name,
            self.rg,
            self.cpf,
            self.date_birth,
            self.date_admission,
            self.role,
        )
        db.session.add(new_user)
        db.session.commit()


class UserHelper:
    def add_seed_data(seed_data):
        for data in seed_data:
            user_obj = Users(
                name=data[0],
                rg=data[1],
                cpf=data[2],
                date_birth=datetime.strptime(data[3], "%Y-%M-%d").date(),
                date_admission=datetime.strptime(data[4], "%Y-%M-%d").date(),
                role=None,
            )
            user_obj.create()
        print("Successfully Added")


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "rg", "cpf", "date_birth", "date_admission")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/listusers", methods=["GET"])
def listusers():
    all_users = Users.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)


@app.route("/userdetails/<id>", methods=["GET"])
def userdetails(id):
    user = Users.query.get(id)
    return user_schema.jsonify(user)


@app.route("/userupdate/<id>", methods=["PUT"])
def userupdate(id):
    user = Users.query.get(id)

    name = request.json["name"]
    rg = request.json["rg"]
    cpf = request.json["cpf"]
    date_birth = datetime.strptime(request.json["data_nascimento"], "%Y-%M-%d").date()
    date_admission = datetime.strptime(request.json["data_admissao"], "%Y-%M-%d").date()
    role = None

    user.name = name
    user.rg = rg
    user.cpf = cpf
    user.date_birth = date_birth
    user.date_admission = date_admission
    user.role = role

    db.session.commit()
    return user_schema.jsonify(user)


@app.route("/userdelete/<id>", methods=["DELETE"])
def userdelete(id):
    user = Users.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)


@app.route("/useradd", methods=["POST"])
def useradd():
    name = request.json["name"]
    rg = request.json["rg"]
    cpf = request.json["cpf"]
    date_birth = datetime.strptime(request.json["data_nascimento"], "%Y-%M-%d").date()
    date_admission = datetime.strptime(request.json["data_admissao"], "%Y-%M-%d").date()
    role = None

    users = Users(name, rg, cpf, date_birth, date_admission, role)
    db.session.add(users)
    db.session.commit()

    return user_schema.jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
