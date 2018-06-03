#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from jinja2 import Template, Environment

# app = Flask(name)
# app.jinja_env.trim_blocks = True

# @app.route('/')
# def hello():
# data = [['a', 'b'], 'c', [['d', 'e'], 'f']]
# return render_template('hello.html', data=data)

bad = '''
{% for element in data recursive %}
{% if element is string %}
<p>{{ element }}</p>
{% else %}
{{ loop(element) }}
{% endif %}
{% endfor %}
'''

good = '''
{% for element in data recursive %}
{% if element is string %}
<p>{{ element }}</p>
{% else %}
{{ loop(element) -}}
{% endif %}
{% endfor %}
'''

env = Environment(trim_blocks=True)
print(Template(bad).render(data=[['a', 'b'], 'c', [['d', 'e'], 'f']]))
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(Template(good).render(data=[['a', 'b'], 'c', [['d', 'e'], 'f']]))