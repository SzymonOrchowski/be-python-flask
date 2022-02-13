<h1>CRUD RESTful API in Python/Flask and Postgres</h1>

<h2>How to setup a project</h2>

Minimum setup requirements:

Python 3.9.2<br/>
Flask 2.0.2<br/>
PostgreSQL 13.4<br/>
psycopg2 2.9.3

1. Fork and clone this repository.
2. Install PostgreSQL, Flask and pytest
3. Install psycopg2-binary (a PostgreSQL database adapter for the Python) - https://www.psycopg.org/docs/install.html
<h2>How to run the project</h2>

Go to the main folder of the repo and run following command: <br/>
<i>(make sure that you don't already have a database called "backend_recipes", and any valuable data in it, otherwise, after that command you will lost them)</i>
>  psql -f data/setup.sql

Seed the data from json file to posgresql by running script: <br/>
<i>(make sure you have postgres configuration settings properly set in "database.ini" file)</i>
> python3 seeding.py

You can run the current test suite by:
> pytest tests/tests.py -v

You can run the server by command:
> flask run

It will react on port 5000 localhost on following endpoints (you can test the using e.g Insomnia):<br/>
>localhost:5000/api/recipes <br/>
>localhost:5000/api/recipes/:id

<h1>Endpoints:</h1>

<h3>/api/recipes</h3>

GET - return all recipes from the database

it takes query of "exclude_ingredients" to exclude recipes that has certain ingredients (separated by commas)
example:
> /api/recipes?exclude_ingredients=bananas,strawberries,coffee,milk,oat milk,apple juice

POST - you can add a recipe to the database

request should include a JSON object that looks like following example:

```json
{
	"recipe": {
		"imageUrl": "http://www.images.com/13456734567",
		"instructions": "instructions",
		"ingredients": [
			{ "name": "ingredient1", "grams": 25},
			{ "name": "ingredient2", "grams": 66},
			{ "name": "ingredient3", "grams": 44},
			{ "name": "ingredient4", "grams": 198}
		]
	}
}
```


<h3>/api/recipes/:id</h3>

GET - return a single recipe of a given id from the database
