from flask import Flask, render_template
# import json

app = Flask(__name__)


@app.route('/')
def index():
    name = 'data1'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)


