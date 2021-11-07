# Temporary code to test docker pipeline
# Stolen from: https://medium.datadriveninvestor.com/deploying-flask-web-app-on-microsoft-azure-89cea17e9114
from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/predict_api', methods=["GET","POST"])
def list_post():
    json_body = request.get_json()
    predictions = 2 * json_body[0]   
    predictions = list(predictions)
    return jsonify(results = predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)