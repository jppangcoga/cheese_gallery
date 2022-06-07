from flask import Flask, render_template
from cheeses import cheeses
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cheese/<cheese_type>')
def cheese(cheese_type):
    cheese_list = cheeses[cheese_type]
    return render_template('keso.html',cheese_type_template=cheese_type, cheese_type_template1=cheese_list)


@app.route('/cheese/<cheese_type>/<int:cheese_id>')
def cheese1(cheese_type, cheese_id):
    profile = cheeses[cheese_type][cheese_id]
    return render_template('content.html', profile=profile)


if __name__ == '__main__':
  app.run(debug=True)
