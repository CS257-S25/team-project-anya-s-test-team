'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask, request, render_template

from ProductionCode.datasource import DataSource

app = Flask(__name__)
ds = DataSource()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon/<name>/')
def display(name):
    # Using 'name' from the URL to match the 'poke_name' logic
    result = ds.get_pokemon_by_name(name)
    if result:
        return result
    else:
        return "No pokemon!"
    
@app.route('/d3example')
def display_d3():
    return render_template('d3_example.html')


@app.route('/displayrow')
def display_row():
    row = request.args['rowchoice']

    return "Your pokemon: " + row


if __name__ == '__main__':
    app.run()