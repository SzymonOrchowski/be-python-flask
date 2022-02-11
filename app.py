import psycopg2
from flask import Flask, request, jsonify
from config import config

app = Flask(__name__)

@app.route("/api/recipes", methods=['GET'])
def getRecipes():
    queries = ('SELECT * FROM recipes',)
    
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(queries[0])
    rows = cur.fetchall()
    cur.close()
    conn.commit()

    return jsonify(rows)