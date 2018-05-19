from jinja2 import Environment

env = Environment(lstrip_blocks=False, trim_blocks=False)

str7481 = '''
    {%+ if True %}
    foo
    {% endif %}'''

str7482 = '''
    <!-- 1 -->
    {% if True %}<!-- 2 -->
    foo<!-- 3 -->
    {%+ endif %}<!-- 4 -->
    <!-- 5 -->'''

'''
When lstrip_blocks == False: jinja2.exceptions.TemplateSyntaxError: tag name expected
'''

print(env.from_string(str7481).render())
print(env.from_string(str7482).render())

