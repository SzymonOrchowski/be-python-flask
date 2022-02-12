from flask import request, jsonify
from models import getAllRecipes, fetchRecipeById, addRecipe

def api_router(app):
    @app.route("/api/recipes", methods=['GET', 'POST'])
    def manageAllRecipes():
        if request.method == 'GET':
            recipes = getAllRecipes()
            return jsonify(recipes), 200
        if request.method == 'POST':
            data = request.json['recipe']
            return addRecipe(data), 201

    @app.route("/api/recipes/<id>", methods=['GET'])
    def getRecipeById(id):
        recipe = fetchRecipeById(id)
        return jsonify(recipe), 200
