from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port='3306', password='root', database='test_db')

@app.route("/")
def hello():
    return "Flask inside Docker!!"

@app.route('/api/get/*', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_months():
    output_json = "no idea"
    db = getMysqlConnection()
    print(db)
    try:
        #sqlstr = "SELECT * from retail_table"
        sqlstr = "SELECT * from months"
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return jsonify(results=output_json)

@app.route('/api/get/months', methods=['GET'])
@cross_origin() # allow all origins all methods.
def get_months():
    output_json = "no idea"
    db = getMysqlConnection()
    print(db)
    try:
        #sqlstr = "SELECT * from retail_table"
        sqlstr = "SELECT * from months"
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return jsonify(results=output_json)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5003)