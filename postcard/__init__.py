from flask import Flask
# from jinja2 import Environment, select_autoescape

app = Flask(__name__)
# env = Environment(
#     autoescape=select_autoescape(
#         enabled_extensions=('html', 'svg'),
#         default_for_string=True,
# ))

from postcard import views
