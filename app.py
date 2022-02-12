import psycopg2
from flask import Flask, request, jsonify
from config import config

app = Flask(__name__)

@app.route("/api/recipes", methods=['GET'])
def getRecipes():
    userQueries = request.args.get('exclude_ingredients').split(',')
    for ingredient in userQueries:
        if ingredient[len(ingredient) - 1] == 's':
            userQueries[userQueries.index(ingredient)] = ingredient[:-1]

    sqlQuery = 'SELECT * FROM recipes'
    if len(userQueries) > 0:
        sqlQuery += ' WHERE '
        for ingredient in userQueries:
            sqlQuery += f" ingredients NOT LIKE '%''{ingredient}''%' "
            if userQueries.index(ingredient) != len(userQueries) -1:
                sqlQuery += "AND"
    
    print(sqlQuery)
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sqlQuery)
    rows = cur.fetchall()
    cur.close()
    conn.commit()

    return jsonify(rows)
