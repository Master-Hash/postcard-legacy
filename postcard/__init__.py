from flask import Flask

app = Flask(__name__, static_folder="../API/res", static_url_path="/static")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from postcard import views
