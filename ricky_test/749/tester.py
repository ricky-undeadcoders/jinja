from jinja2 import Environment
env = Environment(lstrip_blocks=False, trim_blocks=False)
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
print(env.from_string(str7481).render())
print(env.from_string(str7482).render())