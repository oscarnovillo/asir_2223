from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from marshmallow import Schema, fields

# Define the MySQL engine using MySQL Connector/Python
engine = create_engine(
    'mysql+mysqlconnector://root:root@dam2.mysql.iesquevedo.es:3335/carlosmartin_tfc',
    echo=True)

# Define and create the table
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True)
    usuario = Column(String(length=200))
    password = Column(String(length=600))
    correo = Column(String(length=200))

    def __repr__(self):
        return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(
            self.usuario, self.password, self.correo)

app = Flask(__name__)
api = Api(app)


class UserSchema(Schema):
    id_usuario = fields.Number()
    usuario = fields.Str()
    password =fields.Str()
    correo = fields.Str()


class TodoSimple(Resource):
    def get(self):
        session = Session()

        exam_objects = session.query(User).all()

        # transforming into JSON-serializable objects
        schema = UserSchema(many=True)
        exams = schema.dump(exam_objects)

        # serializing as JSON
        session.close()
        return jsonify(exams)




api.add_resource(TodoSimple, '/')

if __name__ == '__main__':
    app.run(debug=True)