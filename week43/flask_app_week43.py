from flask import Flask, jsonify, abort, request
import sqlalchemy as s_a
from sqlalchemy import MetaData

app = Flask(__name__)

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@db/db"
engine = s_a.create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.connect()
metadata = MetaData()
metadata.reflect(bind=engine)
people_table = metadata.tables['people']

def query_to_dict(ret):
    if ret is not None:
        return [{key: value for key, value in row.items()} for row in ret if row is not None]
    else:
        return [{}]

@app.route('/api/showall', methods=['GET'])
def get_people():
  query = 'select * from people'
  result_proxy = connection.execute(query)
  result = [dict(row) for row in result_proxy]
  return jsonify(result)

@app.route('/api/employee/<string:firstName>/<string:lastName>', methods=['GET'])
def search_employee(firstName, lastName):
  query = F"SELECT * FROM people WHERE FirstName = '{firstName}' AND LastName = '{lastName}'"
  result_proxy = connection.execute(query)
  result = [dict(row) for row in result_proxy]
  return jsonify(result)


@app.route('/api/employee', methods=['POST'])
def create_employee():
    if not request.json:
        abort(400)
    person = {
        'FirstName': request.json['FirstName'],
        'LastName': request.json['LastName'],
        'Gender': request.json['Gender'],
        'Age': request.json['Age'],
        'Email': request.json['Email'],
        'Phone': request.json['Phone'],
        'Occupation': request.json['Occupation'],
        'Salary': request.json['Salary']
    }
    insert = people_table.insert().values(person)
    connection.execute(insert)

    return jsonify(person), 201

@app.route('/api/employee/<string:lastName>', methods=['DELETE'])
def delete_employee(lastName):
  del_st = people_table.delete().where(people_table.c.LastName == lastName)
  connection.execute(del_st)
  return jsonify({'result': True})

@app.route('/api/employee', methods=['PUT'])
def update_employee():
  if not request.json:
        abort(400)
  person = {
        'FirstName': request.json['FirstName'],
        'LastName': request.json['LastName'],
        'Gender': request.json['Gender'],
        'Age': request.json['Age'],
        'Email': request.json['Email'],
        'Phone': request.json['Phone'],
        'Occupation': request.json['Occupation'],
        'Salary': request.json['Salary']
  }
  update = people_table.update().where(people_table.c.LastName == person['LastName']).values(person)
  connection.execute(update)

  return jsonify(person), 201