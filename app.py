'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask

from ProductionCode.datasource import DataSource

app = Flask(__name__)

@app.route('/')
def index():
    myds = DataSource()
    return "Welcome to the Pokemon API!"

if __name__ == '__main__':
    app.run(debug=True)