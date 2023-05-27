import flask
import flask_cors
import pandas as pd
import requests
import time
import json
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.route('/api/v1/surebets', methods=['GET'])
def get_surebets():
    df = 
    return df.to_json(orient='records')
    return df
