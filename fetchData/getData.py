from flask import Flask, render_template, request, json
import json

app = Flask(__name__)

data_list = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {}
        data['id'] = len(data_list) + 1
        data['title'] = request.form['title']
        data['content'] = request.form['content']


        data_list.append(data)

    return render_template('data.html', data=data_list)


@app.route('/save')
def save_data():
    json_data = json.dumps(data_list)

    with open('data.json', 'w') as f:
        f.write(json_data)

    return "Data saved to file."

#not in use
@app.route('/load')
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080, debug=True)
