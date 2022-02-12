from flask import Flask
from routes import api_router


app = Flask(__name__)

api_router(app)

if __name__ == '__main__':
    app.run()
