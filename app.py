from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__)

api_response = []

@app.route('/')
def index():
    json_keys = []

    # get the data from the API and append it to the list
    for index in range(11):
        request = requests.get("http://www.boredapi.com/api/activity/")
        json = request.json()
        if index == 0:
            for key in json.keys():
                json_keys.append(key)
            continue
        api_response.append(json)
    return render_template('index.html', response=api_response, keys=json_keys)

@app.route('/clear_table', methods=['GET', 'POST'])
def clear_table():
    api_response = []
    return ""

if __name__ == '__main__':
    app.run(debug=True)