from flask import Flask, render_template

app = Flask(__name__, template_folder='C:\\Users\\Ricky\\PycharmProjects\\jinja\\ricky_test')


@app.route('/')
def index():
    return render_template('base.html', lst=[10])


app.run(host='127.0.0.1', port=5000, debug=True)
