from flask import Flask
import json

from routes import api_router

def test_base_route():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 404

################################

def test_get_all_recipes_respond_with_code_200_and_list_of_recipes():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/api/recipes'

    response = client.get(url)
    decoded_response = response.get_data().decode("utf-8")
    parsed_repsonse = json.loads(decoded_response)

    assert response.status_code == 200
    assert isinstance(parsed_repsonse, list)

def test_get_all_recipes_respond_with_list_of_dictionaries():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/api/recipes'

    response = client.get(url)
    decoded_response = response.get_data().decode("utf-8")
    parsed_repsonse = json.loads(decoded_response)

    for single in parsed_repsonse:
        assert isinstance(single, dict)

def test_get_all_recipes_respond_with_dictionaries_that_has_all_keys():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/api/recipes'

    response = client.get(url)
    decoded_response = response.get_data().decode("utf-8")
    parsed_repsonse = json.loads(decoded_response)

    for recipe in parsed_repsonse:
        assert 'id' in recipe
        assert 'imageUrl' in recipe
        assert 'instructions' in recipe
        assert 'ingredients' in recipe
   

################################

def test_get_recipe_by_ID_respond_with_a_list_includes_single_object():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/api/recipes/1'

    response = client.get(url)
    decoded_response = response.get_data().decode("utf-8")
    parsed_repsonse = json.loads(decoded_response)
    
    assert response.status_code == 200
    assert len(parsed_repsonse) == 1

def test_get_recipe_by_ID_respond_with_a_recipe_with_proper_id():
    app = Flask(__name__)
    api_router(app)
    client = app.test_client()
    url = '/api/recipes/12'

    response = client.get(url)
    decoded_response = response.get_data().decode("utf-8")
    parsed_repsonse = json.loads(decoded_response)
    
    assert parsed_repsonse[0]['id'] == 12

