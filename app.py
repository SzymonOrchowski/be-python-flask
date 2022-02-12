import psycopg2
import json
from flask import Flask, request, jsonify
from config import config

app = Flask(__name__)

@app.route("/api/recipes", methods=['GET'])
def getRecipes():
    sqlQuery = 'SELECT * FROM recipes'

    userQueries = request.args.get('exclude_ingredients')

    if userQueries != None:
        excludedIngredients = userQueries.split(',')
        
        for ingredient in excludedIngredients:
            if ingredient[len(ingredient) - 1] == 's':
                excludedIngredients[excludedIngredients.index(ingredient)] = ingredient[:-1]
        
        sqlQuery += ' WHERE '
        
        for ingredient in excludedIngredients:
            sqlQuery += f" ingredients NOT LIKE '%''{ingredient}''%' "
            if excludedIngredients.index(ingredient) != len(excludedIngredients) -1:
                sqlQuery += "AND"
    
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sqlQuery)
    rows = cur.fetchall()
    cur.close()
    conn.commit()

    recipes = []
    
    for recipe in rows:
        properListOfingredients = []

        splitIngredientsList = recipe[4][1:-1].split('}, ')

        for ingredient in splitIngredientsList:
            if splitIngredientsList.index(ingredient) != len(splitIngredientsList) - 1:
                splitIngredientsList[splitIngredientsList.index(ingredient)] += '}'

        for ingredient in splitIngredientsList:
            properListOfingredients.append(json.loads(ingredient.replace("\'", "\"")))

        recipes.append({
            "id": recipe[0],
            "originalId": recipe[1],
            "imageUrl": recipe[2],
            "instructions": recipe[3],
            "ingredients": properListOfingredients,
        })

    return jsonify(recipes)

@app.route("/api/recipes/<id>", methods=['GET'])
def getRecipeById(id):
    sqlQuery = f'SELECT * FROM recipes WHERE id = {id}'

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sqlQuery)
    rows = cur.fetchall()
    cur.close()
    conn.commit()

    recipes = []
    
    for recipe in rows:
        properListOfingredients = []

        splitIngredientsList = recipe[4][1:-1].split('}, ')

        for ingredient in splitIngredientsList:
            if splitIngredientsList.index(ingredient) != len(splitIngredientsList) - 1:
                splitIngredientsList[splitIngredientsList.index(ingredient)] += '}'

        for ingredient in splitIngredientsList:
            properListOfingredients.append(json.loads(ingredient.replace("\'", "\"")))

        recipes.append({
            "id": recipe[0],
            "originalId": recipe[1],
            "imageUrl": recipe[2],
            "instructions": recipe[3],
            "ingredients": properListOfingredients,
        })

    return jsonify(recipes)

