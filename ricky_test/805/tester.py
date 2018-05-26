from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
t = env.get_template('test.html')
t.module.test()