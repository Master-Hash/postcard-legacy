from flask import render_template, request, redirect, abort, make_response
from flask.wrappers import Response
from postcard import app
from .functions import *
import asyncio

@app.route('/')
def index():
    return redirect("https://github.com/Master-Hash/postcard", 301)

@app.route('/teapot')
def egg():
    abort(418)

# @app.route('/debug/<int:code>')
# def tmp(code: int):
#     abort(code)

# 算了，难得整了
# @admin.errorhandler(404)
# def error_404(error):
#     return render_template("404.html", 404)

# @admin.errorhandler(500)
# def error_500(error):
#     return render_template("500.html", 500)

# @admin.errorhandler(400)
# def error_400(error):
#     return render_template("400.html", 400)

@app.route('/api')
def api() -> Response:
    _ip = request.access_route[0]
    _icons = {i:request.args[i] for i in request.args if i in icons}
    _items = asyncio.run(getSocial(_icons))

    if "img" in request.args and (_img:=request.args["img"]) in ("in", "ex"):
        if "src" in request.args:
            _src = request.args["src"]
        else:
            abort(400)
    else:
        _img = _src = None

    if _img == "in":
        _data = fileToBase64(_src)
    elif _img == "ex":
        _data = hrefToBase64(_src)
    else:
        _data = None

    _c = {i: (request.args[i] if i in request.args else required_param[i]) for i in required_param}

    svg = render_template(
        "api.svg",
        user_agent=request.user_agent,
        date=today(),
        ip=_ip,
        geo=getCity(_ip),
        items=_items,
        img=_img,
        data=_data,
        c=_c,
    )
    resp = make_response(svg)
    resp.mimetype = "image/svg+xml"
    return resp
