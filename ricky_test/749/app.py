from flask import Flask, render_template
from jinja2 import Environment, PackageLoader

# app = Flask(__name__, template_folder='C:\\Users\\Ricky\\PycharmProjects\\jinja\\ricky_test\\749')
#
env = Environment(lstrip_blocks=False, trim_blocks=False)
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
str7481 = '''
    <!-- 1 -->
    {%+ if True %}<!-- 2 -->
    foo<!-- 3 -->
    {% endif %}<!-- 4 -->
    <!-- 5 -->'''

str7482 = '''
    <!-- 1 -->
    {% if True %}<!-- 2 -->
    foo<!-- 3 -->
    {%+ endif %}<!-- 4 -->
    <!-- 5 -->'''

'''
When lstrip_blocks == False: jinja2.exceptions.TemplateSyntaxError: tag name expected
'''

str749 = '''
    <!-- 1 -->
    {%- if True -%}<!-- 2 -->
    foo<!-- 3 -->
    {%- endif -%}<!-- 4 -->
    <!-- 5 -->'''

'''
No matter lstrip_blocks or trim_blocks: jinja2.exceptions.TemplateSyntaxError: unexpected 'end of statement block'
I believe this is incorrect syntax; 
'''

str750 = '''    
    <!-- 1 -->
    {% if True %}              <!-- 2 -->
    foo<!-- 3 -->
    {%- endif %}<!-- 4 -->
    <!-- 5 -->'''

# print(env.from_string(str7481).render())
# print(env.from_string(str7482).render())
print(env.from_string(str749).render())
print(env.from_string(str750).render())

