from WebScraper import createEntry
import flask
from flask import request, jsonify
 
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])

def home():
    return jsonify(createEntry())

if __name__ == '__main__':
    app.run()
