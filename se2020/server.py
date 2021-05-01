from flask import Flask, jsonify
from se2020.morse import encode_morse
import os
import sys
import psycopg2 as dbapi2



app = Flask(__name__)


@app.route("/")
def hello():
     #print(url)
    #song = initialize()
    initialize()
    #payload = {"result": song} 
    payload = {"result": "success"} 
    return jsonify(payload)


@app.route("/morse/<phrase>")
def encode(phrase):
    payload = {"result": encode_morse(phrase)}
    return jsonify(payload)

"""
def initialize():
	
	conn = dbapi2.connect(
    host="localhost",
    #database="whoisplayingtest",
    #user="pinarkaragulle",
    #password="Sept2409!")
    
	#cursor = conn.cursor()
	#cursor.execute("select name from musicrecord;")
	
	
	database="postgres",
    user="postgres",
    password="docker")
    
	cursor = conn.cursor()
	cursor.execute("select	num from dummy;")
	
	
	songname = cursor.fetchone();
	cursor.close()
	return songname
"""

INIT_STATEMENTS = [
    "CREATE TABLE IF NOT EXISTS DUMMY (NUM INTEGER)",
    "INSERT INTO DUMMY VALUES (42)",
]


def initialize():
    #url = os.getenv("DATABASE_URL")
    #url = "postgres://postgres:docker@localhost:5432/postgres"
    #url = "postgres://hxbrdgsplefsjq:ab12a73c25580b6ad7006dd8f483ebef05017d0bd46fe195d26bc4fef3d319cb@ec2-34-230-115-172.compute-1.amazonaws.com:5432/d5nsvu5k5r17qb"
    
    #app.config.from_object('se2020.default_settings')
    
    url = os.getenv("DATABASE_URL")
    print(url) 
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()
    
