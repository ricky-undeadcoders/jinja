from flask import Flask, render_template
from jinja2 import Environment, PackageLoader

# app = Flask(__name__, template_folder='C:\\Users\\Ricky\\PycharmProjects\\jinja\\ricky_test\\749')
#
env = Environment(lstrip_blocks=True, trim_blocks=False)
# env = Environment(lstrip_blocks=True, trim_blocks=True,
                  # loader=PackageLoader('app', 'C:\\Users\\Ricky\\PycharmProjects\\jinja\\ricky_test\\749'))
#
#
# @app.route('/')
# def index():
#     return env.get_template('base.html').render()
#     # return render_template('base.html')
#
#
# app.run(host='127.0.0.1', port=5000, debug=True)

print(env.from_string(
'''    <!-- 1 -->
    {%+ if True %}<!-- 2 -->
    foo<!-- 3 -->
    {%+ endif %}<!-- 4 -->
    <!-- 5 -->''').render())