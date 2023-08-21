from flask import Flask, jsonify
from flask import render_template

import openai
openai.api_key = "YOUR_API_KEY"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generateimages/<prompt>')
def generateImages(prompt):
    response = openai.Image.create(prompt=prompt,
                               n=1,
                               size="512x512")
    return jsonify(response)


app.run(host='0.0.0.0', port=81)
