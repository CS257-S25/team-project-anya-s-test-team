'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask, request, render_template

#from ProductionCode.datasource import DataSource

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display')
def display():
    return render_template('d3_example.html')

@app.route('/displayrow')
def display_row():
    row = request.args['rowchoice']

    return "Your pokemon: " + row


if __name__ == '__main__':
    app.run(debug=True)