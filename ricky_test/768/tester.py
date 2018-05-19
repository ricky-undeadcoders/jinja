#!/usr/bin/python3
# -*- coding: utf-8 -*-

import jinja2

print(jinja2.__version__)


@jinja2.contextfunction
def myContextFunction(ctx):
    return f"myContextFunction: ctx['myI'] = {ctx['myI']}"


tmplt = """
 {% for i in range(2): %}
 {%- set  myI = i -%}
     {{ myContextFunction() }}
     In template myI = {{ myI }}
 {% endfor %}
 """
template = jinja2.Template(tmplt)
template.globals['myContextFunction'] = myContextFunction
print(template.render())
#
# context = {'myI' : 0}
# print(template.render(**context))

# myContextFunction: ctx['myI'] = 0
#         In template myI = 0
# myContextFunction: ctx['myI'] = 0
#         In template myI = 1
